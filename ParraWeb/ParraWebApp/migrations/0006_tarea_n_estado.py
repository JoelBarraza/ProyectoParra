# Generated by Django 3.0.7 on 2020-06-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParraWebApp', '0005_auto_20200628_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea_n',
            name='estado',
            field=models.BooleanField(default=0),
        ),
    ]
