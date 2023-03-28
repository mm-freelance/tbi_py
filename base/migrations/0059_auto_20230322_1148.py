# Generated by Django 3.2.4 on 2023-03-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0058_categoryforblogs_categoryforevents_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_section',
            old_name='Address',
            new_name='Address1',
        ),
        migrations.AddField(
            model_name='contact_section',
            name='Address2',
            field=models.CharField(default='Dr. A.P.J. Abdul Kalam Block, Nehru Group of Institutions, Thirumalayampalayam, Coimbatore – 641 105,Tamil Nadu.', max_length=2000),
            preserve_default=False,
        ),
    ]