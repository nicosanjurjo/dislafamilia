# Generated by Django 5.0.7 on 2024-08-30 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_pedidoproducto_pedido_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidoproducto',
            name='precio_unitario',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
