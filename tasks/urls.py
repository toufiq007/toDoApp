from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('update/<str:pk>/',views.update_file,name='update')
]
