# Generated by Django 3.2.4 on 2023-02-15 17:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0047_auto_20230215_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Start_UpTN',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Heading', models.CharField(max_length=200)),
                ('Content_1', models.CharField(max_length=200)),
                ('last_updated_date', models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 189208, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Start_UpTNContent2',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Content_2', models.CharField(max_length=200)),
                ('last_updated_date', models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 189208, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Start_UpTNimg1',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='images/user_image.png', upload_to='Start_UpTNimg1/%Y/%m/%d')),
                ('last_updated_date', models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 189208, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Start_UpTNimg2',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='images/user_image.png', upload_to='Start_UpTNimg2/%Y/%m/%d')),
                ('last_updated_date', models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 189208, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='about_sisfs',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aboutheading',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='angelinvestordb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='angelinvestorsdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='awards',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='awards',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='birac',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='carrer',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='centralgovernmentfundingdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact_section',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='demodaydb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='demodaypic',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 186861, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='demodaytopsection',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 186861, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventsform',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='globalmarket',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='globalmarketconnectdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='globalmarketpic',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='govt_tie',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='home_testimonial',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='howwework',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='international_partners',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='investors',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='joinourcommunity',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lastcontent',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='latest_news',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='logo',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mbadb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mentorclinicdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mentorconnectdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mission',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new_venturesdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ourprocess',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ourstartup',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sisfs',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181297, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spendingsection',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='stategovernmentfundingdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='stategovtfund',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 186861, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='stategovtfunddb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='stategovtfundeligibilitysection',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 189208, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='stategovtfundsecondsection',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 186861, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tbi',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181297, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topsection',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='value',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='venturecapitalistdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vision',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 176787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='whatwedo',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='whoarewe',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 33, 15, 181804, tzinfo=utc)),
        ),
    ]