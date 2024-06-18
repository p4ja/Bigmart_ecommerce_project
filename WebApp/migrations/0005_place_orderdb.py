# Generated by Django 5.0.4 on 2024-06-08 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_cart_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='place_orderdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('bill', models.TextField(blank=True, null=True)),
            ],
        ),
    ]