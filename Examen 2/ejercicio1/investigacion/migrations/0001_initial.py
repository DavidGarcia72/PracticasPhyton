# Generated by Django 2.1 on 2018-10-29 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investigacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250, null=True)),
                ('autor', models.CharField(max_length=250, null=True)),
                ('content', models.CharField(max_length=250, null=True)),
                ('categoria', models.CharField(choices=[('CiCom', 'Ciencias Computacionales'), ('CiTi', 'Ciencias de la Tierra'), ('CiNa', 'Ciencias Naturales'), ('CiSo', 'Ciencias Sociales'), ('CiMe', 'Ciencias Medicas')], default='CiCom', max_length=50)),
            ],
        ),
    ]
