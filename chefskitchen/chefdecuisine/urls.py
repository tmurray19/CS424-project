from django.urls import path

from . import views

urlpatterns = [
        path('chef/id/<int:souschef_id>', views.souschef),
        path('chefs/', views.souschef_list),
       
]
