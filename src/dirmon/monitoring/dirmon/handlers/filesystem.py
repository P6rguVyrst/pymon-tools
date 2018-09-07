from watchdog.events import (
    FileSystemEventHandler,
)

class GitPusherEventHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        # @error_handling
        # Git commit
        # Git pull
        # Git push
        print(event)


class ConsolePrinterEventHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        print(event)

