from rest_framework import serializers
from Attendanceapp.models import StartAttendance,Present

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=StartAttendance
        fields='__all__'
class PresentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Present
        fields='__all__'
