# Generated by Django 2.2 on 2021-06-01 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0004_auto_20210531_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='User',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
