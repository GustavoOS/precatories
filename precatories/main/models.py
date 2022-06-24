from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):
    status = models.CharField(
        max_length=50, null=False, blank=False, default="STATUS")

    def __str__(self):
        return self.status


class LegalAction(models.Model):
    agent = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    process_number = models.CharField(max_length=50)
    defendant = models.CharField(max_length=50)
    execution = models.CharField(max_length=50)
    process_updated_date = models.DateField()
    process_nature = models.CharField(max_length=50)
    attorney = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.id} - process {self.process_number}"


class ActionAuthor(models.Model):
    action = models.ForeignKey(
        LegalAction, on_delete=models.CASCADE, null=True, blank=True)
    release_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    is_deceased = models.BooleanField(default=False)
    cpf = models.BigIntegerField()
    credit = models.DecimalField(max_digits=30, decimal_places=2)
    interest = models.DecimalField(max_digits=30, decimal_places=2)
    base_date = models.DateField(null=True, blank=True)
    ep = models.CharField(max_length=50)
    depre = models.CharField(max_length=50, null=True, blank=True)
    oc = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.action} {self.name}"


class Proposal(models.Model):
    agent = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    updated_value = models.DecimalField(max_digits=30, decimal_places=2)
    proposed_value = models.DecimalField(max_digits=30, decimal_places=2)
    last_contact_date = models.DateField(blank=True, null=True)
    arrenged_return_date = models.DateField(blank=True, null=True)
    prospected_return_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Proposal {self.id}"


class ContactType(models.Model):
    contact_type = models.CharField(max_length=50, default="EMAIL")

    def __str__(self):
        return self.contact_type


class ProposalContact(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    contact_type = models.ForeignKey(
        ContactType, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.proposal} - {self.contact} - {self.contact_type}"


class AuthorProposal(models.Model):
    author = models.ForeignKey(ActionAuthor, on_delete=models.CASCADE)
    proposal = models.ForeignKey(
        Proposal, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.author}; {self.proposal}"
