from django.shortcuts import render

# Create your views here.

def index(request):
    
    # ------------- Vale Code ----------------
    '''
    
    '''
    linkrow=[1,2]
    linkcol=[1,2]
    range_4=[1,2,3,4]
    linktxt0='  Enlaces Tipo '
    linktxt1='Enlace de interés del grupo '
    linktxt2='Ver más'
    context={'linkrows':linkrow,'linkcols':linkcol,'range_4':range_4,
    'linktxt0':linktxt0,'linktxt1':linktxt1,'linktxt2':linktxt2}
    
    return render(request,'miapp2/index.html',context)
