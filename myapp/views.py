
from django.shortcuts import render, redirect
from myapp.models import student
from djangocrud.forms import studentForm



# Create your views here.
class StudentForm:
    pass


def index(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass

    else:
        form = studentForm()
        return render(request, 'index.html', {'form': form})


def show(request):
    students = student.objects.all()
    return render(request, 'show.html', {'students': students})



def edit(request,id):
    student = studentForm.objects.get(id=id)
    return render(request, 'edit.html', {'student': student})


def delete(request, id):
    student = studentForm.objects.get(id=id)
    student.delete()
    return redirect('/show')




def update(request, id):
    student = studentForm.objects.get(id=id)
    form = studentForm(request.POST, instance=student)
    if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        return render(request, 'edit.html', {'student': student})


