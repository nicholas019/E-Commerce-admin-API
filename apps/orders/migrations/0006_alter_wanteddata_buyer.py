# Generated by Django 4.1 on 2022-09-12 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0005_rename_city_name_deliveryinfo_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wanteddata',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
