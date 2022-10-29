# Generated by Django 4.1.2 on 2022-10-13 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('alias', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TelegramLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=191)),
                ('login', models.CharField(max_length=191)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_photo', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('short_text', models.TextField()),
                ('content', models.TextField()),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('main_news', models.DateTimeField(blank=True, null=True)),
                ('slug', models.CharField(max_length=255)),
                ('date_of_event', models.DateTimeField(blank=True, null=True)),
                ('organizer', models.CharField(blank=True, max_length=255, null=True)),
                ('place', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField()),
                ('view_count', models.IntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parser.category')),
            ],
        ),
    ]