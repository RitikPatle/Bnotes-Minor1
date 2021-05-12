# Generated by Django 2.2.3 on 2019-10-02 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('icon', models.ImageField(upload_to='pics')),
                ('ref', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('icon', models.ImageField(upload_to='pics')),
                ('ref', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(max_length=100)),
                ('stream', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(max_length=100)),
                ('stream', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='')),
            ],
        ),
    ]