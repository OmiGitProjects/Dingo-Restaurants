from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages

def register(request):
        if request.method == 'POST':
                form = UserRegistrationForm(request.POST)
                
                if form.is_valid():
                        form.save()
                        username = form.cleaned_data.get('username')
                        messages.success(request, f' {username} Your Account Has Been Created!!!')
                        return redirect('HomePage')

        else:
                form = UserRegistrationForm()

        context = {'form':form}
        return render(request, 'userApp/register.html', context)