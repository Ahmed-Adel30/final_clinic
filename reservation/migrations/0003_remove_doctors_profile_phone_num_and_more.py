# Generated by Django 4.0.4 on 2022-05-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_doctors_profile_options_doctors_profile_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors_profile',
            name='phone_num',
        ),
        migrations.AddField(
            model_name='doctors_profile',
            name='phone_number',
            field=models.CharField(default='', max_length=12, verbose_name='Phone'),
        ),
    ]