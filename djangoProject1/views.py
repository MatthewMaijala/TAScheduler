from django.shortcuts import render
from django.views import View


class LoginPage(View):
    def get(self, request):
        return render(request, "login.html", {})

class HomePage(View):
    def get(self, request):
        return render(request, "hello.html", {})