# Generated by Django 4.2 on 2024-11-27 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gofinalapp', '0005_user_rename_email_contact_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]
