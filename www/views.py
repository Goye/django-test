from django.shortcuts import render

# Create your views here.
def index(request):
  context = {'name':'Prodigious', 'number': 2}
  return render(request, 'www/index.html',  context)