# Generated by Django 5.1.6 on 2025-03-18 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_medico_especialidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='especialidade',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.especialidade'),
        ),
    ]
