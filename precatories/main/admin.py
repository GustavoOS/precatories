from django.contrib import admin
from .models import *

# Register your models here.
for model in [LegalAction, Proposal, ProposalContact,
              ActionAuthor, Status, ContactType,
              AuthorProposal, UserRole]:
    admin.site.register(model)
