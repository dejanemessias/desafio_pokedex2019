# Generated by Django 2.2 on 2019-04-26 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Habilidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição/Sobre')),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.FileField(upload_to='fotos/')),
                ('nome', models.CharField(max_length=120)),
                ('altura', models.FloatField()),
                ('ponto_saude', models.PositiveIntegerField()),
                ('ataque', models.PositiveIntegerField()),
                ('defesa', models.PositiveIntegerField()),
                ('ataque_especial', models.PositiveIntegerField()),
                ('defesa_especial', models.PositiveIntegerField()),
                ('velocidade', models.PositiveIntegerField()),
                ('fk_categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pokedex.Categoria')),
                ('fk_habilidades', models.ManyToManyField(to='pokedex.Habilidade')),
            ],
        ),
    ]
