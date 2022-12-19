# Generated by Django 4.1.3 on 2022-12-19 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
        ('additional_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closed', models.BooleanField(default=False)),
                ('contract_number', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('amount', models.FloatField(default=0.0)),
                ('payment_due', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='persons.client')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Forthcoming'), (2, 'In progress'), (3, 'Finished')])),
                ('start_event', models.DateTimeField()),
                ('end_event', models.DateTimeField()),
                ('attendees', models.PositiveSmallIntegerField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('id_contract', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.contract')),
                ('id_employee_support', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='persons.supportteamemployee')),
                ('id_location', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='additional_data.location')),
            ],
        ),
    ]