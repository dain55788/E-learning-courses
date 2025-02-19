from django.contrib import admin
from courses.models import Category, Course, Lesson, Tag
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'

# Override admin settings
class MyLessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'active', 'created_date', 'course_id']
    search_fields = ['subject', 'id']
    list_filter = ['id', 'created_date', 'subject']
    readonly_fields = ['image_view']
    form = LessonForm

    def image_view(self, lesson):
        if lesson:
            return mark_safe(f"<img src='/static/{lesson.image.name}' width='120' />")

# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, MyLessonAdmin)
admin.site.register(Tag)
