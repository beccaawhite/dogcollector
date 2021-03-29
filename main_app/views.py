from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Murphy', 'golden', 'sweet and sensitive', 10),
  Dog('Cooper', 'black lab', 'fast and furious', 6),
  Dog('Lucy', 'border collie', 'the crazy', 0)
]


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })