# Generated by Django 4.1 on 2022-09-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_construction_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construction',
            name='category',
            field=models.CharField(choices=[('SW', 'Sliding window'), ('CW', 'Casement window'), ('FW', 'Fix window')], default='FW', max_length=2),
        ),
        migrations.AlterField(
            model_name='construction',
            name='color',
            field=models.CharField(choices=[('8017', 'Brown'), ('9005', 'Black'), ('9006', 'Silver'), ('9016', 'White'), ('7016', 'Antracite')], default='9016', max_length=4),
        ),
    ]
