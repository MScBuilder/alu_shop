# Generated by Django 4.1 on 2022-09-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construction',
            name='category',
            field=models.CharField(choices=[('FW', 'Fix window'), ('SW', 'Sliding window'), ('CW', 'Casement window')], default='FW', max_length=2),
        ),
        migrations.AlterField(
            model_name='construction',
            name='color',
            field=models.CharField(choices=[('9016', 'White'), ('7016', 'Antracite'), ('9006', 'Silver'), ('9005', 'Black'), ('8017', 'Brown')], default='9016', max_length=4),
        ),
        migrations.AlterField(
            model_name='construction',
            name='height',
            field=models.PositiveIntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='construction',
            name='width',
            field=models.PositiveIntegerField(default=1000),
        ),
    ]