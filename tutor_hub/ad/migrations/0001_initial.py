# Generated by Django 3.1.7 on 2021-04-11 09:45

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
            name='Ad_Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('expected_area', models.CharField(blank=True, max_length=150, null=True)),
                ('subject', models.CharField(blank=True, max_length=150, null=True)),
                ('class_level', models.CharField(blank=True, max_length=150, null=True)),
                ('days', models.DecimalField(decimal_places=0, max_digits=7)),
                ('extecpted_salary', models.DecimalField(decimal_places=1000, max_digits=50000)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='male', max_length=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('request_confirmation', models.BooleanField(default=False)),
                ('ad_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ad_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('area', models.CharField(blank=True, max_length=150, null=True)),
                ('subject', models.CharField(blank=True, max_length=150, null=True)),
                ('class_level', models.CharField(blank=True, max_length=150, null=True)),
                ('days', models.DecimalField(decimal_places=0, max_digits=7)),
                ('salary', models.DecimalField(decimal_places=1000, max_digits=50000)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='male', max_length=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('request_confirmation', models.BooleanField(default=False)),
                ('ad_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]