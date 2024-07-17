from django.shortcuts import render
from apps.contact.models import Translate
# Create your views here.

def contact(request):
    contact = Translate.objects.all()
    return render(request, 'base/contact.html', locals())



