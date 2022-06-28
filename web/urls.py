from django.urls import path
from web import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", TemplateView.as_view(
        template_name="home.html"), name="home"),

    path("parent", views.ParenView.as_view(), name="parent"),
    path("parent/<int:pk>", views.DeleteParentView.as_view(), name="parentdelete"),
    path("parent/update/<int:pk>",
         views.UpdateParentView.as_view(), name="parentUpdate"),
    path("child", views.ChildView.as_view(), name="child"),
    path("child/<int:pk>", views.DeleteChildView.as_view(), name="childdelete"),
    path("child/update/<int:pk>",
         views.UpdateChildView.as_view(), name="childUpdate"),

    path("grandchild", views.GrandChildView.as_view(), name="grandchild"),
    path("grandchild/<int:pk>", views.DeleteGrandChildView.as_view(),
         name="grandchilddelete"),
    path("grandchild/update/<int:pk>",
         views.UpdateGrandChildView.as_view(), name="grandchildUpdate"),
]
