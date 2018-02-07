# -*- coding: utf-8 -*-

"""Console script for twitter_monitor."""

from datetime import (
    datetime,
    timedelta,
)
import configparser
import click
from monitoring.twitter_monitor import Monitor
from monitoring.exceptions import MonitoringError


'''
    @click.option('--host', default='localhost')
    @click.option('--key', defaults='twitter.monitor.keyword.count')
    @click.option('--zabbix', default='localhost')
'''

@click.command()
@click.option('--config', '-c', help='Configuration file location')
@click.option('--key', '-k', help='Keyword to monitor in Twitter')
@click.option('--operation', '-o')
@click.option('--date_from', '-df',  help='YYYY-MM-DD')
@click.option('--date_to', '-dt', help='YYYY-MM-DD')
def main(**kwargs):
    """Console script for twitter_monitor."""

    if not kwargs.get('config'):
        raise MonitoringError('Missing configuration file')
    if not kwargs.get('key'):
        raise MonitoringError('Missing key to monitor')

    cp = configparser.ConfigParser()
    cp.read(kwargs['config'])
    app_config = cp['twitter']


    if not kwargs.get('date_from'):
        kwargs['date_from'] = today - timedelta(days=1)
    if not kwargs.get('date_to'):
        kwargs['date_to'] = today

    monitor = Monitor(app_config)
    count = monitor.run(**kwargs)
    print(count)


if __name__ == "__main__":
    main()
