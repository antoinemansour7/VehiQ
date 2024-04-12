from django.contrib.auth import login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from .models import CustomUser, Reservation
from .serializers import UserSerializer, ReservationSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password


def custom_authenticate(email, password):
    User = get_user_model()
    try:
        user = User.objects.get(email=email)
        if check_password(password, user.password):
            return user
    except User.DoesNotExist:
        pass
    return None


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password or not email:
        return JsonResponse({'error': 'Username, password, and email are required'}, status=400)

    if CustomUser.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username already exists'}, status=400)

    # Create a new CustomUser instance with the provided details
    user = CustomUser.objects.create_user(username=username, email=email, password=password)

    # Populate the "user" field with the username
    user_data = {
        "id": user.id,
        "username": user.username,  # Corrected field name to "username"
        "visibility": user.visibility,
        "email": user.email,
        "is_staff": user.is_staff,
        "is_active": user.is_active,
        "date_joined": user.date_joined
    }

    return JsonResponse(user_data, status=201)


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return JsonResponse({'error': 'Email and password are required'}, status=400)

    # Debug print to check email and password
    print("Email:", email)
    print("Password:", password)

    # Authenticate user using email and password
    user = custom_authenticate(email=email, password=password)

    if user is not None:
        # User authenticated, log them in
        login(request, user)

        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "is_staff": user.is_staff,
            "is_active": user.is_active,
            "date_joined": user.date_joined,
            "isLoggedIn": True
        }

        return JsonResponse({'success': 'User logged in successfully', 'user': user_data})
    else:
        # Invalid credentials
        print("Authentication failed for email:", email)
        return JsonResponse({'error': 'Invalid credentials'}, status=401)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    logout(request)
    return JsonResponse({'success': 'User logged out successfully'})


class AllReservations(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class UserReservationsViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


class AllUsers(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    # from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm  # noqa: F401
# from django.contrib.auth import login
# from vehicles.models import Car
# from .models import Reservation
# from .forms import RegistrationForm, ReservationForm
# from django.utils import timezone
# from django.db import IntegrityError
# from django.contrib import messages
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import UserSerializer

# @api_view(['POST'])
# def register_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @login_required
# def user_dashboard(request):
#     return render(request, 'accounts/user_dashboard.html')


# @login_required
# def company_dashboard(request):
#     return render(request, 'accounts/company_dashboard.html')


# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()

#             try:
#                 profile, created = Profile.objects.get_or_create(
#                     user=user, defaults={'user_type': form.cleaned_data['user_type']}
#                 )
#             except IntegrityError:
#                 messages.error(request, 'An error occurred while creating the profile. Please try again.')
#                 return redirect('registration_error')

#             if not created:
#                 profile.user_type = form.cleaned_data['user_type']
#                 profile.save()

#             login(request, user)
#             return redirect('user_reservations')
#     else:
#         form = RegistrationForm()

#     return render(request, 'registration/register.html', {'form': form})


# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = ProfileForm(instance=request.user.profile)
#     return render(request, 'accounts/edit_profile.html', {'form': form})


# @login_required
# def make_reservation(request, car_id):
#     car = get_object_or_404(Car, pk=car_id)

#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             reservation = form.save(commit=False)
#             reservation.profile = request.user.profile
#             reservation.car = car
#             reservation.reservation_date = timezone.now()
#             reservation.modification_allowed_until = timezone.now() + timezone.timedelta(hours=24)
#             reservation.save()
#             car.reserved = True
#             car.save()
#             return redirect('user_reservations')
#     else:
#         form = ReservationForm()

#     return render(request, 'accounts/make_reservation.html', {'form': form, 'car': car})


# @login_required
# def user_reservations(request):
#     user_reservations = Reservation.objects.filter(profile=request.user.profile)
#     return render(request, 'accounts/user_reservations.html', {'user_reservations': user_reservations})


# @login_required
# def modify_or_delete_reservation(request, reservation_id):
#     reservation = get_object_or_404(Reservation, id=reservation_id, profile=request.user.profile)

#     if not reservation.is_modification_allowed():
#         # Check if modification is still allowed
#         return redirect('user_reservations')

#     if request.method == 'POST':
#         if 'modify' in request.POST:
#             form = ReservationForm(request.POST, instance=reservation)
#             if form.is_valid():
#                 form.save()
#                 return redirect('user_reservations')
#         elif 'delete' in request.POST:
#             reservation.delete()
#             return redirect('user_reservations')
#     else:
#         form = ReservationForm(instance=reservation)

#     return render(request, 'accounts/modify_or_delete_reservation.html', {'form': form, 'reservation': reservation})
