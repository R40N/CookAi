# Generated by Django 4.2.1 on 2023-05-28 07:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='이메일')),
                ('username', models.CharField(max_length=20, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_img')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('followings', models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='팔로워')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
