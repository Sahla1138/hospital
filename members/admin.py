from django.contrib import admin
from .models import Department, Doctor,Booking

admin.site.register(Department)
admin.site.register(Doctor)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','is_expired','booking_date',  'booked_on','p_name', 'doc_name', 'p_email', 'p_phone')
    list_filter = ('is_expired', 'booking_date')
    search_fields = ['doc_name__doc_name','booking_date','p_name']
admin.site.register(Booking,BookingAdmin)



