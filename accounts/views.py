from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm 

# Create your views here.
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to a view where users can see their profile
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})

