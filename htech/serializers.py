from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework import exceptions
from booking.models import Booking
from company.models import Company
from attendance.models import Attendance
from django.contrib.auth.models import User

from duty.models import Duty
from dutyHistory.models import DutyHistory
from guard.models import Guard
from permission.models import Permission
from role.models import Role
from roleUser.models import RoleUser
from staff.models import Staff


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'is_superuser', 'is_active')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')


class RoleUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    role = RoleSerializer()

    class Meta:
        model = RoleUser
        fields = ('role', 'user')


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name')


class CompanySerializer(serializers.ModelSerializer):
    building = BuildingSerializer()

    class Meta:
        model = Company
        fields = ('id', 'name', 'owner', 'building_id', 'building', 'mobile', 'email', 'status', 'authorize_person')


class StaffSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Staff
        fields = ('id', 'staff_id', 'name', 'mobile', 'rf_id', 'company', 'status', 'profile_image')


class GuardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guard
        fields = ('id', 'guard_id', 'name', 'nid', 'mobile', 'rf_id', 'status')


class BookingSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    user = UserSerializer()

    class Meta:
        model = Booking
        fields = ('id', 'name', 'company', 'user', 'mobile', 'guest_quantity', 'date_time', 'note', 'is_attendance')


class AttendanceSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    booking = BookingSerializer()
    authorized_by = UserSerializer()

    class Meta:
        model = Attendance
        fields = (
            'id', 'type', 'staff', 'authorized_by', 'booking', 'in_time', 'out_time', 'gate_no', 'out_gate_no',
            'vehicle',
            'person_quantity', 'vehicle_quantity', 'note')


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'moduled', 'create_permission', 'edit_permission', 'view_permission', 'delete_permission',
                  'share_permission', 'role_id')


class DutySerializer(serializers.ModelSerializer):
    guard = GuardSerializer()

    class Meta:
        model = Duty
        fields = ('id', 'guard', 'gate_no', 'from_time', 'to_time')


class DutyHistorySerializer(serializers.ModelSerializer):
    guard = GuardSerializer()

    class Meta:
        model = DutyHistory
        fields = ('id', 'gate_no', 'login_time', 'logout_time', 'guard')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Please provide username and password both."
            raise exceptions.ValidationError(msg)
        return data
