# Generated by Django 5.0.1 on 2024-01-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vfn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200, null=True)),
                ('email', models.IntegerField()),
                ('phone', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('conform_password', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
