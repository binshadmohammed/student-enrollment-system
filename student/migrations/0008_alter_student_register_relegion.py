# Generated by Django 4.1.7 on 2023-05-08 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_student_register_relegion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_register',
            name='relegion',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]