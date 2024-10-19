# Generated by Django 4.2.16 on 2024-10-16 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regalos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regalo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='regalos/')),
                ('enlace1', models.URLField(blank=True)),
                ('enlace2', models.URLField(blank=True)),
                ('enlace3', models.URLField(blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('participante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regalos.participante')),
            ],
        ),
    ]
