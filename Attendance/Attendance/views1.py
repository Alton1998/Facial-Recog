from rest_framework.views import APIView
from rest_framework.response import Response
from Attendanceapp.models import StartAttendance
from .serializer import AttendanceSerializer
class AttendanceAPI(APIView):
    def get(self,request):
        data=StartAttendance.objects.all().order_by('id')
        lastupdate=data.reverse()[:1]
        serializer=AttendanceSerializer(lastupdate,many=True)
        return Response(serializer.data)