# Generated by Django 3.1.1 on 2020-11-07 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MstTwo', '0001_initial'),
        ('MstOne', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='mainModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_name', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MstOne.mstonemodel')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('item_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_one', to='MstTwo.msttwomodel')),
                ('item_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_two', to='MstTwo.msttwomodel')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]