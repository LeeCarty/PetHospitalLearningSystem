# coding: utf-8
from django.db import models

# Create your models here.


class Accounts(models.Model):
	name = models.CharField(max_length=30)
	password = models.CharField(max_length=20)
	email = models.EmailField(max_length=100)
	role = models.BooleanField(default=False)
	create_date = models.DateTimeField(auto_now_add=True) # 创建日期
	modified_date = models.DateTimeField(auto_now_add=True) # 修改日期

	def __str__(self):
		return self.name
