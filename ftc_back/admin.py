from django.contrib import admin
from django.contrib import admin
from ftc_back.models import *
from django.contrib.auth.models import User


class QuestionAdmin(admin.ModelAdmin):
	pass
admin.site.register(Question,QuestionAdmin)
class TeamsAdmin(admin.ModelAdmin):
	pass
admin.site.register(Teams,TeamsAdmin)
class questions_attemptAdmin(admin.ModelAdmin):
	pass
admin.site.register(questions_attempt,questions_attemptAdmin)