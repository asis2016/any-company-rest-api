from django.contrib import admin

from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    """
    Displays Testimonials in admin site.
    """
    list_display = ('id', 'client_name', 'created',)


admin.site.register(Testimonial, TestimonialAdmin)
