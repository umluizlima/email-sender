from . import emails, transactionals


def configure(app, settings):
    for router in [emails, transactionals]:
        router.configure(app, settings)
