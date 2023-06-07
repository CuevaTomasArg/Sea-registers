# Generated by Django 4.2.1 on 2023-06-07 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_alter_teacher_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commission',
            name='teacher',
        ),
        migrations.AddField(
            model_name='commission',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
