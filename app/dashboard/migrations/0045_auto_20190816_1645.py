# Generated by Django 2.2.3 on 2019-08-16 16:45

from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('dashboard', '0044_auto_20190729_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('name', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='profile',
            name='orgs',
            field=models.ManyToManyField(blank=True, to='dashboard.Organization'),
        ),
    ]
