# Generated by Django 5.1.6 on 2025-03-27 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0006_consulta'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='confirmada',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='id_medico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.medico'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='id_paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.paciente'),
        ),
    ]
