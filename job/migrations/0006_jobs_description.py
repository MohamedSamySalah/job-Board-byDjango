# Generated by Django 4.1.3 on 2022-11-12 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_alter_jobs_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='description',
            field=models.TextField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
