from django.shortcuts import render, get_object_or_404, redirect
from .models import Group


def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'group/group_list.html', ctx)

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    ctx = {'group': group}
    return render(request, 'group/group_detail.html', ctx)

def group_create(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group_type = request.POST.get('group_type')
        if group_name and group_type:
            Group.objects.create(
                group_name=group_name,
                group_type=group_type
            )
        return redirect('groups:list')
    else:
        return render(request, 'group/create.html')

def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('groups:list')
