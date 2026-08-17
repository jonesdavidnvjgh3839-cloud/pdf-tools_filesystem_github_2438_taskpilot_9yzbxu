# TaskPilot

A lightweight distributed task queue for Python applications (internal codename: taskpilot_9yzbxu).

## Features
- Redis as the message broker
- Priority queues
- Retries with exponential backoff
- Delayed / scheduled task execution
- Web dashboard for monitoring

## Quick Start
```python
from taskpilot import TaskPilot

app = TaskPilot(redis_url='redis://localhost:6379/0')

@app.task(queue='high')
def send_email(user_id):
    ...
```

## License
MIT
