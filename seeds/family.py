import json
import os

currentpath = os.path.dirname(os.path.abspath(__file__))


def populate(apps, schema_editor):
    Parents = apps.get_model('api', 'Parents')
    Child = apps.get_model('api', 'Child')
    GrandChild = apps.get_model('api', 'GrandChild')

    print("Populating parent")
    file = open(os.path.join(currentpath, 'data.json'), 'r')
    parents = json.load(file)
    file.close()

    parents_objs = []
    for parent in parents:
        parent_obj = Parents(
            name=parent['name'],
            gender=parent["gender"],
        )
        parents_objs.append(parent_obj)

    Parents.objects.bulk_create(parents_objs)

    print("Populating child")
    file = open(os.path.join(currentpath, 'child.json'), 'r')
    childs = json.load(file)
    file.close()

    childs_objs = []
    for child in childs:
        parent = Parents.objects.filter(
            name__icontains=child['fk_parent']).first()
        childs_obj = Child(
            fk_parent=parent,
            name=child['name'],
            gender=child["gender"],
        )
        childs_objs.append(childs_obj)

    Child.objects.bulk_create(childs_objs)

    print("Populating grandchild")
    file = open(os.path.join(currentpath, 'grandchild.json'), 'r')
    grandchilds = json.load(file)
    file.close()

    grandchilds_objs = []
    for grandchild in grandchilds:
        parent = Child.objects.filter(
            name__icontains=grandchild['fk_child']).first()
        grandchilds_obj = GrandChild(
            fk_child=parent,
            name=grandchild['name'],
            gender=grandchild["gender"],
        )
        grandchilds_objs.append(grandchilds_obj)

    GrandChild.objects.bulk_create(grandchilds_objs)
