# Generated by Django 5.0.7 on 2024-07-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_product_categories_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='method',
            field=models.CharField(choices=[('QR', 'BY QR'), ('CREDIT', 'BY CREDIT')], max_length=6),
        ),
    ]
