from django.shortcuts import render
from FullThrottle.models import *
from FullThrottle.forms import HomeForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import json

# Create your views here.


def index(request):
    return render(request, 'personal/home.html')


def home(request):
    # at each load data from all DB fetch and store in the form of Dictionary which later converted into JSON
    data = {"ok": True, "members": []}
    users = UserData.objects.all()
    for user in users:
        details = {}
        activity_periods = []
        details['id'] = user.user_id
        details['real_name'] = user.real_name
        details['tz'] = user.tz
        dateTimes = timeStamp.objects.filter(
            user_id_id=user.id).prefetch_related('user_id')
        timeZone = {}
        for dateTime in dateTimes:
            timeZone['start_time'] = dateTime.start_time
            timeZone['end_time'] = dateTime.end_time
            activity_periods.append(timeZone)
        details['activity_periods'] = activity_periods
        data['members'].append(details)
        json.dump(data, open("json/out.json", "w"))

    return render(request, 'personal/home.html')
