from django.db import models

# Create Blog models
# title
# pub_date
# body
# image

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

# Add the Blog app to the settings

# Create a migration

# Migrate

# Add to the admin