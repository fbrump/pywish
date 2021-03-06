import uuid
from django.db import models

class WishList(models.Model):
    """
    Class that mapping Wish List model.\n
    args:\n
        Wish List ID - UUID*\n
        name - string*\n
        description - string\n
        active - boolean*\n
        created on - date time*\n
        created by - string*\n
        updated on - date time\n
        updated by - string\n
    """
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(max_length=250, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_on = models.DateField(auto_now=False, auto_now_add=True)
    created_by = models.CharField(max_length=250)
    updated_on = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    updated_by = models.CharField(max_length=250, blank=True, null=True, default='')

    def __str__(self):
        return '{}'.format(self.name)

    def __unicode__(self):
        return '{}'.format(self.name)

