from django.db import migrations
from seeds.family import populate


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220628_1725'),
    ]

    operations = [
        migrations.RunPython(
            populate
        ),
    ]
