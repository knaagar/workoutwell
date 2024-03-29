# Generated by Django 4.2.6 on 2023-10-11 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0002_goals'),
    ]

    operations = [
        migrations.CreateModel(
            name='exercise_tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=50)),
                ('edesc', models.TextField()),
                ('etag', models.CharField(max_length=20)),
                ('created_at', models.DateField()),
                ('priority', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
