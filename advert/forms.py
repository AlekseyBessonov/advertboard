from django.forms import ModelForm
from .models import Advert, Reply


class AdvertForm(ModelForm):
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Advert
        fields = ['category', 'subject', 'description']


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['user_reply']
