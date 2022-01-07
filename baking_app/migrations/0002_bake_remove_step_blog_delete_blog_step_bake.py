# Generated by Django 4.0 on 2021-12-29 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baking_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_url', models.URLField()),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=150)),
                ('success', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baking_app.category')),
            ],
        ),
        migrations.RemoveField(
            model_name='step',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.AddField(
            model_name='step',
            name='bake',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='baking_app.bake'),
            preserve_default=False,
        ),
    ]
