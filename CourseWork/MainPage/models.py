from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, db_column='title', db_index=True)
    text = models.TextField()
    image = models.ImageField(upload_to='static/MainPage/img', blank=True)
    pub_date = models.DateTimeField('date published')


class Page(models.Model):
    CATEGORY_CHOICES = [
        ('cat1', 'Category 1'),
        ('cat2', 'Category 2'),
        ('cat3', 'Category 3'),
        ('cat4', 'Category 4'),
        ('cat5', 'Category 5'),
        ('cat6', 'Category 6'),
        ('cat7', 'Category 7'),
        ('cat8', 'Category 8'),
        ('cat9', 'Category 9'),
    ]
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='static/MainPage/img', blank=True)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default=None, null=True)
    value = models.CharField(max_length=255, default='', blank=True)


    def __str__(self):
        return self.title

# Create your models here.
