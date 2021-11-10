# Generated by Django 3.2.8 on 2021-11-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='authors_img', verbose_name='Photo of the author')),
                ('background_photo', models.ImageField(blank=True, null=True, upload_to='authors_back_img', verbose_name='background photo of the profile author')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name="Author's description")),
                ('big_description', models.TextField(blank=True, null=True, verbose_name='big description')),
                ('nationality', models.CharField(blank=True, choices=[('VEN', 'Venezolano/a'), ('ESP', 'Español/a'), ('POR', 'Portugues/a'), ('COL', 'Colombiano/a'), ('PER', 'Peruano/a'), ('MEX', 'Mexicano/a'), ('CHI', 'Chileno/a'), ('ARG', 'Argentino/a'), ('000', 'Otro')], max_length=3, null=True, verbose_name="Author's nationality")),
                ('sex', models.CharField(blank=True, choices=[('HOM', 'Hombre'), ('MUJ', 'Mujer'), ('PLA', 'Plátano'), ('000', 'Otro')], max_length=3, null=True, verbose_name='Gender')),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autors',
            },
        ),
    ]
