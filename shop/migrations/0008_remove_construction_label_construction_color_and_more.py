# Generated by Django 4.1 on 2022-08-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_construction_category_alter_construction_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='construction',
            name='label',
        ),
        migrations.AddField(
            model_name='construction',
            name='color',
            field=models.CharField(choices=[('9005', 'Black'), ('7016', 'Anthracite'), ('9016', 'White'), ('8017', 'Brown'), ('9006', 'Silver')], default='9016', max_length=4),
        ),
        migrations.AlterField(
            model_name='construction',
            name='category',
            field=models.CharField(choices=[('CW', 'Casement window'), ('SW', 'Sliding window'), ('FW', 'Fix window')], default='FW', max_length=2),
        ),
    ]