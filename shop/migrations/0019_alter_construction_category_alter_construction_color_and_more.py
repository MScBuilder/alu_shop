# Generated by Django 4.1 on 2022-09-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_alter_construction_category_alter_construction_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construction',
            name='category',
            field=models.CharField(choices=[('SW', 'Sliding window'), ('FW', 'Fix window'), ('CW', 'Casement window')], default='FW', max_length=2),
        ),
        migrations.AlterField(
            model_name='construction',
            name='color',
            field=models.CharField(choices=[('9005', 'Black'), ('8017', 'Brown'), ('9016', 'White'), ('9006', 'Silver'), ('7016', 'Antracite')], default='9016', max_length=4),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
