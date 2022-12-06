# Generated by Django 2.2.3 on 2022-12-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('image', models.ImageField(upload_to='products/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
