from django.db import models

# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    image=models.ImageField(upload_to='note_images/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_archived=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title