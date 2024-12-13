from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required,  user_passes_test
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import FileResponse, Http404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import JsonResponse
import os

from .models import Curso, Material

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
def acessar(request, curso_id):
    # Filtra o curso específico que o usuário tem permissão para acessar
    try:
        curso = Curso.objects.get(id=curso_id, aluno=request.user)  # Garante que o curso pertence ao aluno
    except Curso.DoesNotExist:
        # Se o curso não for encontrado ou o usuário não for aluno desse curso, retorna uma resposta de erro
        return HttpResponse("Curso não encontrado ou você não tem acesso a este curso", status=404)
    
    # Pré-carrega os vídeos e materiais do curso
    curso.videos.all()  # Carrega os vídeos
    curso.arquivos.all()  # Carrega os arquivos
    
    context = {'curso': curso}
    return render(request, 'acessar.html', context)

login_required
def visualizar_pdf(request, material_id):
    try:
        material = Material.objects.get(pk=material_id)
        # Verifica se o arquivo existe
        if not os.path.exists(material.pdf.path):
            raise Http404("Arquivo PDF não encontrado.")
        
        with open(material.pdf.path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="{material.title or "documento.pdf"}"'
            return response
    except Material.DoesNotExist:
        raise Http404("Material não encontrado.")
