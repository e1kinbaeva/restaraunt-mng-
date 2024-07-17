from django.shortcuts import render,redirect,get_object_or_404
from apps.base.models import Base, Popular_category,Our_chef,News,Our_advantages,Specialmenu_foods,Specialmenu_deserts,Specialmenu_seafood,Specialmenu_beverage
from apps.telegram.models import Telegram
from apps.telegram.views import get_text
from apps.telegram.forms import PERSONE_CHOISE, TIME_CHOISE
# Create your views here.
def index(request):
    base = Base.objects.latest('id')
    category = Popular_category.objects.all()
    chef = Our_chef.objects.all().order_by('?')[:3]
    news = News.objects.all().order_by('?')[:2]
    advantages = Our_advantages.objects.all()
    special_menu = Specialmenu_foods.objects.all()
    desert = Specialmenu_deserts.objects.all()
    seafood = Specialmenu_seafood.objects.all()
    beverage = Specialmenu_beverage.objects.all()

    if request.method == "POST":
        phone = request.POST.get('phone')
        persone = request.POST.get("persone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        Telegram.objects.create(phone=phone, persone=persone, date=date, time=time)
        get_text(f"""Оставлена заявка 💬:
                 
Номер телефона: {phone}

Количество людей: {persone}

Дата: {date}

Время: {time}
""")
        return redirect('index')

    return render(request, 'base/index-dark.html', {
        'base': base,
        'category': category,
        'chef': chef,
        'news': news,
        'PERSONE_CHOISE': PERSONE_CHOISE,
        'TIME_CHOISE': TIME_CHOISE,
        'advantages': advantages,
        'menu': special_menu,
        'deserts': desert,
        'seafood': seafood,
        'beverage': beverage,
    })

def chef_detail(request, id):
    base = Base.objects.latest('id')
    chef = Our_chef.objects.get(id=id)
    return render(request, 'base/chef-details-dark.html', locals())


def errors(request,exeption):
    return render(request, '404/404.html', status=404)












def shop_detail(request, id):
    base = Base.objects.latest('id')
    special_menu = Specialmenu_foods.objects.get(id=id)
    
    return render(request, 'base/shop_detail.html', locals())

def shop_detail(request, id):
    base = Base.objects.latest('id')
    desert = Specialmenu_deserts.objects.get(id=id)
    
    return render(request, 'base/shop_detail.html', locals())


def shop_detail(request, id):
    base = Base.objects.latest('id')
    seafood = Specialmenu_seafood.objects.get(id=id)
    
    return render(request, 'base/shop_detail.html', locals())


def shop_detail(request, id):
    base = Base.objects.latest('id')
    beverage = Specialmenu_beverage.objects.get(id=id)
    
    return render(request, 'base/shop_detail.html', locals())