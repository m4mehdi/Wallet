# Generated by Django 4.1.2 on 2022-10-28 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(blank=True, default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('amount', models.IntegerField(default=0)),
                ('user_id', models.BigIntegerField()),
                ('transactiontype', models.CharField(choices=[('Refound', '12'), ('Transfer', '13'), ('Order', '14'), ('Deduction', '15')], default='Transfer', max_length=20)),
                ('transactiondate', models.DateTimeField()),
                ('reference_id', models.CharField(max_length=15)),
            ],
        ),
    ]
