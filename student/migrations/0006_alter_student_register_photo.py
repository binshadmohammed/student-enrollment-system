# Generated by Django 4.1.7 on 2023-05-06 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_student_register_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_register',
            name='photo',
            field=models.ImageField(max_length=200, upload_to=''),
        ),
    ]
