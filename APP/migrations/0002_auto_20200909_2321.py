# Generated by Django 3.0.3 on 2020-09-09 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number_title', models.CharField(default='', max_length=150)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mayor_and_councilor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mayor_or_councilor_name', models.CharField(default='', max_length=150)),
                ('deginaion', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=150)),
                ('about', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(default='', max_length=150)),
                ('news_details', models.CharField(default='', max_length=3072)),
                ('news_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='notice',
            name='Notice_decription',
            field=models.TextField(default='', max_length=3072),
        ),
        migrations.AlterField(
            model_name='notice',
            name='heading',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]