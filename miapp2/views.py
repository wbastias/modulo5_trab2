from django.shortcuts import render

# Create your views here.

def index(request):
    
    # ------------- Vale Code ----------------    
    equipo = ['Claudio', 'Miguel','Sebastian', 'Valentina', 'Walter']
    context = {'lista_equipo': equipo,
                'tittle': "Nuestro Equipo"}
    return render(request, 'miapp2/index.html', context)


        
        
    
        