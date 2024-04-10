from django.http import JsonResponse
from django.utils import timezone
from .models import RentalAgreement, Reservation
from .utils import take_deposit

def sign_agreement(request, agreement_id):
    if request.method == 'POST':
        try:
            agreement = RentalAgreement.objects.get(id=agreement_id, signed=False)
            agreement.signed = True
            agreement.date_signed = timezone.now()
            agreement.save()
            return JsonResponse({'success': True, 'message': 'Agreement signed.'})
        except RentalAgreement.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Agreement not found or already signed.'})

def process_deposit(request, reservation_id):
    if request.method == 'POST':
        try:
            reservation = Reservation.objects.get(id=reservation_id, deposit_taken=False)
            success, message = take_deposit(reservation.user.id, 500)  # Assuming a fixed deposit amount
            if success:
                reservation.deposit_taken = True
                reservation.save()
                return JsonResponse({'success': True, 'message': message})
            else:
                return JsonResponse({'success': False, 'message': 'Failed to process deposit.'})
        except Reservation.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Reservation not found or deposit already taken.'})
