# Generated by Django 3.0.2 on 2020-07-06 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_homeslidertext'),
    ]

    operations = [
        migrations.CreateModel(
            name='KidsDream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='kidsdream/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KidsDreamTextSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kids_dream_text_slider', models.TextField()),
                ('kide_dream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.KidsDream')),
            ],
        ),
    ]