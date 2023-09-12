# ALUMNO AGUSTIN LUCAS PONCE DE LEON
# PROYECTO PYTHON - CURSO CODER HOUSE

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sof-shoes/', include('AppCoder.urls')),
]

