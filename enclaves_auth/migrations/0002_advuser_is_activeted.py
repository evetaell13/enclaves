# Generated by Django 2.1.7 on 2019-04-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enclaves_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advuser',
            name='is_activeted',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Прошел ли активацию?'),
        ),
    ]
