from django.db import models


class MainAbout(models.Model):
    """
    this model stores a single instance
    of "about our community" text intended
    to populate the corresponding area on 
    the homepage
    """    
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)