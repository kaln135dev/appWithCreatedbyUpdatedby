from django.db import models


# Master table 2(MstTwoModel)
class MstTwoModel(models.Model):
    item_name = models.CharField(max_length=50)
    item_name_abbreviation = models.CharField(max_length=10)
    item_Boolean = models.BooleanField()
    item_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<' + str(self.id) + '> ' + self.item_name_abbreviation
