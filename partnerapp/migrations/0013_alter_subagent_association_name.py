# Generated by Django 4.0.10 on 2023-06-06 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerapp', '0012_alter_subagent_association_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subagent_association',
            name='name',
            field=models.CharField(default='solution.name for use_case.name from subagent.name', max_length=100),
        ),
    ]