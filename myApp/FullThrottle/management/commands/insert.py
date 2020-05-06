from django.core.management.base import BaseCommand, CommandError
from FullThrottle.models import UserData
from FullThrottle.models import timeStamp
from FullThrottle.models import UserDataForm
import json
import os


class Command(BaseCommand):
    help = 'custom management command to populate the database'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        lists_file = options['file']

        with open(lists_file) as input_file:
            data = json.load(input_file)

        data = data['members']

        for i in range(len(data)):
            data1 = UserData(real_name=data[i]['real_name'],
                             user_id=data[i]['id'], tz=data[i]['tz'])
            dataTime = data[i]['activity_periods']
            if not UserData.objects.filter(user_id=data[i]['id']).exists():
                data1.save()
                for j in range(len(dataTime)):
                    data2 = timeStamp(
                        user_id=data1, start_time=dataTime[j]['start_time'], end_time=dataTime[j]['end_time'])
                    data2.save()
            else:
                for j in range(len(dataTime)):
                    data1 = UserData.objects.get(user_id=data[i]['id'])
                    data2 = timeStamp(user_id=data1,
                                      start_time=dataTime[j]['start_time'], end_time=dataTime[j]['end_time'])
                    data2.save()
        return 'User Data Uploded'
