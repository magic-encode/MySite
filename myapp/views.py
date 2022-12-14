from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .forms import CommentForm
from .forms import GetInfoForm

from .models import Comments
from .models import PhotoFor
from .models import AddProject

from myapp.bots.bot import telegram_bot_sendtext

from django.http.response import FileResponse


# ----------------------------  home func --------------------------------------------------


def homeView(request):
    
    return render(request, 'home/include_home.html')

# ----------------------------  about func --------------------------------------------------


def aboutView(request):
    items = Comments.objects.all()
    foto = PhotoFor.objects.all()

    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

            return redirect('about')
    else:
        form = CommentForm()

    context = {
        'form': form,
        'items': items,
        'foto': foto
    }

    return render(request, 'myapp/about/include_about.html', context)

# ----------------------------  comment func --------------------------------------------------

# ----------------------------  Resume func ----------------------------------------------

def myResumeDownloadView(request):

    filename = './static/resume.pdf'

    response = FileResponse(open(filename, 'rb'))
    return response

def commentRemove(request, pk):
    comment = Comments.objects.get(id=pk)
    comment.delete()

    return redirect('about')

# ----------------------------  project func --------------------------------------------------


def projectView(request):
    projects = AddProject.objects.all()
    context = {'projects': projects}
    return render(request, 'myapp/project/include_project.html', context)

# ----------------------------  contact func --------------------------------------------------

def contactView(request):
    
    form = GetInfoForm()
    if request.POST:
        form = GetInfoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            text = f"Xabar yuborgan shaxs => => {obj.fullname}\n Email => =>{obj.email}\n Xabar matni => => {obj.message}"
            resp = telegram_bot_sendtext(text)
            if resp:
                messages.success(
                    request, 'Xabaringiz muofaqqiyati yuborildi, tez oraqa sizga javob beramiz!')
            else:
                messages.success(
                    request, "Xabar yuborib  men biln bog'")

            return redirect('contact')

    else:
        form = GetInfoForm()

    context = {
        "form": form
    }

    return render(request, 'myapp/contact/include_contact.html', context)
