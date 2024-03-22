# rental_agreements/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import RentalAgreement
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def review_agreement(request):
    # Assume there's only one agreement for simplicity
    agreement = RentalAgreement.objects.first()
    return render(request, 'rental_agreements/review_agreement.html', {'agreement': agreement})

@login_required
def sign_agreement(request, agreement_id):
    agreement = get_object_or_404(RentalAgreement, id=agreement_id)
    if request.method == 'POST':
        signature_image = request.FILES['signature_image']
        agreement.signature_image = signature_image
        agreement.signed = True
        agreement.date_signed = timezone.now()
        agreement.save()
        return redirect('agreement_signed_confirmation')
    return render(request, 'rental_agreements/sign_agreement.html', {'agreement': agreement})

def agreement_signed_confirmation(request):
    return render(request, 'rental_agreements/agreement_signed_confirmation.html')
