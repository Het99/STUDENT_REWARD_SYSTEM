# Generated by Django 4.1.3 on 2022-11-21 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srsapp', '0003_instructor'),
    ]

    operations = [
        migrations.CreateModel(
            name='teaches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srsapp.instructor')),
                ('student_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srsapp.student')),
            ],
        ),
    ]
