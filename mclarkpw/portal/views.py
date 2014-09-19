from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def TokenAuth(request, token):
    user = authenticate(token=token)
    if user is not None:
        login(request,user)
    return redirect('/')
    
