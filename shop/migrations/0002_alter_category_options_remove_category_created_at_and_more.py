# Generated by Django 5.2 on 2025-05-24 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='my_order',
        ),
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='category',
            table=None,
        ),
    ]
