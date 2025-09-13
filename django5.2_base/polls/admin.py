from django.contrib import admin
from polls import models
# Register your models here.

class ChoiceAdmin(admin.TabularInline):
    model = models.Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date information',{'fields':['pub_date']})
    ]

    list_display = ['question_text','pub_date','was_published_recently']
    list_filter = ["pub_date"]
    inlines = [ChoiceAdmin]
    search_fields = ["question_text"]

admin.site.register(models.Question,QuestionAdmin)