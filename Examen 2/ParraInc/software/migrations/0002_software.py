# Generated by Django 2.1 on 2018-11-01 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSoftware', models.CharField(max_length=200)),
                ('funcion', models.CharField(max_length=200)),
                ('departamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='software.Departamento')),
            ],
        ),
    ]
