from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Products)
admin.site.register(ProductBundles)
admin.site.register(BundleProducts)
admin.site.register(Reviews)
admin.site.register(Sentiment)
admin.site.register(Orders)