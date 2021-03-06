# Generated by Django 4.0.3 on 2022-05-24 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0005_doc_time_doctors_profile_doctime'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc_time',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='doctors_profile',
            name='DocTime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.doc_time', verbose_name='Appointments '),
        ),
    ]
