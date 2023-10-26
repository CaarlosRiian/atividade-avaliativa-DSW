from django.shortcuts import render
from .models import Aluno
from .forms import AlunoForm

# Create your views here.
def index(request):

    alunos = Aluno.objects.all()

    context = {
        'alunos': alunos,
    }

    return render(request, 'index.html', context)

def editar(request, pk):

    aluno = Aluno.objects.get(pk=pk)

    context = {
        'aluno': aluno,
    }

    return render(request, 'editar.html', context)

def cadastro(request):

    form = AlunoForm()

    context = {
        'form': form
    }

    return render(request, "cadastro.html", context)