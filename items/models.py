from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=255)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)#null and blank to make it optional#

    def __str__(self):
        return self.name

class FavoriteItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="favs")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

