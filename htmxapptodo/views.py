from django.shortcuts import render

# Create your views here.
# from .models import Task
# from django.http import HttpResponse

# Create your views here.
def task_list(request):
    # tasks = Task.objects.all()
    # context = {'tasks': tasks}
    # return render(request, 'task_list.html', context)
    return render(request, 'htmxapptodo/task_list.html')