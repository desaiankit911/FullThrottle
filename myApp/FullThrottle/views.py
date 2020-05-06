from django.shortcuts import render
# from django.http import HttpResponse
from FullThrottle.models import *
from django.contrib.auth.forms import UserCreationForm
from FullThrottle.forms import HomeForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import json


# Create your views here.


def index(request):
    return render(request, 'personal/home.html')


def home(request):
    users = UserData.objects.all()
    # for i in users:
    # print(i.id)
    d = json.dumps(UserData.objects.all())
    print(d)
    data = timeStamp.objects.filter(
        user_id_id=81).prefetch_related('user_id')
    return render(request, 'personal/home.html')


# def download(request):
    # one_entry = timeStamp.objects.get(pk=81)
