from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    main_text = models.TextField()
    published_time = models.DateField()
    is_active = models.BooleanField(default=True)
    created_time =models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title