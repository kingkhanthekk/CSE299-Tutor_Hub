# Generated by Django 3.1.7 on 2021-05-04 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0011_auto_20210504_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad_tutor',
            name='expected_salary',
            field=models.CharField(default=3000, max_length=10),
        ),
    ]
