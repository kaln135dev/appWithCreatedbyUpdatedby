from django.db import models
from django.contrib.auth.models import User
from MstOne.models import MstOneModel
from MstTwo.models import MstTwoModel


class mainModel(models.Model):
    main_name = models.CharField(max_length=10)
    category = models.ForeignKey(MstOneModel, on_delete=models.CASCADE)
    item_one = models.ForeignKey(MstTwoModel, on_delete=models.CASCADE, related_name='item_one')
    item_two = models.ForeignKey(MstTwoModel, on_delete=models.CASCADE, related_name='item_two')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_by')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='updated_by')

    def __str__(self):
        return '<' + str(self.id) + '> ' + self.main_name
