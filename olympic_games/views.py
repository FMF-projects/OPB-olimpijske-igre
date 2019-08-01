from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Disciplina, OlimpijskeIgre, Drzava, Tekmovalec, Rezultat


class HomePageView(generic.base.TemplateView):
    template_name = 'olympic_games/home.html'

class ResultsPageView(generic.base.TemplateView):
    template_name = 'olympic_games/results.html'

    def rezultat(self, leto, disciplina):
        disc = Disciplina.objects.filter(ime=disciplina)[0].id
        rezultati = Rezultat.objects.filter(olimpijske_igre=leto, disciplina=disc)
        return rezultati.order_by('mesto')

    def get(self, request):
        leta = OlimpijskeIgre.objects.all().order_by('-leto')
        discipline = Disciplina.objects.all().order_by('ime')
        context = {"leta": leta, "discipline": discipline}
        return render(request, 'olympic_games/results.html', context=context)

def detail(request, leto, disciplina):
    list_of_results = Rezultat.objects.filter(disciplina=disciplina, olimpijske_igre=leto).order_by("mesto")
    template_name = loader.get_template('write_out_results.html')
    context = {
        'list_of_results': list_of_results
    }
    return render(request, template_name, context)





    










    


