#!/usr/bin/env python
import os
import sys

def main():
    """Run administrative tasks."""
    # Lê o ambiente (dev ou prod)
    environment = os.environ.get("DJANGO_ENV", "dev")

    # Define o módulo de configuração conforme o ambiente
    if environment == "prod":
        settings_module = "core.settings.prod"
    else:
        settings_module = "core.settings.dev"

    # Define a variável que o Django usa
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    print(f"[manage.py] DJANGO_ENV={environment}")
    print(f"[manage.py] Using settings: {settings_module}")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
