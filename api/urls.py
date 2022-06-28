from django.urls import path
from api import views

app_name = "api"

urlpatterns = [
    path("child/", views.ChildView.as_view()),
    path("grandchild/", views.GrandChildView.as_view()),
    path("grandchildfemale/", views.GrandChildFemaleView.as_view()),
    path("aunt/", views.AuntView.as_view()),
    path("cousin/", views.CousinView.as_view()),
]
