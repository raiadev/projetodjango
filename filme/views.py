from django.shortcuts import render, reverse, redirect
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

#^^ Classe no python que será passada à class base views a serem bloqueadas(as pages restritas)


# Create your views here.

#Function based views
#def homepage(request):
#    return render(request, "homepage.html")

class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage

    def get(self,request, *args, **kwargs):
        #contabilizar as visualizações

        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs) #redireciona para a homepage


    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')


class Homefilmes( LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme
    #object_list >> lista de filmes do modelo

class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesFilme.html"
    model = Filme
    #object >> 1 item do modelo

    def get(self,request, *args, **kwargs):
        #contabilizar as visualizações
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs) #redireciona o user para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
       #filtrar tabela de filmes, pegando os filmes cuja categoria é igual ao  do filme na pag.
       #self.get_object()
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context

class Pesquisafilme( LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme
    # editar object list
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get("query")
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None



class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')


class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(selfself, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')




    #object_list >> lista de filmes do modelo





#def homefilmes(request):
    #context = {}
    #lista_filmes = Filme.objects.all()
    #context['lista_filmes'] = lista_filmes
    #return render(request, "homefilmes.html" , context)

#criar o context -> dicionário
#create class based views
