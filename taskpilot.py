"""TaskPilot - distributed task queue for Python."""

__version__ = "1.0.0"


class TaskPilot:
    def __init__(self, redis_url='redis://localhost:6379/0'):
        self.redis_url = redis_url

    def task(self, queue='default'):
        def decorator(fn):
            fn.queue = queue
            return fn
        return decorator

    def enqueue(self, fn, *args, **kwargs):
        # In a real implementation this publishes to Redis.
        return {'task': fn.__name__, 'args': args, 'kwargs': kwargs}
