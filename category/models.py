from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to="photos/categories", blank=True)

    class Meta:       
        verbose_name = "category"    #Hacemos esto para modificar el nombre que aparece en el website cuando entramos como administrador
        verbose_name_plural = "categories"


    def get_url(self):
        return reverse("products_by_category", args = [self.slug])
        #"products_by_category" fue definido en el urlpatterns del script urls.py (ver folder store)
    
    def __str__(self):
        return self.category_name

        