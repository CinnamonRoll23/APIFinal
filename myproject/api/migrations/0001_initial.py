# Generated by Django 5.1.2 on 2024-12-10 16:16

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PROCESSED', 'Processed'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=24, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('cartItemID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('orderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='api.user'),
        ),
    ]
