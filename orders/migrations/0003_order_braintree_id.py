# Generated by Django 4.0.5 on 2022-08-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orderitem_order_alter_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
