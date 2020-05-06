from django.core.management.base import BaseCommand, CommandError
from FullThrottle.models import UserData
from FullThrottle.models import timeStamp
from FullThrottle.models import UserDataForm


class Command(BaseCommand):
    help = 'custom management command to populate the database'

    def handle(self, *args, **options):
        user = ["Ankit Desai", "Egon Spengler"]
        user_id = ["W033A3SDE", "W012A3CDE"]
        tz = ["India/Mumbai", "America/Los_Angeles"]
        start_time = ["Feb 1 2020  1:33PM",
                      "Mar 1 2020  11:11AM", "Mar 16 2020  5:33PM"]
        end_time = ["Feb 1 2020 1:54PM",
                    "Mar 1 2020 2:00PM", "Mar 16 2020 8:02PM"]

        for i in range(len(user)):
            data1 = UserData(real_name=user[i],
                             user_id=user_id[i], tz=tz[i])

        for i in range(len(start_time)):
            for j in range(len(user)):
                data1 = UserData(real_name=user[j],
                                 user_id=user_id[j], tz=tz[j])

                # check if user already exit or not
                if not UserData.objects.filter(user_id=user_id[j]).exists():
                    data1.save()
                    data2 = timeStamp(
                        user_id=data1, start_time=start_time[i], end_time=end_time[i])
                    data2.save()
                else:
                    data1 = UserData.objects.get(user_id=user_id[j])
                    data2 = timeStamp(user_id=data1,
                                      start_time=start_time[i], end_time=end_time[i])
                    data2.save()
        return 'User Data Created'
