  # -*- coding: utf-8 -*-
  #!/usr/bin/env python

from django.core.management import execute_manager
import imp
try:
    imp.find_module('settings')
except ImportError:
    import sys
    sys.stderr.write(
        "Error: Can't find the file 'settings.py' in the directory%r."
        % __file__)
    sys.exit(1)

import settings

if __name__ == "__main__":
    execute_manager(settings)
