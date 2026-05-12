from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Service(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_desc = models.TextField()
    description = RichTextField()
    icon = models.CharField(max_length=100, default="fas fa-bullhorn")
    highlighted = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=150, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    before_image = models.ImageField(upload_to='portfolio/before/', blank=True, null=True)
    after_image = models.ImageField(upload_to='portfolio/after/')
    result = models.TextField()
    date = models.DateField(auto_now_add=True)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(default=5)
    image = models.ImageField(upload_to='testimonials/', blank=True)

    def __str__(self):
        return self.name


class PricingPackage(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.CharField(max_length=20, default="month")
    features = models.JSONField(default=list)
    recommended = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = RichTextField()
    image = models.ImageField(upload_to='blog/', blank=True)
    category = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class CompanyInfo(models.Model):
    name = models.CharField(max_length=100, default="PixelPilot")
    tagline = models.CharField(max_length=300, default="Navigating Your Brand to Digital Success")
    about_story = RichTextField()
    mission = RichTextField()
    email = models.EmailField(default="hello@pixelpilot.in")
    phone = models.CharField(max_length=20, default="+91 98765 43210")
    whatsapp = models.CharField(max_length=20, default="+919876543210")
    address = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Company Information"

    def __str__(self):
        return self.name