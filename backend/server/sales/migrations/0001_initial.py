# Generated by Django 3.0.8 on 2020-07-17 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('hire_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField()),
                ('volume', models.DecimalField(decimal_places=2, max_digits=11)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Agents')),
            ],
        ),
    ]
