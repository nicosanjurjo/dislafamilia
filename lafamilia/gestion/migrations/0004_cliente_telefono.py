# Generated by Django 5.0.7 on 2024-09-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_pedidoproducto_precio_unitario'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
    ]
