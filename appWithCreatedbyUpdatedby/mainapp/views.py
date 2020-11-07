from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from .models import mainModel
from .forms import mainForm


def index(request, num=1):
    data = mainModel.objects.all()
    page = Paginator(data, 3)
    params = {
        'login_user': request.user,
        'data': page.get_page(num),
    }
    return render(request, 'mainapp/index.html', params)


def create(request):
    obj = mainModel()
    # POST
    if (request.method == 'POST'):
        # フォームを生成
        form = mainForm(request.POST, instance=obj)
        if form.is_valid():  # バリデーションがOKなら保存
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.updated_by = request.user
            obj.save()
            return redirect(to='/mainapp')
    # GET
    form = mainForm(instance=obj)
    params = {
        'login_user': request.user,
        'form': form,
    }
    return render(request, 'mainapp/create.html', params)


def edit(request, num):
    obj = get_object_or_404(mainModel, pk=num)
    # POST
    if (request.method == 'POST'):
        # form
        form = mainForm(request.POST, instance=obj)
        if form.is_valid():  # バリデーションがOKなら保存
            obj = form.save(commit=False)
            obj.updated_by = request.user
            obj.save()
            return redirect(to='/mainapp')
        # GET
    form = mainForm(instance=obj)
    params = {
        'login_user': request.user,
        'id': num,
        'form': form,
    }
    return render(request, 'mainapp/edit.html', params)


def delete(request, num):
    obj = get_object_or_404(mainModel, pk=num)
    if (request.method == 'POST'):
        obj.delete()
        return redirect(to='/mainapp')
    params = {
        'login_user': request.user,
        'id': num,
        'obj': obj,
    }
    return render(request, 'mainapp/delete.html', params)
