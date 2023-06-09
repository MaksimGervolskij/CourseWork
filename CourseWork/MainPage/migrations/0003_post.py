# Generated by Django 3.2 on 2023-04-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0002_auto_20230423_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='CourseWork/CourseWork/MainPage/static/MainPage/img')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
