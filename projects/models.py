from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    source = models.URLField()

    def __str__(self):
        return self.title
