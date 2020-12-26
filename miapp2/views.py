from django.shortcuts import render

# Create your views here.

# esta funciòn renderiza index2 que usa como base a index
def mostrar_index2(request):
    numeros_a = ['1', '2', '3', '4']
    numeros_b = ['5','6','7']
    datos = {'numeros_a': numeros_a, 'numeros_b': numeros_b}
    return render(request, 'miapp2/index2.html', context=datos)

