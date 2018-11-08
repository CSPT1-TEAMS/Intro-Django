from django.db import models
from uuid import uuid4

# Create your models here.
class Note ( models.Model ):
    id = models.UUIDField ( primary_key = True, default = uuid4, editable = False, blank = True )
    title = models.CharField( max_length = 30 )
    body = models.TextField( blank = True, max_length = 500)
    # author = models.CharField( max_length = 30, blank = True)
    # date = models.DateTimeField( auto_now=False, auto_now_add=False, blank = True)
    # completed = models.BooleanField( default = False, blank = True )
