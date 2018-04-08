from django.contrib import admin
from .models import TestPaper, DiseaseType, DiseaseSmallType, UserTestRecords, PaperQuestions, Tag

# Register your models here.
admin.site.register(Tag)
admin.site.register(DiseaseType)
admin.site.register(TestPaper)
admin.site.register(DiseaseSmallType)
admin.site.register(UserTestRecords)
admin.site.register(PaperQuestions)
