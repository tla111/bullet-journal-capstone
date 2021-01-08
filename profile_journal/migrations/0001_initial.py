# Generated by Django 3.1.5 on 2021-01-08 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReflectionPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True, default=None, null=True)),
                ('submission_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('name_post', models.BooleanField(choices=[(True, 'Morning Reflection'), (False, 'Evening Reflection')])),
                ('reflection_user_created', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reflection_created_by_bulletjournaluser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('date_filed', models.DateTimeField(default=django.utils.timezone.now)),
                ('assignment_type', models.CharField(choices=[('New', 'New'), ('Lesson', 'Lesson'), ('Activity', 'Activity'), ('Quiz', 'Quiz'), ('Assessment', 'Assessment'), ('Completed', 'Completed')], max_length=200)),
                ('user_created', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_bulletjournaluser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
