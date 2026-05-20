from rest_framework import generics
from .serializers import FormularioSerializer
from .models import Formulario

class FormularioCreateView(generics.CreateAPIView):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer

class FormularioListView(generics.ListAPIView):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer