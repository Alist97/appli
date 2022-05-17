# Generated by Django 4.0.3 on 2022-04-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_activity_project_subactivity_type_unit_delete_log_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='emsissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_amount', models.CharField(max_length=200)),
                ('emission_factor', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
    ]