# Generated by Django 4.1.7 on 2023-05-07 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_student_register_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_register',
            name='relegion',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
