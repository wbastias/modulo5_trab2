from django.shortcuts import render

# Create your views here.

<<<<<<< HEAD
# esta funciòn renderiza index2 que usa como base a index
def mostrar_index2(request):
    numeros_a = ['1', '2', '3', '4']
    numeros_b = ['5','6','7']
    datos = {'numeros_a': numeros_a, 'numeros_b': numeros_b}
    return render(request, 'miapp2/index2.html', context=datos)

def index(request):
    
    # ------------- Vale Code: Enlaces ----------------
    '''
    Variables:
    * linkrow, linkcol, range_4: arrays para controlar el n° de veces que
    se ejecutan ciclos for en el html:
        * linkrow: rango de filas (2 filas)
        * linkcol: rango de columnas (2 columnas por fila)
        * range_4: Para generar los textos con links  de cada columna
    * link_txt0,link_txt1,link_txt2: textos para completar los contenidos
    de las columnas.
    '''
=======
# mostrar index base en el navegador 
def mostrar_base(request):
    return render(request, 'miapp2/index_base.html')



# renderizacion del index extendido

def mostrar_extendido(request):

    # Claudio COMPETENCIAS
    numeros_a = ['1', '2', '3', '4']
    numeros_b = ['5','6','7']

    # Valentina ENLACES 
>>>>>>> f09d1cc634d116a7cbf467449a925e98761bcf03
    linkTitulo='Enlaces de Interés'
    linkrow=[1,2]
    linkcol=[1,2]
    link_range4=[1,2,3,4]
    link_txt0='  Enlaces Tipo '
    link_txt1='Enlace de interés del grupo '
    link_txt2='Ver más'
                
<<<<<<< HEAD
    
    # ------------- FIN Vale Code: Enlaces ----------------
    
    # ------------- Vale Code: Contacto ----------------
    conTitulo='Contáctanos'
    con_txtrange={'1':'Nombre','2':'Email','3':'Email'}
    con_txtbtn=['Enviar','Limpiar']
    
    # ------------- FIN Vale Code: Contacto ----------------
    
    context={'linkTitulo':linkTitulo,'linkrows':linkrow,'linkcols':linkcol,'link_range4':link_range4,'link_txt0':link_txt0,'link_txt1':link_txt1,'link_txt2':link_txt2,
    'conTitulo':conTitulo,'con_txtrange':con_txtrange, 'con_txtbtn':con_txtbtn
    }
    return render(request,'miapp2/index2.html',context)
def index(request):
    
    # ------------- Vale Code ----------------    
    equipo = ['Claudio', 'Miguel','Sebastian', 'Valentina', 'Walter']
    context = {'lista_equipo': equipo,
                'tittle': "Nuestro Equipo"}
    return render(request, 'miapp2/index.html', context)
=======
    # Valentina CONTACTO
    conTitulo='Contáctanos'
    con_txtrange={'1':'Nombre','2':'Email','3':'Email'}
    con_txtbtn=['Enviar','Limpiar']

    # Equipo
    equipo = ['Claudio', 'Miguel','Sebastian', 'Valentina', 'Walter']
    
    datos={'numeros_a': numeros_a, 'numeros_b': numeros_b,'linkTitulo':linkTitulo,'linkrows':linkrow,'linkcols':linkcol,'link_range4':link_range4,'link_txt0':link_txt0,'link_txt1':link_txt1,'link_txt2':link_txt2,
    'conTitulo':conTitulo,'con_txtrange':con_txtrange, 'con_txtbtn':con_txtbtn, 'lista_equipo': equipo,'tittle': "Nuestro Equipo"}

    return render(request, 'miapp2/index_extendido.html', context=datos)


>>>>>>> f09d1cc634d116a7cbf467449a925e98761bcf03


        
        
    
        
