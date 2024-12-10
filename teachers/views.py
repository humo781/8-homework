from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teacher/teacher_list.html', ctx)

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    ctx = {'teacher': teacher}
    return render(request, 'teacher/teacher_detail.html', ctx)

def teacher_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')
        if first_name and last_name and subject:
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                subject=subject
            )
        return redirect('teachers:list')
    else:
        return render(request, 'teacher/create.html')

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teachers:list')
