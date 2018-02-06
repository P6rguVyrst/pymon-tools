# -*- coding: utf-8 -*-

"""Console script for twitter_monitor."""

# Monitoring namespace
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
@click.option('--config', help='Configuration file location')
@click.option('--key', help='Keyword to monitor in Twitter')
@click.option('--date_from', help='YYYY-MM-DD')
@click.option('--date_to', help='YYYY-MM-DD')
def main(config, key, date_from, date_to):
    """Console script for twitter_monitor."""

    if not config:
        raise MonitoringError('Missing configuration file')
    if not key:
        raise MonitoringError('Missing key to monitor')

    conf = configparser.ConfigParser()
    conf.read(config)
    conf = conf['twitter']

    today = datetime.now().date()
    #datetime.now().date().isoformat()
    if not date_from:
        #date_from = (str(today.year)+'-'+str(today.month)+'-'+str(today.day-1))
        date_from = today - timedelta(days=1)
    if not date_to:
        date_to = today

    monitor = Monitor(conf)
    print(key, date_from, date_to)
    data = {
        'key': key,
        'date_from': date_from.isoformat(),
        'date_to': date_to.isoformat()
    }
    count = monitor.run(data)
    print(count)


if __name__ == "__main__":
    main()
