from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Article
from django.utils import timezone

# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        pass_word = request.POST['密码']
        user = auth.authenticate(username=user_name, password=pass_word)
        if user is None:
            return render(request, 'login.html', {'错误': '用户名或密码错误'})
        else:
            auth.login(request, user)
            return redirect('主页')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        password1 = request.POST['密码']
        password2 = request.POST['确认密码']
        try:
            User.objects.get(username=user_name)
            return render(request, 'signup.html', {'用户名错误': '该用户名已存在'})
        except User.DoesNotExist:
            if password1 == password2:
                User.objects.create_user(username=user_name, password=password1)
                return redirect('主页')
            else:
                return render(request, 'signup.html', {'密码错误': '两次密码输入不一致'})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('主页')


def article(request, article_id):
    page = get_object_or_404(Article, pk=article_id)
    return render(request, 'page.html', {'page': page})


@login_required
def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    elif request.method == 'POST':
        title = request.POST['💗の名字']
        sTitle = request.POST['💗の小名']
        article = request.POST['💗の话']
        try:
            icon = request.POST['萌萌の样子']
            image = request.POST['💗の样子']

            articles = Article()
            articles.title = title
            articles.sTitle = sTitle
            articles.article = article
            articles.icon = icon
            articles.image = image

            articles.pub_data = timezone.datetime.now()
            articles.publisher = request.user
            articles.save()
            return redirect('主页')
        except Exception as err:
            return render(request, 'publish.html', {'错误': '请上传图片哦'})




