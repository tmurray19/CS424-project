from django.urls import path

from . import views

urlpatterns = [
        path('chef/id/<int:souschef_id>', views.souschef, name='souschef_profile'),
        path('chefs/', views.souschef_list),
        path('chef/update/id/<int:souschef_id>', views.souschef_update, name='souschef_update'),
        
       
]
