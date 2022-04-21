#Generic Api View and Model Mixin
from .serializers import StudentSerializer
from .models import Student
# from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class StudentLC(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class= StudentSerializer

class StudentR(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class= StudentSerializer