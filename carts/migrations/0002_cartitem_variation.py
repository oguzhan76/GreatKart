# Generated by Django 4.0.3 on 2022-04-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variation',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]