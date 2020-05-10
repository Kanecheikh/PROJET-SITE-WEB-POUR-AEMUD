from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Membre(User):
    GENRE = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    niv_etu = models.CharField("niveau d'étude", max_length=30)
    filiere = models.CharField("filière", max_length=30)
    genre = models.CharField('genre', max_length=1, choices=GENRE)

    def __str__(self):
        return self.username
    

    class Meta:
        verbose_name = 'membre'
        verbose_name_plural = 'membres'
    


class Secretaire(User):

    def __str__(self):
        return self.username
    
    
    class Meta:
        verbose_name = 'secrétaire',
        verbose_name_plural = 'secrétaires'


class GroupeMembre(models.Model):
    nom_gpe = models.CharField("nom du groupe", max_length=30)
    membres = models.ManyToManyField(Membre, through="MembreAdhesion")

    def __str__(self):
        return self.nom_gpe


class MembreAdhesion(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    groupe = models.ForeignKey(GroupeMembre, on_delete=models.CASCADE)
    date_adhesion = models.DateTimeField("date d'adhésion", default=timezone.now)
