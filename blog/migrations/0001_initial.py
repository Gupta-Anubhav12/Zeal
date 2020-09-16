# Generated by Django 2.1.15 on 2020-08-15 16:37

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', tinymce.models.HTMLField()),
                ('author', models.CharField(max_length=20)),
                ('trends', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=128)),
                ('category', models.CharField(max_length=20)),
                ('images', models.ImageField(default='', upload_to='images/blog')),
            ],
        ),
    ]
