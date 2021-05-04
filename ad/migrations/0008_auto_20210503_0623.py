# Generated by Django 3.1.7 on 2021-05-03 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0007_auto_20210502_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad_student',
            name='days',
            field=models.DecimalField(decimal_places=0, default=3, max_digits=2),
        ),
        migrations.AlterField(
            model_name='ad_student',
            name='salary',
            field=models.DecimalField(decimal_places=0, default=3000, max_digits=10),
        ),
        migrations.AlterField(
            model_name='ad_tutor',
            name='days',
            field=models.DecimalField(decimal_places=0, default=3, max_digits=7),
        ),
        migrations.AlterField(
            model_name='ad_tutor',
            name='expected_salary',
            field=models.DecimalField(decimal_places=0, default=3000, max_digits=10),
        ),
    ]
