# Generated by Django 4.1.3 on 2022-11-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='job_type',
            field=models.CharField(choices=[('FT', 'Fulltime'), ('PT', 'Parttime')], default='FT', max_length=2),
        ),
    ]