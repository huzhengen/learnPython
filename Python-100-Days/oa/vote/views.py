from django.shortcuts import render, redirect
from vote.models import Subject


def show_subjects(request):
    """查看所有学科"""
    subjects = Subject.objects.all()
    return render(request, 'subject.html', {'subjects': subjects})

def show_teachers(request):
    """显示指定学科的老师"""
    try:
        sno = int(request.GET['sno'])
        subject = Subject.objects.get(no=sno)
        teachers = subject.teacher_set.all()
        return render(request, 'teachers.html', {'subject': subject, 'teachers': teachers})
    except (KeyError, ValueError, Subject.DoesNotExist):
        return redirect('/')