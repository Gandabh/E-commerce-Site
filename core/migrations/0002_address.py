# Generated by Django 3.2.4 on 2021-08-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='address')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('phone', models.CharField(max_length=13, verbose_name='Phone number')),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
