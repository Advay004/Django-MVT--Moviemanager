from django.shortcuts import render
from . models import Movieinfo
from . forms import Movieform
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login')
def list(request):
    """moviedata={
    'movie':[{
    'title':"godfather",
    'year':1990,
    'img':'godfather.png',
    'summary':"story of an underworld don",
    'success': True
    },
    {
    'title':"titanic",
    'year':2000,
    'img':'titaniclogo.webp',
    'summary':"story of a woman falling in love with a poor",
    'success': True
    },
    {
    'title':"malayali from india",
    'year':2024,
    'img':'mwi.jpg',
    'success': False
    }]
}"""
    print(request.COOKIES)
    visit=int(request.COOKIES.get('visit',0))
    visit=visit+1
    movieset=Movieinfo.objects.all()
    

    print(movieset)
    response=render(request,'list.html',{'movie':movieset,'visit':visit})
    response.set_cookie('visit',visit)
    return response
@login_required(login_url='/login')
def create(request):
    frm=Movieform()
    if request.POST:
        frm=Movieform(request.POST)
        if frm.is_valid():
            frm.save()
        else:
            frm=Movieform()
    return render(request,'create.html',{'frm':frm})
@login_required(login_url='/login')
def edit(request,pk):
    instance_to_be_edited=Movieinfo.objects.get(pk=pk)
    if request.POST:
        frm=Movieform(request.POST,instance=instance_to_be_edited)
        if frm.is_valid():
            instance_to_be_edited.save()
    else:    
        frm=Movieform(instance=instance_to_be_edited)
    return render(request,'create.html',{'frm':frm})
@login_required(login_url='/login')
def delete(request,pk):
    instance=Movieinfo.objects.get(pk=pk)
    instance.delete()
    movieset=Movieinfo.objects.all()
    return render(request,'list.html',{'movie':movieset})



# Create your views here.

    