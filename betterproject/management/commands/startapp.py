import os
import src

def app_copy_helper(*args, **kwargs):
    from src.management.base import copy_helper

    import ipdb; ipdb.set_trace()
    kwargs['template_dir'] = os.path.join(src.__path__[0], 'conf', 'app_template')
    copy_helper(*args, **kwargs)

# replace django's default copy_helper with ours
import django.core.management.base
django.core.management.base.copy_helper = app_copy_helper

# Since we're keeping the same copy_helper api, we can use Django's original commands
from django.core.management.commands.startapp import Command, ProjectCommand
