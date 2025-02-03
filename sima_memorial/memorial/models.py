from django.db import models

# Create your models here.
class SimaPost(models.Model):
    title = models.CharField(max_length=300, blank=False)
    main_picture = models.ImageField(upload_to="uploads/%Y/%m/%d")
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title