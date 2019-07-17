# Generated by Django 2.2.2 on 2019-07-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20190717_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='height',
            field=models.PositiveIntegerField(default=180, help_text='輸入病人身高(cm)'),
        ),
        migrations.AddField(
            model_name='patient',
            name='weight',
            field=models.PositiveIntegerField(default=70, help_text='輸入病人體重(kg)'),
        ),
    ]
