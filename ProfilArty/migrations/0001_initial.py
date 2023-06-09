# Generated by Django 4.0.6 on 2023-05-20 13:54

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/photos/')),
                ('fichier_CV', models.FileField(blank=True, null=True, upload_to='upload/documents/')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='members')),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('poste', models.CharField(max_length=50)),
                ('linkedin_url', models.URLField(blank=True)),
                ('website_url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='portfolio')),
                ('testimonial', models.TextField()),
                ('client_name', models.CharField(max_length=200)),
                ('client_company', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='project_images/')),
                ('results', models.CharField(max_length=100)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('achevé', 'Achevé'), ('en_cours', 'En cours')], max_length=20)),
                ('start_date', models.DateField()),
                ('estimated_end_date', models.DateField()),
                ('completed_steps', models.PositiveIntegerField(default=0)),
                ('remaining_tasks', models.PositiveIntegerField(default=0)),
                ('issues', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('design_graphique', 'Design graphique'), ('production_audiovisuelle', 'Production audiovisuelle'), ('conception_3d', 'Conception 3D')], max_length=100)),
                ('image', models.ImageField(upload_to='services')),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('equipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProfilArty.equipe')),
            ],
        ),
        migrations.AddField(
            model_name='equipe',
            name='Personnel',
            field=models.ManyToManyField(to='ProfilArty.personnel'),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier', models.FileField(upload_to='fichiers/')),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProfilArty.projet')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProfilArty.service')),
            ],
        ),
    ]
