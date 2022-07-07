from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from slugify import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Категория", max_length=32)
    slug = models.SlugField("url", max_length=200, unique="True")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"




class Advert(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    subject = models.CharField("Тема", max_length=128)
    description = models.TextField("Объявление", max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField("url", max_length=200, unique=True)
    #reply = models.ForeignKey(Reply, verbose_name="Комментрарии", blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('advert-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.subject)
        super(Advert, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

class Reply(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    comment = models.ForeignKey(Advert, verbose_name="Объявление", on_delete=models.CASCADE, related_name='comments', null= True)
    user_reply = models.TextField("Отклик", max_length=400, null=True)
    created = models.DateTimeField("Создано", auto_now_add=True)

    def __str__(self):
        return 'комментарий {} от {}'.format(self.user_reply, self.user)

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"

    @property
    def post_title(self):
        return self.comment.subject

