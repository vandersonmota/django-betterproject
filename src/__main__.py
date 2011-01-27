import sys
from os import path

from django.conf import settings
from django.core import management


PACKAGE_PATH = path.dirname(__file__)
PACKAGE_NAME = path.basename(PACKAGE_PATH)
PARENT_PATH  = path.abspath(path.join(PACKAGE_PATH, path.pardir))

# Hack related to the way find_management_module works
# Forces Django to find the management commands in this package
sys.path.insert(0, PARENT_PATH)

settings.configure(INSTALLED_APPS=[PACKAGE_NAME])
management.execute_from_command_line(sys.argv)