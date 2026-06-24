from pydoc import doc
from django.shortcuts import render, redirect
from .models import Booking, Doctor, Department
from .forms import BookingForm
from django.db.models import Q,Count
from django.contrib import messages
from datetime import date

def home(request):

    Booking.objects.filter(
        booking_date__lt=date.today(),
        is_expired=False
    ).update(is_expired=True)

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)

            if booking.booking_date < date.today():
                messages.error(request, "Booking date cannot be in the past.")
                return redirect('/#booking')  

            booking.save()
            return redirect('confirmation')

    else:
        form = BookingForm()

    doc = Doctor.objects.annotate(
        active_bookings=Count(
            'bookings',
            filter=Q(bookings__is_expired=False)
        )
    )
    return render(request, 'index.html', {
        'doc': doc,
        'dept': Department.objects.all(),
        'form': form
    })


def confirmation(request):
    return render(request, 'confirmation.html')


