# Generated by Django 4.0.5 on 2022-06-20 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=200, unique='True', verbose_name='url')),
            ],
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=128, verbose_name='Тема')),
                ('description', models.TextField(max_length=1000, verbose_name='Объявление')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='url')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advert.category', verbose_name='Категория')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
