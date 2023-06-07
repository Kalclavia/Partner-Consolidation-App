from django.db import models

class PrimaryPartner(models.Model):
    name = models.CharField(max_length=100, help_text='Enter the primary partner name')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    # other fields related to Primary Partner

class Subagent(models.Model):
    name = models.CharField(max_length=100)
    primary_partner = models.ForeignKey(PrimaryPartner, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    # other fields related to Solution

    # other fields related to Subagent

class Subagent_Association(models.Model):
    subagent = models.ForeignKey(Subagent, on_delete=models.SET_NULL, null = True)
    use_case = models.ForeignKey('UseCase', on_delete=models.SET_NULL, null = True)
    solution = models.ForeignKey('Solution', on_delete=models.SET_NULL, null = True)
    oems = models.ManyToManyField('OEM', help_text='Specify one or many OEMs for this solution')    
    verticals = models.ManyToManyField('VerticalSector', help_text='Specify one or many Verticals for this solution')
    name = models.CharField(max_length=100, default = "Leave This Blank")
    def __str__(self):
        self.name = "{} for {} from {}".format(self.solution.name, self.use_case.name, self.subagent.name)    
        """String for representing the Model object."""
        return self.name

class UseCase(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    # other fields related to Use Case

class Solution(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    # other fields related to Solution

class OEM(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    # other fields related to OEM

class VerticalSector(models.Model):
    Sectors = (
        ('Transportation & Logistics','Transportation & Logistics'),
        ('Police/Fire','Police/Fire'),
        ('K-12','K-12'),
        ('Higher Ed','Higher Ed'),
        ('Financial Services','Financial Services'),
        ('Municipalities','Municipalities'),
        ('Retail','Retail'),
        ('Tech, Media, & Services','Tech, Media, & Services'),
        ('Logistics','Logistics'),
        ('Oil, Gas & Utility','Oil, Gas & Utility'),
        ('Healthcare','Healthcare')
    )

    name = models.CharField(max_length=100, choices=Sectors, blank=False, help_text="Vertical Sector")
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    # other fields related to Vertical Sector
