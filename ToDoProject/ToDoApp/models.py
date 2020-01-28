from django.db import models


# Create your models here.
class ToDo(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='Title')
    description = models.CharField(max_length=500, verbose_name='Description')
    state = models.BooleanField(default=False, verbose_name='State')
    created_date = models.DateTimeField(verbose_name='Created')

    def __str__(self):
        return self.title

