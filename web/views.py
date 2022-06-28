from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView, RedirectView

from api.models import Child, GrandChild, Parents


class HomeView(TemplateView):
    template_name = "home.html"


class ParenView(TemplateView):
    template_name = "parent.html"

    def get(self, request):
        data = Parents.objects.all()

        context = {
            'datas': data
        }
        return render(request, self.template_name, context)

    def post(self, request):
        parentid = request.POST['parent_id']
        if parentid == "":
            parentid = None
        Parents.objects.update_or_create(id=parentid, defaults={
            "name": request.POST['nama'],
            "gender": request.POST['gender']
        })

        data = Parents.objects.all()
        context = {
            'datas': data
        }
        return render(request, self.template_name, context)


class DeleteParentView(RedirectView):
    pattern_name = 'web:parent'

    def get(self, *args, **kwargs):
        delete_id = kwargs['pk']
        Parents.objects.filter(id=delete_id).delete()
        return redirect(self.pattern_name)


class UpdateParentView(TemplateView):
    template_name = "parent.html"

    def get(self, request, *args, **kwargs):
        update_id = kwargs['pk']
        data_update = Parents.objects.get(id=update_id)
        data = Parents.objects.all()
        context = {
            'datas': data,
            'data_update': data_update
        }
        return render(request, self.template_name, context)


class ChildView(TemplateView):
    template_name = "child.html"

    def get(self, request):
        data = Child.objects.all()
        parent = Parents.objects.all()

        context = {
            'datas': data,
            'parent': parent
        }
        return render(request, self.template_name, context)

    def post(self, request):
        parentid = request.POST['parent_id']
        print(request.POST['orangtua'])
        if parentid == "":
            parentid = None
        Child.objects.update_or_create(id=parentid, defaults={
            "fk_parent_id":  request.POST['orangtua'],
            "name": request.POST['nama'],
            "gender": request.POST['gender']
        })

        parent = Parents.objects.all()
        data = Child.objects.all()
        context = {
            'datas': data,
            'parent': parent

        }
        return render(request, self.template_name, context)


class DeleteChildView(RedirectView):
    pattern_name = 'web:child'

    def get(self, *args, **kwargs):
        delete_id = kwargs['pk']
        Child.objects.filter(id=delete_id).delete()
        return redirect(self.pattern_name)


class UpdateChildView(TemplateView):
    template_name = "child.html"

    def get(self, request, *args, **kwargs):
        update_id = kwargs['pk']
        data_update = Child.objects.get(id=update_id)
        data = Child.objects.all()
        parent = Parents.objects.all()
        context = {
            'datas': data,
            'parent': parent,
            'data_update': data_update
        }
        return render(request, self.template_name, context)


class GrandChildView(TemplateView):
    template_name = "grandchild.html"

    def get(self, request):
        data = GrandChild.objects.all()
        parent = Child.objects.all()

        context = {
            'datas': data,
            'parent': parent
        }
        return render(request, self.template_name, context)

    def post(self, request):
        parentid = request.POST['parent_id']
        print(request.POST['orangtua'])
        if parentid == "":
            parentid = None
        GrandChild.objects.update_or_create(id=parentid, defaults={
            "fk_child_id":  request.POST['orangtua'],
            "name": request.POST['nama'],
            "gender": request.POST['gender']
        })

        parent = Child.objects.all()
        data = GrandChild.objects.all()
        context = {
            'datas': data,
            'parent': parent

        }
        return render(request, self.template_name, context)


class DeleteGrandChildView(RedirectView):
    pattern_name = 'web:grandchild'

    def get(self, *args, **kwargs):
        delete_id = kwargs['pk']
        GrandChild.objects.filter(id=delete_id).delete()
        return redirect(self.pattern_name)


class UpdateGrandChildView(TemplateView):
    template_name = "grandchild.html"

    def get(self, request, *args, **kwargs):
        update_id = kwargs['pk']
        data_update = GrandChild.objects.get(id=update_id)
        data = GrandChild.objects.all()
        parent = Child.objects.all()
        context = {
            'datas': data,
            'parent': parent,
            'data_update': data_update
        }
        return render(request, self.template_name, context)
