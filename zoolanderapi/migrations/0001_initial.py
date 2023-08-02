# Generated by Django 4.1.3 on 2023-08-02 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='studentClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoolanderapi.classroom')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoolanderapi.student')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoolanderapi.user'),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoolanderapi.classroom')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoolanderapi.user')),
            ],
        ),
    ]