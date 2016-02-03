from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Articulos
from models import Question

from django.template import RequestContext
from django.utils import timezone

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("<h1>usted esta buscando en las preguntas</h1><hr> %s." % question_id)

def results(request, question_id):
    response = "Usted esta buscando en los resultados de las preguntas %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Usted esta votando una pregunta %s." % question_id)

def page(request, num='1'):
    return HttpResponse("Usted esta en el blog %s." % num)

def ejemplo1(request):
	return render_to_response('ejemplo1.html', context_instance=RequestContext(request))

def ejemplo2(request):
    title_list = Articulos.objects.order_by('-fecha')[:]
    template = loader.get_template('ejemplo2.html')
    context = {
        'title_list': title_list,
    }
    return HttpResponse(template.render(context, request))

def ejemplo3(request):
#	return render_to_response('ejemplo2.html', {})
    title_list = Articulos.objects.order_by('fecha')[:]
    template = loader.get_template('ejemplo3.html')
    context = {
        'title_list': title_list,
    }
    return HttpResponse(template.render(context, request))

def insertar(request):
	try:
		tit = request.POST['titulo']
		cont = request.POST['contenido']
		print 'titulo=', tit,'\ncontenido=', cont
		a = Articulos(titulo=tit, contenido=cont, fecha = timezone.now())
		a.save()
		return render_to_response('insertar.html', {})
	except Exception as e:
		return render_to_response('insertar.html', {})

def actualizar(request):
	try:
		tit = request.POST['titulo']
		cont = request.POST['contenido']
		fech = request.POST['fecha']
		id_upd = request.POST['id']
		print 'id=',id_upd,'\ntitulo=', tit,'\ncontenido=', cont,'\nfecha=',fech
#		print timezone.now()
#		2016-01-30 03:05:25.490543+00:00
		Articulos.objects.filter(id=id_upd).update(titulo=tit, contenido=cont, fecha=fech)
		return render_to_response('actualizar.html', {})
	except Exception as e:
		return render_to_response('actualizar.html', {})

def borrar(request):
	try:
		id_del = request.POST['id']
		print 'id=',id_del
		Articulos.objects.filter(id=id_del).delete()
		return render_to_response('borrar.html', {})
	except Exception as e:
		return render_to_response('borrar.html', {})

def lista_borrar(request):
	title_list = Articulos.objects.all()
	context = {'title_list': title_list}
	return render(request, 'polls/lista_borrar.html', context)

def borrar2(request):
	try:
		articulo_seleccionado = get_object_or_404(Articulos, pk=request.POST['articulo'])
	except (KeyError, Articulos.DoesNotExist):
		return render(request, 'polls/lista_borrar.html', {'title_list':Articulos.objects.all() ,'error_message':"No has seleccionado un arituclo para borrar."})
	else:
		articulo_seleccionado.delete()
	return HttpResponseRedirect(reverse('lista_borrar'))

#    selected_choice.votes += 1
#    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
#    return HttpResponseRedirect(reverse('polls:results', args=(articulo.id,)))

