# Generated by Django 5.1.1 on 2024-12-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_alter_material_pdf_alter_material_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='pdf',
            field=models.FileField(upload_to='materiais', verbose_name='Material'),
        ),
    ]