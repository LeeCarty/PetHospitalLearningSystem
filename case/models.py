from django.db import models

# Create your models here.
class Case(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=30, verbose_name='名称')
    desc = models.TextField(verbose_name='描述')
    img = models.ImageField(verbose_name='图片', upload_to='case-image/')
    belongs = models.CharField(max_length=30, verbose_name='病种')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')  # 创建日期
    modified_date = models.DateTimeField(auto_now_add=True, verbose_name='修改日期')  # 修改日期


    def details(self):
        res = {
            'name': self.name,
            'desc': self.desc,
            'img': self.img,
            'belongs': self.belongs,
        }
        return res

    class Meta:
        verbose_name = '病例'
        verbose_name_plural = '病例'
