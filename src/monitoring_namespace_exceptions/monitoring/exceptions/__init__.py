"""monitoring_namespace_exceptions - Exceptions for monitoring namespace packages"""

__version__ = '0.1.0'
__author__ = 'Toomas Ormisson <toomas.ormisson@gmail.com>'
__all__ = []
name = 'exceptions'

class MonitoringError(Exception):
    pass

class MonitoringClientError(MonitoringError):
    pass

class MonitoringServerError(MonitoringError):
    pass
