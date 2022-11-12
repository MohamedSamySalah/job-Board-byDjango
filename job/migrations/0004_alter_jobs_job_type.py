# Generated by Django 4.1.3 on 2022-11-12 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_jobs_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='job_type',
            field=models.CharField(choices=[('FT', 'Fulltime'), ('PT', 'Parttime')], max_length=2),
        ),
    ]
