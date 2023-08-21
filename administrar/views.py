from django.shortcuts import render
from django.http import HttpResponseRedirect
from administrar.models import Tarea # Importar el modelo
from .forms import TareaFrom
# Create your views here.
def v_index(request):
  if request.method == 'POST':
    ######
    # Post, voy a crear un registro
    ######
    _titulo = request.POST["titulo"]
    datos = request.POST.copy()
    form = TareaFrom(datos) # para validaciones
    if form.is_valid():
      form.save()
    else:
      return HttpResponseRedirect("/")

    if False:
      tarea = Tarea()
      tarea.titulo = _titulo
      tarea.save()
    
    return HttpResponseRedirect("/")
  else:
    ##peticiones metodo GET
    
    consulta = Tarea.objects.filter(titulo__icontains = request.GET.get("titulo",""))

    if request.GET.get("estado", "") != "":
      consulta = consulta.filter(estado = request.GET.get("estado", ""))
    ## Listar las tareas
    
    context = {
      'var1': 'Valor1',
      'var2': 'Valorasdasdasdasdasd',
      'lista': consulta
    }
    return render(request, 'pagina_x.html',context)

def v_eliminar(request, tarea_id):
  Tarea.objects.filter(id = tarea_id).delete()
  return HttpResponseRedirect("/") # Redirigir

def v_completado(request, tarea_id):
  task = Tarea.objects.get(id = tarea_id)
  task.estado = 1
  task.save()
  return HttpResponseRedirect('/')