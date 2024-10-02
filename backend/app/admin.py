from django.contrib import admin
from .improve_models import CustomUser, Image, AnalysisResult, ImprovementSuggestion
from django.contrib.auth.admin import UserAdmin 

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Image)
admin.site.register(AnalysisResult)
admin.site.register(ImprovementSuggestion)