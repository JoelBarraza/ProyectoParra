# Generated by Django 3.0.7 on 2020-06-28 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParraWebApp', '0002_auto_20200627_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea_n',
            name='terminado',
        ),
        migrations.AddField(
            model_name='tarea_n',
            name='fechalimite',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha limite'),
        ),
        migrations.AlterField(
            model_name='tarea_n',
            name='empezado',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de inicio'),
        ),
    ]