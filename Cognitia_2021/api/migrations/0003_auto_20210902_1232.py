# Generated by Django 3.1.9 on 2021-09-02 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210901_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='event_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_members', to='api.event'),
        ),
    ]