import sys
import os
import django
import logging

sys.path.append('./')
if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'config.settings')
    django.setup()
from django.core.management import call_command
from django.conf import settings

logger = logging.getLogger('django')

class MigrationRun:
    def main(self):
        print(f"Called Migrations: {django.db.connections.databases['default']['NAME']}")



        call_command('migrate')
        print("Migrations Were DONE")

if __name__ == "__main__":
    # db_name = sys.argv[2]
    # django.db.connections.databases['default']['NAME'] = db_name

    # django.db.connections.databases['default']['PASSWORD'] = settings.DATABASES["default"]["PASSWORD"]
    MigrationRun().main()