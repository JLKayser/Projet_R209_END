from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ClubForm, JoueurForm , Joueur_ajoutForm

from . import  models

def ajout(request):
    if request.method == "POST":
        form = ClubForm(request)
        if form.is_valid():
            club = form.save()
            return HttpResponseRedirect("/football/")
        else:
            return render(request,"football/ajout.html",{"form": form})
    else:
        form = ClubForm()
        return render(request,"football/ajout.html",{"form" : form})

def ajout2(request):
    if request.method == "POST":
        form = JoueurForm(request)
        if form.is_valid():
            joueur = form.save()
            return HttpResponseRedirect("/football/")
        else:
            return render(request,"football/ajout2.html",{"form": form})
    else:
        form = JoueurForm()
        return render(request,"football/ajout2.html",{"form": form})

def ajout3(request,id):

        form = Joueur_ajoutForm()
        return render(request,"football/ajout3.html",{"form": form,"id":id})

def traitement(request):
    cform = ClubForm(request.POST)
    if cform.is_valid():
        club = cform.save()
        return HttpResponseRedirect("/football/")
    else:
        return render(request,"football/ajout.html",{"form": cform})

def traitement2(request):
    jform = JoueurForm(request.POST)
    if jform.is_valid():
        club = jform.save()
        return HttpResponseRedirect("/football/")
    else:
        return render(request,"football/ajout2.html",{"form": jform})

def traitement3(request , id):
    aform = Joueur_ajoutForm(request.POST)
    club= models.Club.objects.get(pk=id)
    if aform.is_valid():
        joueur_ajout = aform.save(commit=False)
        joueur_ajout.club_id = id
        joueur_ajout.club = club
        joueur_ajout.save()
        return HttpResponseRedirect(f"/football/affiche/{id}/")
    else:
        return render(request, "football/ajout3.html", {"form": aform, "id": id})

def main(request):
    club = list(models.Club.objects.all())
    return render(request, 'football/home.html', {'liste': club})


def affiche(request, id):
    club = models.Club.objects.get(pk=id)
    joueur = list(models.Joueur.objects.filter(club_id=id))
    return render(request,"football/affiche.html",{"club": club,"joueur": joueur})

def delete(request, id):
    club = models.Club.objects.get(pk=id)
    club.delete()
    return HttpResponseRedirect("/football/")

def delete2(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    joueur.delete()
    return HttpResponseRedirect("/football/affiche/" + str(joueur.club_id) + "/")


def update(request, id):
    club = models.Club.objects.get(pk=id)
    cform = ClubForm(club.dico())
    return render(request, "football/update.html", {"form": cform, "id": id})

def update2(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    jform = JoueurForm(joueur.dico())
    return render(request, "football/update2.html ", {"form": jform, "id": id})

def traitementupdate(request, id):
    cform = ClubForm(request.POST)
    if cform.is_valid():
        club = cform.save(commit=False)
        club.id = id
        club.save()
        return HttpResponseRedirect("/football")
    else:
        return render(request, "football/update.html", {"form": cform, "id": id})

def traitementupdate2(request, id):
    jform = JoueurForm(request.POST)
    if jform.is_valid():
        joueur = jform.save(commit=False)
        joueur.id = id
        joueur.save()
        return HttpResponseRedirect("/football")
    else:
        return render(request, "football/update2.html", {"form": jform, "id": id})

def traitementupdate3(request, id):
    aform = JoueurForm(request.POST)
    if aform.is_valid():
        joueur_ajout = aform.save(commit=False)
        joueur_ajout.id = id
        joueur_ajout.save()
        return HttpResponseRedirect("/football")
    else:
        return render(request, "football/update3.html", {"form": aform, "id": id})