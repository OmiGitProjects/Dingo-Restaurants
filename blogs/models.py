from datetime import datetime
from django.db import models

class BlogsDatabase(models.Model):

        id = models.AutoField(primary_key=True)
        title = models.CharField(max_length=200, null=False, blank=True)
        content = models.TextField(max_length=50000, null=False, blank=True)
        category = models.CharField(max_length=150)
        postImage = models.ImageField(null=True, blank=True, upload_to='Blogs')
        displayContent = models.CharField(max_length=450)
        slug = models.CharField(max_length=200, null=False, blank=True)
        timeStamp = models.DateTimeField(default=datetime.utcnow, null=True)

        def __str__(self):
                return self.title + ' ' + str(self.id) 