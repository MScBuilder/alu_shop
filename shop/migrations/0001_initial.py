# Generated by Django 4.1 on 2022-08-29 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shop.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Construction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('CW', 'Casement window'), ('FW', 'Fix window'), ('SW', 'Sliding window')], default='FW', max_length=2)),
                ('reference_name', models.CharField(max_length=100)),
                ('width', models.PositiveIntegerField(default=1000, validators=[shop.validators.width_validator])),
                ('height', models.PositiveIntegerField(default=1000, validators=[shop.validators.height_validator])),
                ('price', models.FloatField()),
                ('color', models.CharField(choices=[('9016', 'White'), ('9006', 'Silver'), ('8017', 'Brown'), ('7016', 'Antracite'), ('9005', 'Black')], default='9016', max_length=4)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.construction')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='shop.orderitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
