# Generated by Django 4.0.10 on 2023-06-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerapp', '0011_subagent_association_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subagent_association',
            name='name',
            field=models.CharField(default='None for None from None', max_length=100),
        ),
    ]