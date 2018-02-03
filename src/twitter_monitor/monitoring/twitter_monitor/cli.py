# -*- coding: utf-8 -*-

"""Console script for twitter_monitor."""

# Monitoring namespace

from datetime import datetime
import click
from monitoring.twitter_monitor import Monitor
from monitoring.exceptions import MonitoringError


'''
    @click.option('--host', default='localhost')
    @click.option('--key', defaults='twitter.monitor.keyword.count')
    @click.option('--zabbix', default='localhost')
'''

@click.command()
@click.option('--config')
@click.option('--key', help='Keyword to monitor in Twitter')
@click.option('--date_from', help='YYYY-MM-DD')
@click.option('--date_to', help='YYYY-MM-DD')
def main(config, key, date_from, date_to):
    """Console script for twitter_monitor."""

    if not config:
        raise MonitoringError('Missing configuration file')

    now = datetime.now()
    if not date_from:
        date_from = (str(now.year)+'-'+str(now.month)+'-'+str(now.day-1))
    if not date_to:
        date_to = (str(now.year)+'-'+str(now.month)+'-'+str(now.day))

    monitor = Monitor(config)
    count = monitor.run()

    #count = get_keyword_count(config, key, date_from, date_to)
    print(count)


if __name__ == "__main__":
    main()
