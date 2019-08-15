from .monitor import prometheus_monitor


@prometheus_monitor
def alpha():
    print("function alpha")
    bravo()


def bravo():
    print("function bravo")
