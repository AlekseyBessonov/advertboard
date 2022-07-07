from django import forms
from django_filters import FilterSet, DateFilter
from .models import Advert, Reply


# создаём фильтр
class AdvertFilter(FilterSet):
     #createTime = DateFilter(lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Advert
        #fields = ['subject', 'category', 'user']
        fields = {
            'subject': ['icontains'],
            'category': ['exact'],
            'user': ['exact'],

        }


class ReplyFilter(FilterSet):
    # createTime = DateFilter(lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Reply

        fields = {
            'user_reply': ['icontains'],
            'user': ['exact'],

        }


