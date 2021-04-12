#!/usr/bin/env python
"""Since we are trying to distribute Django applications as Python Packages,
it is important that some commands (such `migrate`) are available from within
the installation of the package without the need of copying the source code.

Because of that ``pyscaffoldext-django`` moves the generated ``manage.py`` file
to become the package's ``__main__.py`` file. This way all the commands that
could be run before as ``python3 manage.py <COMMAND>`` can now be run as
``python3 -m component_tags_tailwindcss <COMMAND>``, in a straight forward fashion just after
a ``pip3 install``.

This file is a executable stub that simply calls ``__main__.py:main()`` for
the sake of backward compatibility of the developer's workflow.
"""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


