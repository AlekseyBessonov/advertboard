from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import mail_managers, send_mail
from .models import Advert, Reply
from accounts.models import Profile


@receiver(post_save, sender=Advert)
def notify_post_create(sender, instance, **kwargs):

    subject = f'{instance.subject}'
    message = f'{instance.description} '

    userlist = []
    for usr in Advert.objects.all():
        subscribers = usr.user.email
        print(11, subscribers)
        userlist.append(subscribers)

    send_mail(subject, message, 'hellraver81@yandex.ru', userlist)

    post_save.connect(notify_post_create, sender=Advert)