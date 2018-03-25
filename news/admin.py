from django.contrib import admin
from news.models import Articles
from categories.models import Categories

admin.site.register(Articles)
admin.site.register(Categories)