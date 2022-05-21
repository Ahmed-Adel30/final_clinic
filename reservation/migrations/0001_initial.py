# Generated by Django 4.0.4 on 2022-05-21 17:13

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
            name='Doctors_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('E_mail', models.CharField(max_length=50, verbose_name='E-Mail')),
                ('phone_num', models.IntegerField(max_length=50, verbose_name='Phone Number')),
                ('Specialty', models.CharField(choices=[('Dentistry', 'Dentistry'), ('Psychiatry', 'Psychiatry'), ('Neurology ', 'Neurology '), ('Ear, Nose and Throat', 'Ear, Nose and Throat'), ('Chest and Respiratory', 'Chest and Respiratory'), ('Heart', 'Heart'), ('Brain & Nerves', 'Brain & Nerves'), ('Bones', 'Bones'), (' Male Infertility', ' Male Infertility'), ('Pediatrics and New Born', 'Pediatrics and New Born')], default='', max_length=50, verbose_name='Specialty')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
                ('who_i', models.TextField(max_length=250, verbose_name='synopsis about your self')),
                ('price', models.IntegerField(verbose_name='price')),
                ('new_join', models.DateTimeField(auto_now_add=True, verbose_name='joining_Time')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
    ]
