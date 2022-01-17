# Generated by Django 4.0.1 on 2022-01-17 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matriculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.alunos')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.cursos')),
            ],
        ),
    ]