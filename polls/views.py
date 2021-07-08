from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializer import EmployeeSerializer


@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        serializer = EmployeeSerializer(Employee.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response("", status=status.HTTP_405_METHOD_NOT_ALLOWED)
