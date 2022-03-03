# Generated by Django 2.2.12 on 2022-03-03 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='skill_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='first_model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_Name', models.CharField(max_length=50)),
                ('user_Address', models.CharField(max_length=100)),
                ('user_Age', models.IntegerField()),
                ('Date_Of_birth', models.DateField()),
                ('skills', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='new_pjt_app.skill_table')),
            ],
        ),
    ]
