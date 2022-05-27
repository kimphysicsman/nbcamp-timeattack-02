from django.shortcuts import render
from .models import UserModel
from django.http import HttpResponse



def sign_up_view(request):
    if request.method == 'POST':
        print(request.POST.get('email', None))

    return HttpResponse('회원가입 성공!')