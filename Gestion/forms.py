from django import forms
from django.forms.widgets import DateTimeInput

from Gestion.models import Article, Bon, Etablissement, Facture, ArticleBL

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = "__all__"
    
class ArticleBLForm(forms.ModelForm):
  class Meta:
    model = ArticleBL
    fields = "__all__"


class EtablissementForm(forms.ModelForm):
  class Meta:
    model = Etablissement
    fields = "__all__"
    

class FactureForm(forms.ModelForm):
  class Meta:
    model = Facture
    fields = "__all__"
    widgets = {
      'date' : DateTimeInput(attrs={'type' : 'date'}) ,
    }


class BonForm(forms.ModelForm):
  class Meta:
    model = Bon
    fields = "__all__"
    widgets = {
      'date' : DateTimeInput(attrs={'type' : 'date'}) ,
    }



