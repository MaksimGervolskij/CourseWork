# Generated by Django 3.2 on 2023-04-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='CourseWork/CourseWork/MainPage/static/MainPage/img')),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
