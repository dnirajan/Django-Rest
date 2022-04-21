from django.shortcuts import render
from .models import Student
from .searializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer


# Create your views here.

def student_detail(request, pk):
    obj1 = Student.objects.get(id=pk)
    serializer = StudentSerializer(obj1)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)


# Query Set : All student data
def student_list(request):
    obj1 = Student.objects.all()
    serializer = StudentSerializer(obj1, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data, safe=False)
