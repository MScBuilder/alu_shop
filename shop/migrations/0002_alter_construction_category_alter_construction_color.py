# Generated by Django 4.1 on 2022-08-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construction',
            name='category',
            field=models.CharField(choices=[('FW', 'Fix window'), ('CW', 'Casement window'), ('SW', 'Sliding window')], default='FW', max_length=2),
        ),
        migrations.AlterField(
            model_name='construction',
            name='color',
            field=models.CharField(choices=[('9016', 'White'), ('7016', 'Antracite'), ('9005', 'Black'), ('8017', 'Brown'), ('9006', 'Silver')], default='9016', max_length=4),
        ),
    ]