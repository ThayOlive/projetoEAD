# Generated by Django 5.1.1 on 2024-12-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_alter_material_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='pdf',
            field=models.FileField(upload_to='', verbose_name='Material'),
        ),
    ]