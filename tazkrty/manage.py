#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django  # Import django

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tazkrty.settings')

    # Add this block to handle createsuperuser
    if 'createsuperuser' in sys.argv:
        from django.conf import settings
        settings.DATABASES['default'] = settings.DATABASES['users_db']
        django.setup()  # Set up Django with the modified settings
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
        return  # Exit the function after createsuperuser

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