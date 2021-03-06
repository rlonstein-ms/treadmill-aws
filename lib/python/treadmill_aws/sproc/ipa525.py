"""Runs IPA 525 credential service.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

import click

from treadmill_aws import ipa525

_LOGGER = logging.getLogger(__name__)


def init():
    """Top level command handler."""

    @click.command()
    @click.option('--port',
                  required=True,
                  type=int,
                  help='Service port to listen on.')
    @click.option('--client-realm',
                  required=True,
                  help='Client Kerberos realm.')
    @click.option('--server-realm',
                  required=True,
                  help='Server Kerberos realm.')
    @click.option('--admin-group',
                  required=False,
                  help='IPA 525 admin group.')
    def ipa525server(port, client_realm, server_realm, admin_group):
        """Run IPA525 credential daemon."""
        ipa525.run_server(port, client_realm, server_realm, admin_group)

    return ipa525server
