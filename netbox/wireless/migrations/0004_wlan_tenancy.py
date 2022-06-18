# Generated by Django 4.0.4 on 2022-06-18 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0007_contact_link'),
        ('wireless', '0003_created_datetimefield'),
    ]

    operations = [
        migrations.AddField(
            model_name='wirelesslan',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='wireless_lans', to='tenancy.tenant'),
        ),
    ]
