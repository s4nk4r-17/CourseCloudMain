# Generated by Django 5.1.5 on 2025-02-10 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0013_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='course_object',
            new_name='course_objects',
        ),
    ]
