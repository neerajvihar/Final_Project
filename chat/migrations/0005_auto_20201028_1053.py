# Generated by Django 2.2.1 on 2020-10-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_nurse_patient_volunteer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AddField(
            model_name='patient',
            name='pat_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
