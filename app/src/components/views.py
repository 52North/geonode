# app/views.py
from django.shortcuts import render
from .models import STAService
from .utils import fetch_sta_data

def sta_service_view(request, service_id):
    service = STAService.objects.get(id=service_id)
    sta_data = fetch_sta_data(service.url)
    # For simplicity, passing the data directly to the template. In a real scenario, you'd likely process this data or use a Django REST Framework serializer for AJAX.
    return render(request, 'sta_service_template.html', {'sta_data': sta_data})
