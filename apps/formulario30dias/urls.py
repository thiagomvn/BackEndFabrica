from django.urls import path
from .views import FormularioCreateView, FormularioListView

urlpatterns = [

    path('create/', FormularioCreateView.as_view(), name='formulario-create'),
    path('list/', FormularioListView.as_view(), name='formulario-list'),

]