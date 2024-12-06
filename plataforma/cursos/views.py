from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required,  user_passes_test
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import JsonResponse

from .models import Curso

@login_required
def administrador(request):
    cursos = Curso.objects.all()
    
    context = {
        
        'cursos': cursos
    }
    return render(request, 'administrador.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Autenticar o usuário
            user = form.get_user()
            auth_login(request, user)
            return redirect('main') 
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})



@login_required
def cadastrar_aluno(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        nome_completo = request.POST.get('nome_completo')
        cod_aluno = request.POST.get('cod_aluno')
        
        if form.is_valid():
            user = form.save()
            user.first_name = nome_completo
            user.last_name = cod_aluno
            user.save()
            

            messages.success(request, 'Aluno cadastrado com sucesso e adicionado ao grupo Alunos!')
            
        else:
            messages.error(request, 'Erro ao cadastrar aluno. Verifique os dados.')
    else:
        form = UserCreationForm()
    
    return render(request, 'cadastrar_aluno.html', {'form': form})

@login_required
def main (request):
      
        cursos = Curso.objects.filter(aluno = request.user)
        context = {
            'cursos': cursos 
        }
        return render(request, 'main.html', context)

@require_POST
def custom_logout(request):
    logout(request)
    return render('login.html')  # Redireciona para a página de login (login.html)

@login_required
def acessar(request):
        cursos = Curso.objects.filter(aluno=request.user)
    # Criar uma lista de dicionários com os valores ajustados
        cursos_modificados = []
        for curso in cursos:
            video_aula_embed = curso.video_aula
        # Substituir "watch?v=" por "embed/" para vídeos do YouTube
        if "watch?v=" in video_aula_embed:
            video_aula_embed = video_aula_embed.replace("watch?v=", "embed/")
        
        # Adicionar os dados modificados em uma lista
        cursos_modificados.append({
            'name': curso.name,
            'slug': curso.slug,
            'short_description': curso.short_description,
            'long_description': curso.long_description,
            'pdf': curso.pdf,
            'video_aula': video_aula_embed
        })

        context = {
        'cursos': cursos_modificados  # Enviar a lista modificada ao template
        }
        return render(request, 'acessar.html', context)