# Generated by Django 3.1.7 on 2021-05-04 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0010_auto_20210503_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad_student',
            name='salary',
            field=models.CharField(default=3000, max_length=10),
        ),
    ]
