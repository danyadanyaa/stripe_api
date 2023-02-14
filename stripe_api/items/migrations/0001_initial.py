# Generated by Django 3.2.18 on 2023-02-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=250, null=True, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='price')),
                ('currency', models.CharField(choices=[('usd', 'usd'), ('eur', 'eur')], default='usd', max_length=3, verbose_name='currency')),
            ],
        ),
    ]
