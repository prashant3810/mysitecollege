from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from college.models import Student, Staff, StudentReg

from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, "college/main.html")


def student_application(request):
    return render(request, "college/application.html")


def save_application(request):
    Student.objects.create(student_name=request.POST['student_name'], phone_num=request.POST['phone_num'],
                           student_mail=request.POST['student_mail'],
                           ssc_marks=request.POST['ssc_marks'], pu_marks=request.POST['pu_marks'])
    return HttpResponseRedirect("/college/")


def student_reg(request):
    return render(request, "college/student_reg.html")


def save_std_reg(request):
    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
    student = Student.objects.get(student_mail=request.POST['student_mail'])
    StudentReg.objects.create(student_dep=request.POST['student_dep'], user=user, student=student)
    return HttpResponseRedirect("/college/")


def student_login(request):
    return render(request, "college/student_login.html")


def student_log_status(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/college/std_detail/")
    else:
        return HttpResponse("<h3>your username and password did not match</h3>")


def staff_reg(request):
    return render(request, "college/staff_reg.html")


def save_staff_reg(request):
    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
    Staff.objects.create(staff_name=request.POST['staff_name'],
                         staff_dep=request.POST['staff_dep'],
                         staff_mail=request.POST['staff_mail'],
                         staff_phone_num=request.POST['staff_phone_num'],
                         staff_qualifications=request.POST['staff_qualifications'],
                         staff_experience=request.POST['staff_experience'], user=user)
    return HttpResponseRedirect("/college/")


def staff_login(request):
    return render(request, "college/staff_login.html")


def staff_log_status(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/college/staff_detail/")
    else:
        return HttpResponse("<h3>your username and password did not match</h3>")


@login_required()
def std_detail(request):
    user = request.user
    return render(request, "college/std_detail.html", {'user': user})


@login_required()
def staff_detail(request):
    user = request.user
    return render(request, "college/staff_detail.html", {'user': user})


def student_logout(request):
    logout(request)
    return HttpResponseRedirect("/college/student_login/")


def staff_logout(request):
    logout(request)
    return HttpResponseRedirect("/college/staff_login/")


@login_required()
def student_list(request):
    # user_list = StudentReg.objects.all()
    return render(request, "college/studentlist.html")


@login_required()
def staff_list(request):
    # stf_list = Staff.objects.all()
    return render(request, "college/staff_list.html")


def staff_ece(request):
    stf_list = Staff.objects.filter(staff_dep='ece')
    return render(request, 'college/staff_ece.html', {'stf_list': stf_list})


def staff_eee(request):
    stf_list = Staff.objects.filter(staff_dep='eee')
    return render(request, 'college/staff_eee.html', {'stf_list': stf_list})


def staff_it(request):
    stf_list = Staff.objects.filter(staff_dep='IT')
    return render(request, 'college/staff_it.html', {'stf_list': stf_list})


def staff_mec(request):
    stf_list = Staff.objects.filter(staff_dep='mech')
    return render(request, 'college/staff_mec.html', {'stf_list': stf_list})


def staff_cse(request):
    stf_list = Staff.objects.filter(staff_dep='cse')
    return render(request, 'college/staff_cse.html', {'stf_list': stf_list})


def std_ece(request):
    std_list = StudentReg.objects.filter(student_dep='ece')
    return render(request, 'college/student_ece.html', {'std_list': std_list})


def std_eee(request):
    std_list = StudentReg.objects.filter(student_dep='eee')
    return render(request, 'college/student_eee.html', {'std_list': std_list})


def std_cse(request):
    std_list = StudentReg.objects.filter(student_dep='cse')
    return render(request, 'college/student_cse.html', {'std_list': std_list})


def std_it(request):
    std_list = StudentReg.objects.filter(student_dep='IT')
    return render(request, 'college/student_it.html', {'std_list': std_list})


def std_mec(request):
    std_list = StudentReg.objects.filter(student_dep='mech')
    return render(request, 'college/student_mec.html', {'std_list': std_list})


def std_dep(request):
    stf_list = Staff.objects.all()
    return render(request, "college/student_dep.html")

# def staff_dep(request,staff_dep):
#     if staff_dep == 'ece':
#         stu_dep = StudentReg.objects.filter(student_dep='ece')
#         return render(request, "college/staff_ece.html", {'stu_dep': stu_dep})
#
#     elif staff_dep == 'eee':
#         stf_list = Staff.objects.filter(staff_dep='eee')
#         return render(request, 'college/staff_eee.html', {'stf_list': stf_list})
#     elif staff_dep == 'mech':
#         stf_list = Staff.objects.filter(staff_dep='mech')
#         return render(request, 'college/staff_mec.html', {'stf_list': stf_list})
#
#     elif staff_dep == 'cse':
#         stf_list = Staff.objects.filter(staff_dep='cse')
#         return render(request, 'college/staff_cse.html', {'stf_list': stf_list})
#     elif staff_dep == 'it':
#         stf_list = Staff.objects.filter(staff_dep='it')
#         return render(request, 'college/staff_it.html', {'stf_list': stf_list})
