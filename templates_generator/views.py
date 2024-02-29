from django.shortcuts import render
from .models import BusinessType, WebsiteTemplate

def home(request):
    business_types = BusinessType.objects.all()
    return render(request, 'home.html', {'business_types': business_types})

def generate_template(request):
    if request.method == 'POST':
        business_type_id = request.POST.get('business_type')
        website_template = WebsiteTemplate.objects.filter(business_type=business_type_id).first()
        if website_template:
            return render(request, 'generated_template.html', {'template_html': website_template.template_html})
        else:
            return render(request, 'error.html', {'message': 'Template not found for selected business type'})
    return render(request, 'error.html', {'message': 'Invalid request'})

