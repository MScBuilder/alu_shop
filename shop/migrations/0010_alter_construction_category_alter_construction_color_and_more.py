# Generated by Django 4.1 on 2022-08-28 18:38

from django.db import migrations, models
import django.db.models.deletion


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
            field=models.CharField(choices=[('9005', 'Black'), ('7016', 'Antracite'), ('9016', 'White'), ('9006', 'Silver'), ('8017', 'Brown')], default='9016', max_length=4),
        ),
        migrations.CreateModel(
            name='Qutation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('construction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.construction')),
            ],
        ),
    ]