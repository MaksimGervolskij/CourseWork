# Generated by Django 3.2 on 2023-05-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0006_auto_20230501_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.CharField(blank=True, choices=[('cat1', 'Category 1'), ('cat2', 'Category 2'), ('cat3', 'Category 3'), ('cat4', 'Category 4'), ('cat5', 'Category 5'), ('cat6', 'Category 6'), ('cat7', 'Category 7'), ('cat8', 'Category 8'), ('cat9', 'Category 9')], max_length=4),
        ),
    ]
