from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from .functions import *
import data.models
# assume that I get a account_instance from Bora
'''
stu2 = data.models.Account.objects.all()[1]
stu3 = data.models.Account.objects.all()[2]
stu4 = data.models.Account.objects.all()[3]
notification1 = data.models.Notification.objects.all()[0]
notification2 = data.models.Notification.objects.all()[1]
notification3 = data.models.Notification.objects.all()[2]
'''


def get_current_account():
    """
    get current account()
    :return:
    """
    stu2 = data.models.Account.objects.all()[1]
    return stu2


def notification_requested(request):
    """
    :param request:
    :return: render with list_notifications
    """
    return render(request, 'student_notification.html',
                  {'list_notification': account_get_notification(get_current_account())})


def read_nofitication(request):
    """
    :param request:
    :return: True or False
    """
    temp_str = request.get_full_path()
    notification_id = temp_str.split("read/")[-1]
    temp_obj = data.models.Notification.objects.filter(notification_id=notification_id)
    if not temp_obj:
        print("ERROR: cant find the notification")
        return False
    else:
        temp_obj[0].read = True
        temp_obj[0].save()
        return HttpResponseRedirect('/notification')
