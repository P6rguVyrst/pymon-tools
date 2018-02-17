# -*- coding: utf-8 -*-

"""Console script for dirmon."""
import time
import logging.config
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import click
import redis

 class RedisHandler(FileSystemEventHandler):


     def __init__(self, observer):
         self.observer = observer
         self.redis = redis.Redis()

     def on_created(self, event):
         self.rpush('queue', event)
         print(event)
     def on_moved(self, event):
         self.rpush('queue', event)
         print(event)
     def on_deleted(self, event):
         self.rpush('queue', event)
         print(event)
     def on_modified(self, event):
         self.rpush('queue', event)
         print(event)


def choose_handler(handler, observer):
    options = {
        'logging': LoggingEventHandler,
        'redis': RedisHandler,
    }
    return options.get(handler, 'logging')(observer)


@click.command()
@click.option('--path', '-p', default='.', help='System path to monitor')
@click.option('--config', '-c', help='Configuration file')
@click.option('--handler'. '-h', default='logging')
def main(path, **kwargs):
    """Console script for dirmon."""
    conf = kwargs.get('config')
    if not conf:
        raise AssertionError('Missing configuration.')

    logging.config.fileConfig(conf)
    logging.getLogger('dirmon')

    observer = Observer()
    choose_handler(handler, observer)
    #event_handler = LoggingEventHandler()
    #event_handler = RedisHandler(observer)

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
