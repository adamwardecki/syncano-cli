# -*- coding: utf-8 -*-

from syncano_cli.base.exceptions import CLIBaseException


class MissingRequestDataException(CLIBaseException):
    default_message = u'--data option should be provided when method {} is used'


class EndpointNotFoundException(CLIBaseException):
    default_message = u'Endpoint `{}` not found'


class SocketYMLParseException(CLIBaseException):
    default_message = u'Can not parse yml file.'


class SocketFileFetchException(CLIBaseException):
    default_message = u'Can not fetch the file: {}.'


class ConfigNameMissingException(CLIBaseException):
    default_message = u'Variable name should be provided in config.'


class OneEndpointPerMethodException(CLIBaseException):
    default_message = u'Only one endpoint per method allowed.'


class BadYAMLDefinitionInEndpointsException(CLIBaseException):
    default_message = u'Specify one general endpoint or specify endpoints for each method.'


class SocketNameMissingException(CLIBaseException):
    default_message = u'Name should be specified: `--name`.'