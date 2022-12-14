# Generated by Django 4.1.3 on 2022-12-04 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_jobs_slug_alter_jobs_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apllyjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=60)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='files/')),
                ('cover_letter', models.TextField(max_length=255)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.jobs')),
            ],
        ),
    ]
