from .emails import SendEmailTask


def configure(app, settings):
    for task in [SendEmailTask]:
        app.tasks.register(task)
