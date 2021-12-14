from django.http import request
from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""

    if request.method != "POST":
        form = UserCreationForm()
    else:
        # Process submitted form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Login then redirect to index
            login(request, new_user)
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
