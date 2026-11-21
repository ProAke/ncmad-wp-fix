#!/usr/bin/env python3
"""Write new, local-only Compose credentials without overwriting an existing file."""

from os import open as os_open
from pathlib import Path
from secrets import token_hex
import sys


def private_opener(path, flags):
    return os_open(path, flags, 0o600)


def main():
    env_path = Path(__file__).resolve().parent.parent / '.env'
    try:
        with open(env_path, 'x', opener=private_opener, encoding='utf-8') as env:
            env.write(
                f'STAGING_DB_PASSWORD={token_hex(32)}\n'
                f'STAGING_ROOT_PASSWORD={token_hex(32)}\n'
                'STAGING_TABLE_PREFIX=wp_\n'
                '# STAGING_WP_IMAGE=wordpress:php8.3-apache\n'
                '# STAGING_CLI_IMAGE=wordpress:cli-php8.3\n'
                '# STAGING_DB_IMAGE=mariadb:10.11\n'
            )
    except FileExistsError:
        print('.env already exists; no changes made.', file=sys.stderr)
        return 1
    print('Created .env with new staging-only database credentials.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
