import os
import betterproject

def app_copy_helper(*args, **kwargs):
    from betterproject.management.base import copy_helper

    kwargs['template_dir'] = os.path.join(betterproject.__path__[0], 'conf', 'app_template')
    copy_helper(*args, **kwargs)

# replace django's default copy_helper with ours
import django.core.management.base
django.core.management.base.copy_helper = app_copy_helper

# Since we're keeping the same copy_helper api, we can use Django's original commands
from django.core.management.commands.startapp import Command, ProjectCommand
