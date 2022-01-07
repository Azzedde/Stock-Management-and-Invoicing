from django.contrib import admin
from .models import Article, ArticleBL, Bon, Etablissement, Facture
# Register your models here.
admin.site.register(Article)
admin.site.register(Bon)
admin.site.register(Etablissement)
admin.site.register(Facture)
admin.site.register(ArticleBL)
