# Generated by Django 4.2.6 on 2023-10-10 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name_en', models.CharField(max_length=100)),
                ('name_th', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name_en', models.CharField(max_length=100)),
                ('name_th', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Subdistrict',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name_en', models.CharField(max_length=100)),
                ('name_th', models.CharField(max_length=100)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subdistricts', to='thailand_geography.district')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='thailand_geography.province'),
        ),
    ]