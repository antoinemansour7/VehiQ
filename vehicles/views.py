from django.shortcuts import get_object_or_404, redirect, render
from vehicles.forms import AddCarForm, EditCarForm
from django.contrib.auth.decorators import login_required
from .models import Car


@login_required
def view_available_vehicles(request):
    available_vehicles = Car.objects.filter(reserved=False)
    return render(request, 'vehicles/view_available_vehicles.html', {'available_vehicles': available_vehicles})

@login_required
def add_car(request):
    if request.method == 'POST':
        form = AddCarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.company_uuid = request.user.profile.company_uuid
            car.save()
            return redirect('company_dashboard')
    else:
        form = AddCarForm()

    return render(request, 'vehicles/add_car.html', {'form': form})


@login_required
def list_company_cars(request):
    company_uuid = request.user.profile.company_uuid
    company_cars = Car.objects.filter(company_uuid=company_uuid)
    return render(request, 'vehicles/list_company_cars.html', {'company_cars': company_cars})

@login_required
def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id, company_uuid=request.user.profile.company_uuid)

    if request.method == 'POST':
        form = EditCarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('list_company_cars')
    else:
        form = EditCarForm(instance=car)

    return render(request, 'vehicles/edit_car.html', {'form': form, 'car': car})

@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id, company_uuid=request.user.profile.company_uuid)

    if request.method == 'POST':
        car.delete()
        return redirect('list_company_cars')

    return render(request, 'vehicles/delete_car.html', {'car': car})