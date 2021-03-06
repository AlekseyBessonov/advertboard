# Generated by Django 4.0.5 on 2022-06-30 08:18

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=120, null=True, verbose_name='имя')),
                ('last_name', models.CharField(blank=True, max_length=240, null=True, verbose_name='фамилия')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/%Y/%m/%d', verbose_name='аватар')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'профиль',
                'verbose_name_plural': 'профили',
            },
        ),
    ]
