# Generated by Django 4.1.3 on 2022-11-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_jobs_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='jobs',
            name='pulished_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jobs',
            name='vecancy',
            field=models.IntegerField(default=1),
        ),
    ]