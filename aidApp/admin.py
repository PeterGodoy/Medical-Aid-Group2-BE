from django.contrib import admin
from .models import Doctors
from .models import Clinics
from .models import Pharmacies
from .models import Patients
from .models import Consultations
from .models import Feedback_Complaint
from .models import FAQ


from .models import ContactUs, Newsletter
# Register your models here.


admin.site.register(ContactUs)
admin.site.register(Newsletter)
admin.site.register(Doctors)
admin.site.register(Clinics)
admin.site.register(Pharmacies)
admin.site.register(Patients)
admin.site.register(Consultations)
admin.site.register(Feedback_Complaint)
admin.site.register(FAQ)
