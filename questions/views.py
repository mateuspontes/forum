from django.shortcuts import render, get_object_or_404

from questions.models import Question

def index(request):
  questions = Question.objects.all()
  return render(request, 'questions/index.html', {'questions' : questions})

def create(request):
  return render(request, 'questions/create.html')