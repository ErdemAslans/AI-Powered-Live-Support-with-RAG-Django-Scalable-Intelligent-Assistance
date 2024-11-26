from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, f'{request.user.username} Daha önce oturum açılmış.')
        return redirect('home_view')
    context = dict()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if len(username) < 20:
            messages.warning(request,"Lütfen Geçerli Bir Email Giriniz. ")
            return redirect('user_profile:login_view')
        if len(password) <7:
            messages.warning(request,"Lütfen Geçerli Bir Şifre Giriniz. ")
            return redirect('user_profile:login_view')
        if user is not None:
            login(request, user)
            messages.success(request, 'Başarıyla Giriş Yapıldı')
            return redirect('home_view')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre yanlış')
    return render(request, 'login.html', context)

def logout_view(request):
    messages.info(request, f'{request.user.username} Oturum Kapatıldı.')
    logout(request)
    return redirect('home_view')

from django.contrib.auth.models import User
from .models import Profile

def register_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        username_confirm = request.POST.get('username-confirm')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password-confirm')

        if username != username_confirm:
            messages.warning(request, "Lütfen Email Bilgisini Doğru Giriniz.")
            return redirect('user_profile:register_view')
        if password != password_confirm:
            messages.warning(request, "Lütfen Şifre Bilgisini Doğru Giriniz.")
            return redirect('user_profile:register_view')
        if len(username) < 20:
            messages.warning(request, "Lütfen Geçerli Bir Email Giriniz.")
            return redirect('user_profile:register_view')
        if len(password) < 7:
            messages.warning(request, "Lütfen Geçerli Bir Şifre Giriniz.")
            return redirect('user_profile:register_view')
        
        user, created = User.objects.get_or_create(username=username)
        if not created:
            user_login = authenticate(request, username=username, password=password)
            if user_login is None:
                messages.error(request, 'Girdiğiniz Email mevcut fakat Parolanız Hatalı.')
                return redirect('user_profile:login_view')
            else:
                login(request, user_login)
                messages.success(request, 'Başarıyla Giriş Yapıldı')
                return redirect('home_view')
        else:
            user.set_password(password)
            user.is_staff = False
            user.is_superuser = False
            user.save()
            profile = Profile.objects.create(user=user)
            profile.save()

            messages.success(request, 'Başarıyla Kayıt Olundu')
            return redirect('user_profile:login_view')
    
    return render(request, 'register.html', context)
