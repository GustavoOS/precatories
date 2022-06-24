# Generated by Django 4.0.5 on 2022-06-24 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('is_deceased', models.BooleanField(default=False)),
                ('cpf', models.BigIntegerField()),
                ('credit', models.DecimalField(decimal_places=2, max_digits=30)),
                ('interest', models.DecimalField(decimal_places=2, max_digits=30)),
                ('base_date', models.DateField(blank=True, null=True)),
                ('ep', models.CharField(max_length=50)),
                ('depre', models.CharField(blank=True, max_length=50, null=True)),
                ('oc', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(default='EMAIL', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_value', models.DecimalField(decimal_places=2, max_digits=30)),
                ('proposed_value', models.DecimalField(decimal_places=2, max_digits=30)),
                ('last_contact_date', models.DateField(blank=True, null=True)),
                ('arrenged_return_date', models.DateField(blank=True, null=True)),
                ('prospected_return_date', models.DateField(blank=True, null=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='STATUS', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.PositiveSmallIntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProposalContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=50)),
                ('contact_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.contacttype')),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.proposal')),
            ],
        ),
        migrations.AddField(
            model_name='proposal',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.status'),
        ),
        migrations.CreateModel(
            name='LegalAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_number', models.CharField(max_length=50)),
                ('defendant', models.CharField(max_length=50)),
                ('execution', models.CharField(max_length=50)),
                ('process_updated_date', models.DateField()),
                ('process_nature', models.CharField(max_length=50)),
                ('attorney', models.CharField(max_length=100)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorProposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.actionauthor')),
                ('proposal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.proposal')),
            ],
        ),
        migrations.AddField(
            model_name='actionauthor',
            name='action',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.legalaction'),
        ),
        migrations.AddIndex(
            model_name='userrole',
            index=models.Index(fields=['user'], name='main_userro_user_id_3368c1_idx'),
        ),
        migrations.AddIndex(
            model_name='proposal',
            index=models.Index(fields=['agent'], name='main_propos_agent_i_f0026c_idx'),
        ),
        migrations.AddIndex(
            model_name='authorproposal',
            index=models.Index(fields=['author'], name='main_author_author__6e3873_idx'),
        ),
    ]
