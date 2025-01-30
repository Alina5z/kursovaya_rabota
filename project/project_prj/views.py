from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from .models import Task, Orders
from .forms import TaskForm
from django.views.generic import DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'project_prj/index.html', {
        'title': 'Главная страница сайта', 'tasks': tasks})


def add_order(request, pk):
    print('ДОБАВЛЕН ', pk)
    print('USER ', request.user)
    get_task = Task.objects.get(id=pk)
    t = Orders(owner=request.user, task=get_task)
    t.save()
    # tasks = Task.objects.order_by('-id')
    # return render(request, 'project_prj/index.html', {
    #     'title': 'Главная страница сайта', 'tasks': tasks})
    messages.info(request, 'Вы добавили в корзину: ' + get_task.name)
    return HttpResponseRedirect('/')


def rasp(request):
    return render(request, 'project_prj/rasp.html')


def news(request):
    return render(request, 'project_prj/news.html')


class TaskListView(ListView):
    model = Task
    template_name = 'blog/task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список заявок'
        return context


def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверно'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'project_prj/create.html', context)


class Del(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'project_prj/task-delete.html'


class Upd(UpdateView):
    model = Task
    template_name = 'project_prj/create.html'
    form_class = TaskForm
    success_url = '/'


class UserOrdersListView(ListView):
    model = Orders
    context_object_name = 'orders'
    extra_context = {'title': 'История записей'}

    def get_queryset(self):
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Orders.objects.filter(owner=self.request.user).order_by('-created')
