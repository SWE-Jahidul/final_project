# Generated by Django 3.0.3 on 2020-09-10 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_auto_20200909_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evnets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Events_images', models.ImageField(upload_to=None)),
                ('Events_title', models.CharField(default='', max_length=150)),
                ('Events_time', models.DateTimeField(auto_now_add=True)),
                ('Ecent_location', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
