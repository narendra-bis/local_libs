# Generated by Django 2.2.24 on 2021-06-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dreamreal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField()),
            ],
            options={
                'db_table': 'dreamreal',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organisation', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('roll_number', models.IntegerField(help_text='please use your roll number')),
                ('place', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organisation', models.CharField(max_length=100)),
                ('teacherid', models.CharField(help_text='use your id', max_length=50)),
                ('username', models.CharField(help_text='please use username', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'mytest',
            },
        ),
    ]
