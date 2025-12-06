from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Skill(models.Model):
    CATEGORY_CHOICES = (
        ('Technical', 'Technical'),
        ('Soft', 'Soft'),
    )

    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)  # Beginner / Intermediate / Expert
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Technical')

    def __str__(self):
        return f"{self.name} ({self.category})"


class Certification(models.Model):
    title = models.CharField(max_length=150)
    issued_by = models.CharField(max_length=150)
    issue_date = models.DateField()
    resource_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.issued_by}"


class Achievement(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    details = models.TextField(blank=True)  # optional longer description
    image = models.ImageField(upload_to='achievements/', blank=True, null=True)
    resource_link = models.URLField(blank=True, null=True)  # NEW FIELD
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
