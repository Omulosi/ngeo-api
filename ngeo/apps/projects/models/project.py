from django.db import models

THEME_CHOICES = (
    ('Business Incubartion', 'BUSINESS INCUBATION'),
    ('Agri-business', 'AGRI-BUSINESS'),
    ('Water & Sanitation', 'WATER-SANITATION'),
)


class Project(models.Model):
    name = models.CharField(max_length=200)
    themes = models.CharField(max_length=50, choices=THEME_CHOICES, default="Agri-Business")