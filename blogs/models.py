from django.db import models
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """Model for blog post for webapp."""
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return f"{self.text[:150]}..."
        