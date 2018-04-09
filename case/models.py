from django.db import models

# Create your models here.
class Case(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    desc = models.TextField()
    img = models.ImageField()
    belongs = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True)  # 创建日期
    modified_date = models.DateTimeField(auto_now_add=True)  # 修改日期


    def details(self):
        res = {
            'name': self.name,
            'desc': self.desc,
            'img': self.img,
            'belongs': self.belongs,
        }
        return res


