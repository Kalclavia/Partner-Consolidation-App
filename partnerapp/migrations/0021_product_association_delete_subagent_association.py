# Generated by Django 4.0.10 on 2023-06-07 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partnerapp', '0020_subagent_association_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Association',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Leave This Blank', max_length=100)),
                ('oems', models.ManyToManyField(help_text='Specify one or many OEMs for this solution', to='partnerapp.oem')),
                ('solution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='partnerapp.solution')),
                ('subagent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='partnerapp.subagent')),
                ('use_case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='partnerapp.usecase')),
                ('verticals', models.ManyToManyField(help_text='Specify one or many Verticals for this solution', to='partnerapp.verticalsector')),
            ],
        ),
        migrations.DeleteModel(
            name='Subagent_Association',
        ),
    ]
