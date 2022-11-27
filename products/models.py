from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save #importamos el signal
import uuid 


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    slug = models.SlugField(null=True, blank=False, unique=True)      # poner en la creacion null=False!!!
    created_at = models.DateTimeField(auto_now_add=True)
    # generar slug automaticos 1
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    #generar Signals para el slug (callback atraves de los Singals (pres_ave))
def set_slug(sender, instance, *args, **kwargs ):
    if instance.title and not instance.slug:  #si posee un title y no posee slug
        slug = slugify(instance.title)

        while Product.objects.filter(slug=slug).exists(): #validamos que sea unico ya que si existe
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8]) # se le agrega al titulo 8 caracteres generados por uuid4
            )
        instance.slug = slug
        #instance.slug= slugify(instance.title) # es lo mismo quela linea 15
   
pre_save.connect(set_slug, sender=Product) # registramos el callback al modelo Product

    

