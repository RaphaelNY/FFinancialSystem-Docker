# Generated by Django 3.1.4 on 2024-09-01 13:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_account_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_occurrence', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('currency', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.currency')),
                ('from_account', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_account', to='accounting.account')),
                ('to_account', models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_account', to='accounting.account')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.normaluser')),
            ],
            options={
                'ordering': ['-time_of_occurrence'],
            },
        ),
    ]
