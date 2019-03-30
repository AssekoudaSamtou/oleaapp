from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Eleve(models.Model):
	nom = models.CharField(max_length=100)
	prenom = models.CharField(max_length=42)
	sexe = models.BooleanField(verbose_name="Produit publié ?", default=True)
	annee_admission = models.CharField(max_length=4)
	semestrefiliere = models.ForeignKey('SemestreFiliere', on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.nom} {self.prenom}"

class SemestreFiliere(models.Model):
	libelle = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.libelle}"

class Matiere(models.Model):
	code = models.CharField(max_length=10, null=True)
	libelle = models.CharField(max_length=100)
	filieres = models.ManyToManyField(SemestreFiliere, through='CoursSemestreFiliere', related_name='cours', verbose_name="filieres suivant le cours")

	def __str__(self):
		return f"{self.code} {self.libelle}"

class Enseignant(User):
	# nom = models.CharField(max_length=100)
	# prenom = models.CharField(max_length=42)
	numero = models.CharField(max_length=42)
	cours = models.ManyToManyField(Matiere, through='DispenserCours', related_name='titulaire', verbose_name="Cours")
	signature = models.ImageField(upload_to="signature/", null=True)

	class Meta:
		verbose_name = "Enseignant"

	def __str__(self):
		return f"{self.numero}"

class Salle(models.Model):
	libelle = models.CharField(max_length=100)
	situation = models.CharField(max_length=5, null=True)

	def __str__(self):
		return f"{self.libelle} au {self.situation}"

class DispenserCours(models.Model):
	matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
	enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
	salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
	date = models.DateField(null=True, verbose_name="Jour du cours")
	heure_arrivee = models.DateField(null=True)
	heure_depart = models.DateField(null=True)

	def __str__(self):
		return f"{self.enseignant} à dispensé le cours {self.matiere}"

class Presence(models.Model):
	eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
	cours = models.ForeignKey(DispenserCours, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.eleve} est present(e) au cours {self.cours}"

class CoursSemestreFiliere(models.Model):
	cours = models.ForeignKey(Matiere, on_delete=models.CASCADE)
	semestrefiliere = models.ForeignKey(SemestreFiliere, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.cours} Pour {self.semestrefiliere}"
