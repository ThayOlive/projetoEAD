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
from .models import Curso, Material, Progresso, Video


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
    try:
        curso = Curso.objects.get(id=curso_id, aluno=request.user)
    except Curso.DoesNotExist:
        return HttpResponse("Curso não encontrado ou você não tem acesso a este curso", status=404)

    total_videos = curso.videos.count()
    total_assistidos = Progresso.objects.filter(curso=curso, aluno=request.user, assistido=True).count()
    progresso_percentual = (total_assistidos / total_videos) * 100 if total_videos > 0 else 0

    videos_assistidos = Progresso.objects.filter(curso=curso, aluno=request.user, assistido=True).values_list('video_id', flat=True)

    context = {
        'curso': curso,
        'progresso_percentual': progresso_percentual,
        'total_videos': total_videos,
        'total_assistidos': total_assistidos,
        'videos_assistidos': videos_assistidos,
    }
    
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


@login_required
def marcar_assistido(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    curso = video.cursos.first()  # Considerando que o vídeo pertence a apenas um curso
    if curso and request.user in curso.aluno.all():
        progresso, created = Progresso.objects.get_or_create(
            aluno=request.user,
            curso=curso,
            video=video
        )
        
        # Alterna o status de assistido
        progresso.assistido = not progresso.assistido  # Alterna entre True/False
        progresso.save()
        
        if progresso.assistido:
            return JsonResponse({'success': True, 'message': 'Vídeo marcado como assistido.'})
        else:
            return JsonResponse({'success': True, 'message': 'Vídeo desmarcado como assistido.'})
    
    return JsonResponse({'success': False, 'message': 'Permissão negada.'})

def progresso(request, curso_id):
   def progresso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    
    # Calculando o número total de vídeos e os vídeos assistidos
    total_videos = curso.videos.count()
    total_assistidos = curso.progresso.filter(aluno=request.user, assistido=True).count()
    
    # Calculando a porcentagem de vídeos assistidos
    progresso_percentual = 0
    if total_videos > 0:
       progresso_percentual = (total_assistidos / total_videos) * 100
       progresso_percentual = round(progresso_percentual, 2)  # Arredonda para 2 casas decimais
       progresso_percentual = min(max(progresso_percentual, 0), 100)  # Garante o intervalo [0, 100]

    
    # Passando esses dados para o template
    context = {
        'curso': curso,
        'total_videos': total_videos,
        'total_assistidos': total_assistidos,
        'progresso_percentual': progresso_percentual,
        
    }
    return render(request, 'cursos/acessar.html', context)
