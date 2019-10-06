from django.shortcuts import render
from data import models as DataModel
from myclasses.views import getMyClass

def getIDInstance():
    """
    :return: current student instance who clicked
    """
    return DataModel.Account.objects.all()[2]

def getAllProfile(s_ins):
    """
    :param s_ins: user instance for retrieve profiles
    :return: all profiles user has
    """
    fname = s_ins.first_name
    lname = s_ins.last_name
    email = s_ins.email
    is_instructor_of = DataModel.Class.objects.filter(instructor_instance=s_ins)
    photo = s_ins.photo
    descrip_by_class = DataModel.Description.objects.filter(student_instance=s_ins)
    class_enroll = getMyClass(s_ins)
    skill = DataModel.Skill_label.objects.filter(student_instance=s_ins)
    list = [fname, lname, email, is_instructor_of,
            photo, descrip_by_class, class_enroll,
            skill]
    return list

def listRequested(request):
    list = getAllProfile(getIDInstance())

    '''
    hm = {}
        for sins in list[7]:
        if (sins.class_instance.class_name in hm):
            hm[sins.class_instance.class_name].append(sins.label)
        else:
            hm[sins.class_instance.class_name] = [sins.label]
    list[7] = hm
    '''

    return render(request, 'userprofile.html', {
        'fname':list[0],
        'lname':list[1],
        'email':list[2],
        'incins':list[3],
        'photo':list[4],
        'desins':list[5],
        'encins':list[6],
        'sins':list[7]
    })
