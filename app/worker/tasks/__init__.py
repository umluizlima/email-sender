from . import send_email


def configure(app, settings):
    for task in [send_email]:
        app.tasks.register(task.configure(settings))
