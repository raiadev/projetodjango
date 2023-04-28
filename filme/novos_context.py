from .models import Filme
#criar todas as var padrões que o html irá usar


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}


def lista_filmes_populares(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_filmes_populares": lista_filmes}

 ##filme_destaque(request):
    #filme = Filme.objects.order_by('-data-criacao')[0]
    #return {"filme_destaque": filme}
