# Generated by Django 3.2.4 on 2021-08-09 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_slide_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slogan1',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='slogan part 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='slogan2',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='slogan part 1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slide_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='slide image'),
        ),
    ]
