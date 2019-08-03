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

class SearchResultsPageView(generic.base.TemplateView):
    template_name = 'olympic_games/results.html'

    def get(self, request):
        leta = OlimpijskeIgre.objects.all().order_by('-leto')
        discipline = Disciplina.objects.all().order_by('ime')
        context = {"leta": leta, "discipline": discipline}
        return render(request, 'olympic_games/results.html', context=context)


def get_results(request, year, discipline):
    disc = Disciplina.objects.filter(ime=discipline)[0].id
    results = Rezultat.objects.filter(disciplina=disc, olimpijske_igre=year).order_by("mesto")
    rez = []
    oseba = []
    for i in str(results).split(' ')[1:]:
        if i == '<Rezultat:' or i == '[<Rezultat:':
            oseba = []
        if i[-1] == '>' or i[-1] == ',':
            if i[-1] == '>':
                oseba.append(i[:-3])
            else:
                oseba.append(i[:-2])
            rez.append(oseba[1:])
            oseba = []
        else:
            oseba.append(i)
    context = {
        'results': rez
    }
    return render(request, 'olympic_games/write_out_results.html', context=context)





    










    


