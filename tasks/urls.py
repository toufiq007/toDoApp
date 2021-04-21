from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('update/<str:pk>/',views.update_file,name='update'),
    path('delete/<str:pk>/',views.delete_file,name='delete')
]
