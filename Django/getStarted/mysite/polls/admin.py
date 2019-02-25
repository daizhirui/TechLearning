from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# StackedInline ocupied much space! use TabularInline to save space.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # set what to display in the list: can be attributes and methods
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # add a list filter by the pub_date field
    list_filter = ['pub_date']
    # add a search field
    search_fields = ['question_text']
    #fields = ['pub_date', 'question_text']
    # a fieldset: ( <title>, <field-set-dict> )
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date Information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # inline Choice to Question, choices will be shown in the admin page of a question
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

# add admin page of Choice directly
# admin.site.register(Choice)


