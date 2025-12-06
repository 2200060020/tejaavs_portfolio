from django.shortcuts import render
from .models import Project, ContactMessage, Skill, Achievement, Certification


def home(request):
    technical_skills = Skill.objects.filter(category='Technical')
    soft_skills = Skill.objects.filter(category='Soft')
    achievements = Achievement.objects.all()
    certifications = Certification.objects.all()

    return render(request, 'portfolio/home.html', {
        'technical_skills': technical_skills,
        'soft_skills': soft_skills,
        'achievements': achievements,
        'certifications': certifications,
    })


def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def contact(request):
    success = False
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        success = True

    return render(request, 'portfolio/contact.html', {'success': success})
