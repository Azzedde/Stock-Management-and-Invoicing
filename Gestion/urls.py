from django.urls import path

from . import views

urlpatterns = [
    path('', views.Accueil, name='Accueil'),
    path('Contact', views.Contact, name='Contact'),
    path('Travail', views.Travail , name='Travail'),
    path('Travail/GestionStock', views.GestionStock, name='GestionStock'),
    path('Travail/GestionStock/Consulter/<int:id>', views.AfficherArticle, name='afficherArticle'),
    path('Travail/GestionStock/Modifer/<int:id>', views.ModifierArticle, name='modifierArticle'),
    path('Travail/GestionStock/Ajouter', views.AjouterArticle, name='ajouterArticle'),
    path('Travail/GestionStock/Supprimer/<int:id>', views.SupprimerArticle, name='supprimerArticle'),
    path('Travail/GestionStock/ModifierStock', views.ModifierStock, name='modifierStock'),
    path('Travail/Comptabilité', views.Comptabilité, name="Comptabilité"),
    path('Travail/Comptabilité/AjouterEtablissement', views.AjouterEtablissement, name="AjouterEtablissement"),
    path('Travail/Comptabilité/AjouterFacture', views.AjouterFacture, name="AjouterFacture"),
    path('Travail/Comptabilité/AjouterBL', views.AjouterBL, name="AjouterBL"),
    path('Travail/Comptabilité/ConsulterEtablissement/<int:id>', views.ConsulterEtablissement, name="ConsulterEtablissement"),
    path('Travail/Comptabilité/ConsulterFacture/<int:id>', views.ConsulterFacture, name="ConsulterFacture"),
    path('Travail/Comptabilité/ConsulterBL/<int:id>', views.ConsulterBL, name="ConsulterBL"),
    path('Travail/Comptabilité/ModifierEtablissement/<int:id>', views.ModifierEtablissement, name="ModifierEtablissement"),
    path('Travail/Comptabilité/ModifierFacture/<int:id>', views.ModifierFacture, name="ModifierFacture"),
    path('Travail/Comptabilité/ModifierBL/<int:id>', views.ModifierBL, name="ModifierBL"),    
    path('Travail/Comptabilité/SupprimerEtablissement/<int:id>', views.SupprimerEtablissement, name='SupprimerEtablissement'),
    path('Travail/Comptabilité/SupprimerFacture/<int:id>', views.SupprimerFacture, name='SupprimerFacture'),
    path('Travail/Comptabilité/SupprimerBL/<int:id>', views.SupprimerBL, name='SupprimerBL'),
    path('Travail/Comptabilité/SupprimerArticleBL/<int:id>', views.SupprimerArticleBL, name='SupprimerArticleBL'),
    path('Travail/Comptabilité/ExportBL/<int:id>', views.ExportBL, name='ExportBL'),
    path('Travail/Comptabilité/ExportFac/<int:id>', views.ExportFac, name='ExportFac'),

]