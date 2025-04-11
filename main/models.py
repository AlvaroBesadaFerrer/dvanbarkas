from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class About(models.Model):
    about_text = models.CharField(max_length=700)
    created_at = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = "about"
    

class What_I_do(models.Model):
    topic_1 = models.CharField(max_length=20)
    about_text_1 = models.CharField(max_length=230)
    
    topic_2 = models.CharField(max_length=20)
    about_text_2 = models.CharField(max_length=230)

    topic_3 = models.CharField(max_length=20)
    about_text_3 = models.CharField(max_length=230)

    class Meta:
        verbose_name_plural = "What I do"


class Characteristic(models.Model):
    characteristic_title_1 = models.CharField(max_length=40, default="Many musical genres...")
    characteristic_text_1 = models.CharField(max_length=400)
    photo_1 = models.ImageField(default=None, upload_to="polls_media")

    characteristic_title_2 = models.CharField(max_length=40, default="Deep lyrics")
    characteristic_text_2 = models.CharField(max_length=400)
    photo_2 = models.ImageField(default=None, upload_to="polls_media")

    characteristic_title_3 = models.CharField(max_length=40, default="Unique style, unique feeling")
    characteristic_text_3 = models.CharField(max_length=400)
    photo_3 = models.ImageField(default=None, upload_to="polls_media")



class News(models.Model):
    news_title_1 = models.CharField(max_length=30, default="New Music Alert!")
    news_text_1 = models.CharField(max_length=100)
    photo_1 = models.ImageField(default=None, upload_to="polls_media")

    news_title_2 = models.CharField(max_length=30, default="Don't Miss Out!")
    news_text_2 = models.CharField(max_length=100)
    photo_2 = models.ImageField(default=None, upload_to="polls_media")
    
    news_title_3 = models.CharField(max_length=30, default="Behind the Scenes")
    news_text_3 = models.CharField(max_length=100)
    photo_3 = models.ImageField(default=None, upload_to="polls_media")
    
    news_title_4 = models.CharField(max_length=30, default="Fan Art Friday")
    news_text_4 = models.CharField(max_length=100)
    photo_4 = models.ImageField(default=None, upload_to="polls_media")
    
    news_title_5 = models.CharField(max_length=30, default="Vanbarkas in the News")
    news_text_5 = models.CharField(max_length=100)
    photo_5 = models.ImageField(default=None, upload_to="polls_media")
    
    news_title_6 = models.CharField(max_length=30, default="Happy Birthday")
    news_text_6 = models.CharField(max_length=100)
    photo_6 = models.ImageField(default=None, upload_to="polls_media")

    class Meta:
        verbose_name_plural = "News"


class Opinion(models.Model):
    main_photo = models.ImageField(default=None, upload_to="polls_media")
    opinions_fan_info_1 = models.CharField(max_length=50, default="Pete Rock, from Croatia")
    opinions_text_1 = models.CharField(max_length=500)

    opinions_fan_info_2 = models.CharField(max_length=50, default="Michael Snowden, from Ecuador")
    opinions_text_2 = models.CharField(max_length=500)
    
    opinions_fan_info_3 = models.CharField(max_length=50, default="Tom Davis, from Nigeria")
    opinions_text_3 = models.CharField(max_length=500)

class Contact(models.Model):
    address = models.CharField(max_length=65, default="Grand-Manil, Namur, Belgium")
    phone_number = models.CharField(max_length=25, default="+44 7849 905419")
    email = models.EmailField(max_length=256, default="cconteconte23@gmail.com")
    class Meta:
        verbose_name_plural = "Contact"


class Social_Media(models.Model):
    facebook = models.CharField(max_length=200, default="https://www.facebook.com/djuphi.vanbarkas")
    instagram = models.CharField(max_length=200, default="")
    linkedin = models.CharField(max_length=200, default="")
    youtube = models.CharField(max_length=200, default="https://www.youtube.com/@carlosconte7741")
    whatsapp = models.CharField(max_length=200, default="https://wa.me/+447849905419")
    youtube_video = models.CharField(max_length=1000, default='<iframe width="1" height="1" src="https://www.youtube.com/embed/oU3KWPxQzOA" title="KAl Ki I DI Bô" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>')

    class Meta:
        verbose_name_plural = "Social Media"
