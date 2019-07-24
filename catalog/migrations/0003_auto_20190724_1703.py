# Generated by Django 2.2.2 on 2019-07-24 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190724_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment_record',
            name='medication',
        ),
        migrations.AddField(
            model_name='medication',
            name='treatment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Treatment_record'),
        ),
    ]
