# Generated by Django 4.1.7 on 2023-05-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_register_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_register',
            name='guardianmobile',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student_register',
            name='hsspassoutyear',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student_register',
            name='hsspersentage',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student_register',
            name='sslcpassoutyear',
            field=models.CharField(max_length=200),
        ),
    ]
