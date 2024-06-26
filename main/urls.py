from django.urls import path
from main import views

urlpatterns = [
    path("",views.index,name="index"),
    path("dashboard",views.dashbord,name="dashboard"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"), 
    path("register",views.register,name="register"),
    path("add-record",views.add_record,name="add-record"), 
    path("update-record/<int:pk>",views.update_record,name="update-record"),
    path("view/<int:pk>",views.view_record,name="view"), 
    path("delete/<int:pk>",views.delete_record,name="delete"), 
]
