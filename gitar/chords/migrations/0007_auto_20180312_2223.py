# Generated by Django 2.0.3 on 2018-03-12 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chords', '0006_auto_20180312_2220'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChordGenreReferences',
            new_name='ArtistGenreReference',
        ),
        migrations.RenameModel(
            old_name='ArtistGenreReferences',
            new_name='ChordGenreReference',
        ),
        migrations.RemoveField(
            model_name='artistgenrereference',
            name='chord',
        ),
        migrations.RemoveField(
            model_name='chordgenrereference',
            name='artist',
        ),
        migrations.AddField(
            model_name='artistgenrereference',
            name='artist',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='chords.Artist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chordgenrereference',
            name='chord',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='chords.Chord'),
            preserve_default=False,
        ),
    ]
