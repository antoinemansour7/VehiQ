from django.shortcuts import get_object_or_404, render, redirect 
from django.contrib.auth.decorators import login_required

from vehicles.models import Car
from .models import Profile, Reservation
from .forms import ProfileForm, ReservationForm 

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


# vehicles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Car, Reservation
from .forms import ReservationForm

@login_required
def make_reservation(request, car_id):
    car = get_object_or_404(Car, pk=car_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.profile = request.user.profile
            reservation.car = car
            reservation.reservation_date = timezone.now()
            reservation.modification_allowed_until = timezone.now() + timezone.timedelta(hours=24)
            reservation.save()
            car.reserved = True
            car.save()
            return redirect('user_reservations')
    else:
        form = ReservationForm()

    return render(request, 'accounts/make_reservation.html', {'form': form, 'car': car})


@login_required
def user_reservations(request):
    user_reservations = Reservation.objects.filter(profile=request.user.profile)
    return render(request, 'accounts/user_reservations.html', {'user_reservations': user_reservations})

@login_required
def modify_or_delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, profile=request.user.profile)

    if not reservation.is_modification_allowed():
        # Check if modification is still allowed
        return redirect('user_reservations')

    if request.method == 'POST':
        if 'modify' in request.POST:
            form = ReservationForm(request.POST, instance=reservation)
            if form.is_valid():
                form.save()
                return redirect('user_reservations')
        elif 'delete' in request.POST:
            reservation.delete()
            return redirect('user_reservations') 
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'accounts/modify_or_delete_reservation.html', {'form': form, 'reservation': reservation})
