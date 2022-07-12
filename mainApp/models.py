from django.db import models


class Box(models.Model):
    box_number = models.IntegerField('Box Number', unique=True)
    box_location = models.CharField('Box Location', max_length=50, blank=True)
    box_description = models.TextField(blank=True)
    box_creation_date = models.DateTimeField('Box Date', blank=True)

    def __int__(self):
        return self.box_number

class BoxItem(models.Model):
    box = models.ForeignKey(Box, blank=True, null=True, on_delete=models.CASCADE)
    item_name = models.CharField('Item Name', max_length=300)
    item_quantity = models.CharField('Item Quantity', max_length=50, default=1)
    item_creation_date = models.DateTimeField('Item Date', blank=True)

    def __str__(self):
        return self.item_name
