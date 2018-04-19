# coding: utf-8
from django.db import models
import random

# Create your models here.


class Accounts(models.Model):
	name = models.CharField(max_length=30, verbose_name='用户名')
	password = models.CharField(max_length=20, verbose_name='密码')
	email = models.EmailField(max_length=100, primary_key=True, verbose_name='邮箱')
	role = models.BooleanField(default=False, verbose_name='是否为管理员') # yes--manage role
	create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期') # 创建日期
	modified_date = models.DateTimeField(auto_now_add=True, verbose_name='修改日期') # 修改日期
	confirm_code = models.CharField(blank=True, max_length=6, verbose_name='验证码')
	is_active = models.BooleanField(default=False, verbose_name='是否有效')

	class Meta:
		verbose_name = '用户账号'
		verbose_name_plural = '用户账户'

	def __str__(self):
		return self.name

	def set_confirm_code(self):
		confirm_code = ''
		code_list = []
		for i in range(6):
			statu = random.randint(1, 3)
			if statu == 1:
				a = random.randint(65, 90)
				random_uppercase = chr(a)
				code_list.append(random_uppercase)
			elif statu == 2:
				b = random.randint(97, 122)
				random_lowercase = chr(b)
				code_list.append(random_lowercase)
			elif statu == 3:
				random_num = random.randint(0, 9)
				code_list.append(str(random_num))

		confirm_code = "".join(code_list)
		self.confirm_code = confirm_code.lower()
		self.save()
		return self.confirm_code

