from django.db import models
from django.db.models.fields.related import ForeignKey



class Article(models.Model):
    Nom = models.CharField(max_length=100)
    Type = models.CharField(max_length=100,)
    Marque = models.CharField(max_length=100,)
    nbDisponible = models.IntegerField(null=True,)
    prix = models.FloatField(null=True,)

    def __str__(self):
        return self.Nom



class Etablissement(models.Model):
    Nom = models.CharField(max_length=100,unique=True)
    Montant = models.FloatField(null=True,)
    
    def __str__(self):
        return self.Nom


class Bon(models.Model):
    Num = models.IntegerField(null=True)
    Etab = models.ForeignKey(Etablissement,on_delete=models.CASCADE)
    Type = models.CharField(max_length=100,)
    date = models.DateField()
    Montant = models.FloatField(null=True,)
    paye = models.BooleanField()
    def __str__(self):
        return "BL n°"+str(self.Num) +" "+self.Etab.Nom+"("+self.Type+")"
    
class Facture(models.Model):
    Num = models.IntegerField(null=True)
    Etab = models.ForeignKey(Etablissement,on_delete=models.CASCADE)
    Type = models.CharField(max_length=100,)
    date = models.DateField()
    Montant = models.FloatField(null=True,)
    Bons = models.ManyToManyField(Bon)
    paye = models.BooleanField()
    def __str__(self):
        return "Facture n°"+str(self.Num) +" "+self.Etab.Nom+"("+self.Type +")"


class ArticleBL(models.Model):
    article = ForeignKey(Article, on_delete=models.CASCADE)
    Quantité = models.IntegerField(null=True,)
    Bon = models.ForeignKey(Bon, on_delete=models.CASCADE ) 
    def __str__(self):
        return self.article.Nom+"("+ str(self.Quantité)+")"
