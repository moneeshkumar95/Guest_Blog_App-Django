from django.urls import path
from . import  views
from .models import *

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('my_blogs',views.myblogs, name= 'my_blogs'),
    path('publish_blog',views.publishblog, name='publish_blog'),
    path('my_blogs/edit_blog/<int:pk>',views.editblog, name= 'edit_blog'),
    path('my_blogs/delete_blog/<int:pk>',views.deleteblog, name= 'delete_blog'),
    path('blog/<str:pk>/', views.detailview, name= 'detailview')
]