from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# class based views
class Homepage(TemplateView):
    template_name = "homepage.html"


class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object_list >> todos os objetos armazenados pelo modelo em models.py


class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # object >> 1 item do modelo

    def get(self, request, *args, **kwargs):
        #contabiliza uma visualização
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        return super().get(request, *args, **kwargs) # direciona o usuario para a url final

    def get_contex_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)
        context['filmes_relacionados'] = filmes_relacionados
        return context


# function based view
# def homepage(request):
#     return render(request, 'homepage.html')

# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)