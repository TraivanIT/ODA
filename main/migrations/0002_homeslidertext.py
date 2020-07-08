# Generated by Django 3.0.2 on 2020-07-06 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSliderText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_slider_text', models.TextField()),
                ('home_slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.HomeSlider')),
            ],
        ),
    ]