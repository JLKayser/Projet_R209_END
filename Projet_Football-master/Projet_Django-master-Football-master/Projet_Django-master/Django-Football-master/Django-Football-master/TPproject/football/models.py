from django.db import models

class Club(models.Model):
    nom_club = models.CharField(max_length=100)
    pays_club = models.CharField(max_length = 100)
    date_parution_club = models.DateField(blank = True, null = True)
    nombre_LDC = models.IntegerField(blank = False)
    resume = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"{self.nom_club}"
        return chaine

    def dico(self):
        return {"nom_club": self.nom_club, "pays_club": self.pays_club,"date_parution_club":self.date_parution_club,"nombre_LDC": self.nombre_LDC,"resume": self.resume}

class Joueur(models.Model):
    nom_joueur = models.CharField(max_length=100)
    pays_joueur = models.CharField(max_length=100)
    date_naissance_joueur = models.DateField(blank=True, null=True)
    nombre_LDC = models.IntegerField(blank=False)
    resume = models.TextField(null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE,default= None, null=True)

    def __str__(self):
        chaine = f"{self.nom_joueur}"
        return chaine

    def dico(self):
        return {"nom_joueur": self.nom_joueur, "pays_joueur": self.pays_joueur,"date_naissance_joueur":self.date_naissance_joueur,"nombre_LDC": self.nombre_LDC,"resume": self.resume,"club":self.club}