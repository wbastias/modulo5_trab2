from django.shortcuts import render

# Create your views here.

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
    linkTitulo='Enlaces de Interés'
    linkrow=[1,2]
    linkcol=[1,2]
    link_range4=[1,2,3,4]
    link_txt0='  Enlaces Tipo '
    link_txt1='Enlace de interés del grupo '
    link_txt2='Ver más'
                
    
    # ------------- FIN Vale Code: Enlaces ----------------
    
    # ------------- Vale Code: Contacto ----------------
    conTitulo='Contáctanos'
    con_txtrange={'1':'Nombre','2':'Email','3':'Email'}
    con_txtbtn=['Enviar','Limpiar']
    
    # ------------- FIN Vale Code: Contacto ----------------
    
    context={'linkTitulo':linkTitulo,'linkrows':linkrow,'linkcols':linkcol,'link_range4':link_range4,'link_txt0':link_txt0,'link_txt1':link_txt1,'link_txt2':link_txt2,
    'conTitulo':conTitulo,'con_txtrange':con_txtrange, 'con_txtbtn':con_txtbtn
    }
    return render(request,'miapp2/index.html',context)
