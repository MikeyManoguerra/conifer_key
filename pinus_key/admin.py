from django.contrib import admin

# Register your models here.


from django.contrib import admin

from .models import PinusGenus
from .models import PinusKey


admin.site.register(PinusGenus)
admin.site.register(PinusKey)