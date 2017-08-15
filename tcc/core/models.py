from django.contrib.auth.models import AbstractUser, Group, User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Authors(AbstractUser):
    biography = models.TextField("Biografia", max_length=1000)



@receiver(post_save, sender=Authors)
def user_post_save(sender, instance, created, **kwargs):
    """ This method is executed whenever an user object is saved
    """
    if created:
        instance.groups.add(Group.objects.get(name='publishers'))



class Hashtags(models.Model):
    text = models.TextField("Hashtags", max_length=15)

    def __str__(self):
        return self.text


class Articles(models.Model):
    title = models.TextField("Titulo", max_length=50)
    text = RichTextField(config_name='full', verbose_name=u'Texto')
    published_data = models.DateField("Data publicação", auto_now=True)
    author = models
    hashtags = models.ManyToManyField(Hashtags)


