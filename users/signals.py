from django.db.models import signals
from django.contrib.auth.models import User
from django.dispatch import receiver
from blog.models import Profile

@receiver(signals.post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(signals.post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()




''' qisqacha qnaday ishashi
        Bissmilahi Rohmani Rohim
tak bu yerda reciver() bu sigan qabul qiluvchi qachonki biz sign up bosganimzda baza signal boradi
 kein regisr otgandan kein  signals.post_save() blan uni saqlab qoish kerak, va sender = User orqali
 foylanuvchiga sigal jonatadi
'''