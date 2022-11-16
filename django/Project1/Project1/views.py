from datetime import datetime
from pipes import Template
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Person(object):
    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name

def about_me(request):
    current_date = datetime.datetime.now()
    return render(request, "about.html")

def greeting(request): # first view
    themes = ["Templates", "Models", "Forms", "Views", "Application Deployment", "Hello man"]
    obj_person = Person("Cecilia", "Sierra")
    current_date = datetime.datetime.now()
    return render(request, "main.html", {"name_person":obj_person.name, "last_name":obj_person.last_name, "date":current_date, "themes":tuple(themes)})

def farewells(request):
    return HttpResponse("So long, see you later, see you soon, my first page django")

def get_date(request):
    current_date = datetime.datetime.now()
    document = f"""<html>
    <body>
    Time date: <h2> {current_date}</h2>
    </body>
    </html>
    """
    return HttpResponse(document)

def calc_edad(request, edad, agno):
    period = agno - 2019
    edadFutura = edad + period
    document = f"<h2>In the year {agno} I will be {edadFutura} years old</h2>"
    return HttpResponse(document)