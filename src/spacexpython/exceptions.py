"""Exceptions module

This module contains the exceptions which SpacePY-X generates:

This file is imported as a module and contains the following
Exceptions:

    * SpaceXReadTimeOut - if a call to the API times out.
        The timeout respects the timeOut parameter on all functions
    * SpaceXParameterError - if a call to a wrapper function contains
        either invalid parameter names (or types), this exception is
        returned together with a message stating where the issue lies.
"""


class SpaceXReadTimeOut(Exception):
    pass


class SpaceXParameterError(Exception):
    pass
