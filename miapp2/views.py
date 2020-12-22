from django.shortcuts import render

# Create your views here.

def archivo(request):
	
	return render(request, 'index.html')