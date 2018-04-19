# coding: utf-8
from django.db import models
# from accounts.models import Accounts

# Create your models here.


class DiseaseType(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    code = models.CharField(max_length=20, blank=True, verbose_name='标识码')
    descriptions = models.TextField(blank=True, null=False, verbose_name='描述')
    # image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '病种'
        verbose_name_plural = '病种'


class DiseaseSmallType(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    code = models.CharField(max_length=20, blank=True, verbose_name='标识码')
    descriptions = models.TextField(blank=True, null=False, verbose_name='描述')
    disease_type_id = models.ForeignKey(DiseaseType, verbose_name='病种')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '疾病'
        verbose_name_plural = '疾病'


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class TestPaper(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='试卷名')
    disease_type_id = models.ForeignKey(DiseaseType, verbose_name='病种')
    disease_small_type_id = models.ForeignKey(DiseaseSmallType, verbose_name='疾病名称')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    test_time = models.CharField(max_length=20, default='30分钟', verbose_name='测试时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '测试试卷'
        verbose_name_plural = '测试试卷'


class PaperQuestions(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='名称')
    content = models.TextField(null=False, verbose_name='内容')
    paper_id = models.ForeignKey(TestPaper, verbose_name='试卷名')
    answer_A = models.CharField(max_length=100, null=False, verbose_name='答案A')
    answer_B = models.CharField(max_length=100, null=False, verbose_name='答案B')
    answer_C = models.CharField(max_length=100, null=False, verbose_name='答案C')
    answer_D = models.CharField(max_length=100, null=True, verbose_name='答案D')
    answer = models.CharField(max_length=10, null=False, verbose_name='答案')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '测试题目'
        verbose_name_plural = '测试题目'


class UserTestRecords(models.Model):
    user_id = models.ForeignKey('accounts.Accounts', verbose_name='用户名')
    paper_id = models.ForeignKey(TestPaper, verbose_name='试卷名')
    finish_time = models.DateTimeField(auto_now_add=True, verbose_name='完成时间')
    grade = models.IntegerField(default=0, verbose_name='成绩')
    tips = models.CharField(max_length=100, null=False, verbose_name='评价')

    class Meta:
        verbose_name = '用户测试记录'
        verbose_name_plural = '用户测试记录'
