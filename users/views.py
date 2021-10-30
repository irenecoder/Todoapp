from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    #log the user out
    logout(request)
    return HttpResponseRedirect(reverse('todoapp:index'))
def register(request):
    #register a new user
    if request.method != 'POST':
        #display blank registration form
        form = UserCreationForm()
    else:
        #process completed form
        form= UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #log the user in and then redirect to home page
            authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('todoapp:index'))

    context = {'form':form}
    return render(request,'registration/register.html',context)  