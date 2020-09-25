from . import send_email, send_transactional


def configure(app, settings):
    for task in [send_email, send_transactional]:
        app.tasks.register(task.configure(settings))
