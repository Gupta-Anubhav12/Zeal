from django.contrib import admin



# Register your models here.



from .models import Thought,Schedule

# Register your models here.

admin.site.register(Thought)
admin.site.register(Schedule)

