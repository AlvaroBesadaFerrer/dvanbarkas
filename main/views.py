from django.shortcuts import render
from .models import About, What_I_do, Characteristic, News, Opinion, Contact, Social_Media


def index(request):
    
    about_info = About.objects.all()
    wido1 = What_I_do.objects.all()
    charac = Characteristic.objects.all()
    news_info = News.objects.all()
    opinions = Opinion.objects.all()
    contact = Contact.objects.all()
    social_media = Social_Media.objects.all()

    dict_photos = {
    "charac_photo_1":charac[0].photo_1.url,
    "charac_photo_2":charac[0].photo_2.url,
    "charac_photo_3":charac[0].photo_3.url,

    "news_info_photo_1":news_info[0].photo_1.url,
    "news_info_photo_2":news_info[0].photo_2.url,
    "news_info_photo_3":news_info[0].photo_3.url,
    "news_info_photo_4":news_info[0].photo_4.url,
    "news_info_photo_5":news_info[0].photo_5.url,
    "news_info_photo_6":news_info[0].photo_6.url,

    "opinions_photo_1":opinions[0].main_photo.url,

    }
    
    context = {
        "about_info": about_info[0].about_text,
        "wido1": wido1[0],
        "wido2": wido1[0],
        "wido3": wido1[0],
        "charac": charac[0],
        "dict_photos": dict_photos,
        "news": news_info[0],
        "opinions": opinions[0],
        "contact": contact[0],
        "emailto": "mailto:" + contact[0].email,
        "social_media": social_media[0],
    }
    return render(request, "polls/index.html", context)
    