from django.shortcuts import render

# Create your views here.

def archivo(request):
	
	return render(request, 'index.html')

def nuestro_equipo(request):
			equipo = ['Claudio','Miguel','Sebastian', 'Valentina', 'Walter']
			request,
			context = {'lista': equipo}
			return render(request, 'miapp2/nuestro_equipo.html', context)