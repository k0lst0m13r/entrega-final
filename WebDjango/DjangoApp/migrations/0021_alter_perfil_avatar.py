# Generated by Django 3.2.14 on 2022-07-19 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0020_alter_perfil_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile_images'),
        ),
    ]
