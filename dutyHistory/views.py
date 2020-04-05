from django.http import JsonResponse

from dutyHistory.models import DutyHistory
from htech.globalMethods import GetListData
from htech.serializers import DutyHistorySerializer


def index(request):
    duty = GetListData()
    data = duty.get(request, DutyHistory.objects.all(), DutyHistorySerializer, 'DutyHistory')
    return JsonResponse({
        'data': data[0],
        'totalItems': data[1],
    })