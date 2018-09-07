# -*- coding: utf-8 -*-

"""Console script for dirmon."""
import time
import logging.config
import logging
from watchdog.observers import Observer
from .handlers import (
    LoggingEventHandler,
    GitPusherEventHandler,
    ConsolePrinterEventHandler,
)
import click



@click.command()
@click.option('--path', '-p', default='.', help='System path to monitor')
@click.option('--handler', '-h', default='logging', help='Handler for events')
@click.option('--config', '-c', help='Configuration file')
def main(path, handler, **kwargs):
    """Console script for dirmon."""

    conf = kwargs.get('config')
    if not conf:
        raise AssertionError('Missing configuration.')

    logging.config.fileConfig(conf)
    logging.getLogger('dirmon')

    router = {
        'printer': ConsolePrinterEventHandler,
        'logging': LoggingEventHandler,
        'git-pusher': GitPusherEventHandler,
    }

    event_handler = router[handler]()

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



if __name__ == "__main__":
    main()
