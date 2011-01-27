import os
import betterproject

def project_copy_helper(*args, **kwargs):
    from betterproject.management.base import copy_helper

    kwargs['template_dir'] = os.path.join(src.__path__[0], 'conf', 'project_template')
    copy_helper(*args, **kwargs)

# replace django's default copy_helper with ours
import django.core.management.base
django.core.management.base.copy_helper = project_copy_helper

# Since we're keeping the same copy_helper api, we can use Django's original commands
from django.core.management.commands.startproject import Command
