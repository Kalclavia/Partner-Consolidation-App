# Generated by Django 3.2.13 on 2023-06-01 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partnerapp', '0005_auto_20230601_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='OEM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('vertical_sectors', models.ManyToManyField(to='partnerapp.VerticalSector')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subagent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('primary_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partnerapp.primarypartner')),
            ],
        ),
        migrations.RemoveField(
            model_name='partner',
            name='oem',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='solution',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='subagent',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='use_case',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='vertical_sectors',
        ),
        migrations.CreateModel(
            name='UseCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subagent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partnerapp.subagent')),
            ],
        ),
        migrations.CreateModel(
            name='SolutionAssociation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partnerapp.solution')),
                ('subagent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partnerapp.subagent')),
                ('use_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partnerapp.usecase')),
            ],
        ),
        migrations.AddField(
            model_name='solution',
            name='associations',
            field=models.ManyToManyField(related_name='solutions', to='partnerapp.SolutionAssociation'),
        ),
        migrations.CreateModel(
            name='PartnerSubagent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partnerapp.partner')),
                ('subagent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partnerapp.subagent')),
            ],
        ),
        migrations.CreateModel(
            name='OEMAssociation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partnerapp.oem')),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partnerapp.solution')),
                ('subagent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partnerapp.subagent')),
            ],
        ),
        migrations.AddField(
            model_name='oem',
            name='associations',
            field=models.ManyToManyField(related_name='oems', to='partnerapp.OEMAssociation'),
        ),
        migrations.AddField(
            model_name='partner',
            name='subagents',
            field=models.ManyToManyField(through='partnerapp.PartnerSubagent', to='partnerapp.Subagent'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='primary_partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partnerapp.primarypartner'),
        ),
    ]
