from django.contrib import admin
from .models import LearningStep, AboutMe

@admin.register(LearningStep)
class LearningStepAdmin(admin.ModelAdmin):
    list_display = ('step_no', 'title', 'description', 'date')  # use real field


    def get_step_no(self, obj):
        return obj.id
    get_step_no.short_description = 'Step No'


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
