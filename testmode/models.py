# coding: utf-8
from django.db import models
from phls.accounts.models import Accounts

# Create your models here.


class DiseaseType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, blank=True)
    descriptions = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name


class DiseaseSmallType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, blank=True)
    descriptions = models.TextField(blank=True, null=False)
    disease_type_id = models.ForeignKey(DiseaseType)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TestPaper(models.Model):
    name = models.CharField(max_length=100, null=False)
    disease_type_id = models.ForeignKey(DiseaseType)
    disease_small_type_id = models.ForeignKey(DiseaseSmallType)
    tags = models.ManyToManyField(Tag, blank=True)
    test_time = models.CharField(default='30分钟')

    def __str__(self):
        return self.name


class PaperQuestions(models.Model):
    name = models.CharField(max_length=100, null=True)
    content = models.TextField(null=False)
    paper_id = models.ForeignKey(TestPaper)
    answer_A = models.CharField(max_length=100, null=False)
    answer_B = models.CharField(max_length=100, null=False)
    answer_C = models.CharField(max_length=100, null=False)
    answer_D = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class UserTestRecords(models.Model):
    user_id = models.ManyToManyField(Accounts)
    paper_id = models.ForeignKey(TestPaper)
    finish_time = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(default=0)
    tips = models.CharField(max_length=100, null=False)
