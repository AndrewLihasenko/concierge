# Generated by Django 3.0.1 on 2020-01-18 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(help_text='Number of the room')),
                ('maximum_guest', models.IntegerField(blank=True, help_text='Maximum amount of guests for same time', null=True)),
                ('owner', models.CharField(blank=True, help_text='Owner/Tenant of the room', max_length=250, null=True)),
                ('room_status', models.CharField(blank=True, choices=[('FREE', 'Free'), ('BUSY', 'Busy')], max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('guests_cnt', models.IntegerField(blank=True, help_text='How many guests are accepted', null=True)),
                ('is_kept', models.BooleanField(blank=True, help_text='Action type does concierge keep key or not', null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycore.Room')),
            ],
        ),
    ]
