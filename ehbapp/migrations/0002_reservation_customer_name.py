# Generated by Django 3.0.5 on 2020-04-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehbapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='Customer_Name',
            field=models.CharField(blank=True, default=' ', max_length=50, null=True),
        ),
    ]
