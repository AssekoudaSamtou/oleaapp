# Generated by Django 2.1.5 on 2019-03-29 21:22

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursSemestreFiliere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DispenserCours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Jour du cours')),
                ('heure_arrivee', models.DateField(null=True)),
                ('heure_depart', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=42)),
                ('sexe', models.BooleanField(default=True, verbose_name='Produit publié ?')),
                ('annee_admission', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('numero', models.CharField(max_length=42)),
                ('signature', models.ImageField(null=True, upload_to='signature/')),
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
            name='Matiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='presence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oleaapp.DispenserCours')),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oleaapp.Eleve')),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SemestreFiliere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='matiere',
            name='filieres',
            field=models.ManyToManyField(related_name='cours', through='oleaapp.CoursSemestreFiliere', to='oleaapp.SemestreFiliere', verbose_name='filieres suivant le cours'),
        ),
        migrations.AddField(
            model_name='enseignant',
            name='cours',
            field=models.ManyToManyField(related_name='titulaire', through='oleaapp.DispenserCours', to='oleaapp.Matiere', verbose_name='Cours'),
        ),
        migrations.AddField(
            model_name='eleve',
            name='semestrefiliere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oleaapp.SemestreFiliere'),
        ),
        migrations.AddField(
            model_name='dispensercours',
            name='enseignant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oleaapp.Enseignant'),
        ),
        migrations.AddField(
            model_name='dispensercours',
            name='matiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oleaapp.Matiere'),
        ),
        migrations.AddField(
            model_name='dispensercours',
            name='salle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oleaapp.Salle'),
        ),
        migrations.AddField(
            model_name='courssemestrefiliere',
            name='cours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oleaapp.Matiere'),
        ),
        migrations.AddField(
            model_name='courssemestrefiliere',
            name='semestrefiliere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oleaapp.SemestreFiliere'),
        ),
    ]