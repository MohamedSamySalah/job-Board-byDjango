# Generated by Django 4.1.3 on 2022-11-12 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_jobs_experience_jobs_pulished_at_jobs_salary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='salary',
            field=models.DecimalField(decimal_places=3, default=1.1, max_digits=8),
        ),
    ]
