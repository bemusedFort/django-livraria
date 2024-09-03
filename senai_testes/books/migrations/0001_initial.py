# Generated by Django 5.0.7 on 2024-08-01 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=10, verbose_name='Sexo')),
                ('birth_date', models.DateField(verbose_name='Data de Nascimento')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='PublishingCompany',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('cnpj', models.CharField(max_length=20, verbose_name='CNPJ')),
                ('address', models.CharField(max_length=100, verbose_name='Endereço')),
                ('address_number', models.CharField(max_length=50, verbose_name='Número')),
                ('address_complement', models.CharField(max_length=1000, verbose_name='Complemento')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('state', models.CharField(max_length=2, verbose_name='Estado')),
                ('zipcode', models.CharField(max_length=20, verbose_name='CEP')),
            ],
            options={
                'verbose_name': 'Editora',
                'verbose_name_plural': 'Editoras',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('pages', models.IntegerField(verbose_name='Páginas')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('publication_date', models.DateField(verbose_name='Data de Publicação')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author', verbose_name='Autor')),
                ('publishing_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.publishingcompany', verbose_name='Editora')),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
            },
        ),
        migrations.CreateModel(
            name='BookStock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('quantity', models.IntegerField(verbose_name='Quantidade')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books', verbose_name='Livro')),
            ],
            options={
                'verbose_name': 'Estoque',
                'verbose_name_plural': 'Estoques',
            },
        ),
    ]