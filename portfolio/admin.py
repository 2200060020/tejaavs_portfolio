from django.contrib import admin
from .models import Project, ContactMessage, Skill, Achievement, Certification

# Register your models
admin.site.register(Project)
admin.site.register(ContactMessage)
admin.site.register(Skill)
admin.site.register(Achievement)
admin.site.register(Certification)

# 🔹 CHANGE ADMIN TEXTS HERE
admin.site.site_header = "Administration"
admin.site.site_title = "Administration"
admin.site.index_title = "Welcome to Teja's Admin Panel"
