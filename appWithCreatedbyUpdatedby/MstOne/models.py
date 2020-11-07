from django.db import models


# Master table 1(MstOneModel)
class MstOneModel(models.Model):
    category_name = models.CharField(max_length=30)
    category_name_abbreviation = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<' + str(self.id) + '> ' + self.category_name + '/' + self.category_name_abbreviation
