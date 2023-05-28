from django.db import models
from django.contrib.auth.models import User
class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio')
    testimonial = models.TextField()
    client_name = models.CharField(max_length=200)
    client_company = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

        
class CustomUser(User):
    telephone = models.CharField(max_length=20,null=True, blank=True)
    image=models.ImageField(upload_to='upload/photos/',null=True, blank=True)
    fichier_CV = models.FileField(upload_to='upload/documents/',null=True, blank=True)
        


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=[
        ('design_graphique', 'Design graphique'),
        ('production_audiovisuelle', 'Production audiovisuelle'),
        ('conception_3d', 'Conception 3D'),
    ])
    image = models.ImageField(upload_to='services')
  

    def __str__(self):
        return self.title    
class Personnel(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    poste = models.CharField(max_length=50) 
    linkedin_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.poste})"
class equipe(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='members')
    bio = models.TextField()
    Personnel = models.ManyToManyField(Personnel)


    
    def __str__(self):
        return self.name
class Projet(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    equipe = models.ForeignKey(equipe, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom

    
class Detail(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    fichier = models.FileField(upload_to='fichiers/')
    
    def __str__(self):
        return f"{self.projet} - {self.service}"


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    results = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=(('achevé', 'Achevé'), ('en_cours', 'En cours')))
    start_date = models.DateField(null=True)
    estimated_end_date = models.DateField(null=True)
    completed_steps = models.PositiveIntegerField(default=0)
    remaining_tasks = models.PositiveIntegerField(default=0)
    issues = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
