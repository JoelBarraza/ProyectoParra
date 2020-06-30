# Generated by Django 3.0.7 on 2020-06-27 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tarea_n',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('contenido', models.CharField(max_length=300)),
                ('imagen', models.ImageField(upload_to='')),
                ('empezado', models.DateTimeField(auto_now_add=True)),
                ('terminado', models.DateTimeField()),
            ],
        ),
    ]
