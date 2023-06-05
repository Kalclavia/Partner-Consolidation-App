from django.db import models

class VerticalSector(models.Model):
    name = models.CharField(max_length=100)
    # other fields related to Vertical Sector

class PrimaryPartner(models.Model):
  name = models.CharField(max_length=100)
  vertical_sectors = models.ManyToManyField(VerticalSector)
    # other fields related to Primary Partner

class Subagent(models.Model):
    primary_partner = models.ForeignKey(PrimaryPartner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # other fields related to Subagent

class UseCase(models.Model):
    subagent = models.ForeignKey(Subagent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # other fields related to Use Case

class Solution(models.Model):
    name = models.CharField(max_length=100)
    associations = models.ManyToManyField('SolutionAssociation', related_name='solutions')
    # other fields related to Solution

class OEM(models.Model):
    name = models.CharField(max_length=100)
    associations = models.ManyToManyField('OEMAssociation', related_name='oems')
    # other fields related to OEM

class SolutionAssociation(models.Model):
    subagent = models.ForeignKey(Subagent, on_delete=models.CASCADE)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
    use_case = models.ForeignKey(UseCase, on_delete=models.CASCADE)
    # other fields related to Solution Association

class OEMAssociation(models.Model):
    subagent = models.ForeignKey(Subagent, on_delete=models.CASCADE)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
    oem = models.ForeignKey(OEM, on_delete=models.CASCADE)
    # other fields related to OEM Association

class Partner(models.Model):
    primary_partner = models.ForeignKey(PrimaryPartner, on_delete=models.CASCADE)
    subagents = models.ManyToManyField(Subagent, through='PartnerSubagent')
    # other fields related to Partner

class PartnerSubagent(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    subagent = models.ForeignKey(Subagent, on_delete=models.CASCADE)
    # other fields related to Partner-Subagent association