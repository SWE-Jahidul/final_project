# Generated by Django 3.0.3 on 2020-09-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('heading', models.CharField(max_length=150)),
                ('Notice_decription', models.TextField(max_length=3072)),
                ('notice_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
