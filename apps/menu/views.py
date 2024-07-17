from django.shortcuts import render
from apps.base.models import  Base



def menu(request):
    base = Base.objects.latest('id')
    return render(request, 'menu.html', locals())
