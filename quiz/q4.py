from polls.models import Employee
from polls.serializer import EmployeeSerializer

q = Employee(name="kevin", address="taipei", age=25)
q.save()

q2 = Employee(name="kochi", address="taipei 2", age=24)
q2.save()

serializer = EmployeeSerializer(Employee.objects.all(), many=True)
print(serializer.data)
