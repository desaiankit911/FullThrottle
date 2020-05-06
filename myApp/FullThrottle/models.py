from django.db import models
from django.forms import ModelForm


class UserData(models.Model):
    real_name = models.CharField(max_length=250)
    user_id = models.CharField(max_length=250)
    tz = models.CharField(max_length=250)

    def __str__(self):
        return self.tz
    '''
    as given formate is 'month date year and time' which is not approprate for DateTimeField
    thats why CharFiled
    '''


class timeStamp(models.Model):
    user_id = models.ForeignKey(
        UserData, verbose_name='UserData', default=1, on_delete=models.SET_DEFAULT)
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)


class UserDataForm(ModelForm):
    class Meta:
        model = UserData
        # fields = '__all__'
        fields = ['user_id']
