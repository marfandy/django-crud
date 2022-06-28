from django.db import models


class Gender(models.TextChoices):
    Male = "male"
    Female = "female"


class Parents(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=Gender.choices)

    def __str__(self):
        return str(self.name)


class Child(models.Model):
    fk_parent = models.ForeignKey(
        Parents, related_name="child", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=Gender.choices)

    def __str__(self):
        return str(self.name)


class GrandChild(models.Model):
    fk_child = models.ForeignKey(
        Child, related_name="grandchild", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=Gender.choices)

    def __str__(self):
        return str(self.name)
