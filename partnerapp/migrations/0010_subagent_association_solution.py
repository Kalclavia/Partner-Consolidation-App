# Generated by Django 4.0.10 on 2023-06-05 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partnerapp', '0009_remove_solution_oems_remove_solution_use_case_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subagent_association',
            name='solution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='partnerapp.solution'),
        ),
    ]
