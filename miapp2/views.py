from django.shortcuts import render

# Create your views here.

# mostrar index base en el navegador 
def mostrar_base(request):
    return render(request, 'miapp2/index_base.html')



# renderizacion del index extendido

def mostrar_extendido(request):

    # Claudio COMPETENCIAS
    numeros_a = ['1', '2', '3', '4']
    numeros_b = ['5','6','7']

    # Valentina ENLACES 
    linkTitulo='Enlaces de Interés'
    linkrow=[1,2]
    linkcol=[1,2]
    link_range4=[1,2,3,4]
    link_txt0='  Enlaces Tipo '
    link_txt1='Enlace de interés del grupo '
    link_txt2='Ver más'
                
    # Valentina CONTACTO
    conTitulo='Contáctanos'
    con_txtrange={'1':'Nombre','2':'Email','3':'Email'}
    con_txtbtn=['Enviar','Limpiar']

    # Equipo
    equipo = ['Claudio', 'Miguel','Sebastian', 'Valentina', 'Walter']
    
    datos={'numeros_a': numeros_a, 'numeros_b': numeros_b,'linkTitulo':linkTitulo,'linkrows':linkrow,'linkcols':linkcol,'link_range4':link_range4,'link_txt0':link_txt0,'link_txt1':link_txt1,'link_txt2':link_txt2,
    'conTitulo':conTitulo,'con_txtrange':con_txtrange, 'con_txtbtn':con_txtbtn, 'lista_equipo': equipo,'tittle': "Nuestro Equipo"}

    return render(request, 'miapp2/index_extendido.html', context=datos)




        
        
    
        
