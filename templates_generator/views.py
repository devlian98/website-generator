
from django.shortcuts import render
from .models import BusinessType, WebsiteTemplate
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



#def home(request):
#    business_types = BusinessType.objects.all()
#    return render(request, 'home.html', {'business_types': business_types})

class UserCreate(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
  return render(request, 'index.html')


def index_view(request):
    # Your logic here
    return render(request, 'restaurant_template/index.html')

def menu_view(request):
    # Your logic here
    return render(request, 'restaurant_template/menu.html')

def about_view(request):
    # Your logic here
    return render(request, 'restaurant_template/about.html')

def book_view(request):
    # Your logic here
    return render(request, 'restaurant_template/book.html')    

def generate_template(request):
    if request.method == 'POST':
        business_type_id = request.POST.get('business_type')
        website_template = WebsiteTemplate.objects.filter(business_type=business_type_id).first()
        print(website_template.template_html)
        if website_template:
            if  website_template.template_html =='restaurant':
                 return render(request, 'restaurant_template/index.html', {'template_html': website_template.template_html})
            elif website_template.template_html =='barber':
                 return render(request, 'barbershop_template/index.html', {'template_html': website_template.template_html})
            elif website_template.template_html =='portfolio':
                 return render(request, 'portfolio_template/index.html', {'template_html': website_template.template_html})
            elif website_template.template_html =='ecommerce':
                 return render(request, 'ecommerce_template/index.html', {'template_html': website_template.template_html})


        else:
            return render(request, 'error.html', {'message': 'Template not found for selected business type'})
    return render(request, 'error.html', {'message': 'Invalid request'})