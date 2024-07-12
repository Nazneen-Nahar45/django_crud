from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Member
def index(request):
    mem=Member.objects.all()
    context= {
        'mem': mem,
    }

    return render(request,template_name='index.html', context=context)

def add(request):

    return render(request, template_name='add.html')

def delete(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    return redirect('index')
def addrec(request):
    if request.method == 'POST':
        x = request.POST.get('first')
        y = request.POST.get('last')
        z = request.POST.get('country')

        if x and y and z:  # Ensure all fields are provided
            mem = Member(firstname=x, lastname=y, country=z)
            mem.save()
            return redirect('index')  # Redirect to the index page after adding the member
        else:
            return HttpResponse("All fields are required.", status=400)

    return HttpResponse("Invalid request method.", status=405)



def update(request,id):
    mem= Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})


def uprec(request,id):
    x = request.POST.get('first')
    y = request.POST.get('last')
    z = request.POST.get('country')
    mem=Member.objects.get(id=id)
    mem.firstname = x
    mem.lastname =y
    mem.country=z
    mem.save()
    return redirect("/")