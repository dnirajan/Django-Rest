from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets



#for all crud operations
class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

# readony viewset
# class StudentViewset(viewsets.ReadOnlyModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
   