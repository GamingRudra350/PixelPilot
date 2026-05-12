from django.shortcuts import render, get_object_or_404
from .models import *

def home(request):
    company = CompanyInfo.objects.first()
    services = Service.objects.all().order_by('order')[:6]
    return render(request, 'home.html', {
        'company': company,
        'services': services,
    })

def about(request):
    company = CompanyInfo.objects.first()
    return render(request, 'about.html', {'company': company})

def services(request):
    services = Service.objects.all().order_by('order')
    return render(request, 'services.html', {'services': services})

def portfolio(request):
    portfolios = Portfolio.objects.filter(featured=True)
    return render(request, 'portfolio.html', {'portfolios': portfolios})

def pricing(request):
    packages = PricingPackage.objects.all().order_by('order')
    return render(request, 'pricing.html', {'packages': packages})

def blog(request):
    posts = BlogPost.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'blog_detail.html', {'post': post})

def contact(request):
    company = CompanyInfo.objects.first()
    return render(request, 'contact.html', {'company': company})
# Create your views here.
