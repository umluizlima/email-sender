from app.core.adapters import ActiveAdapter, BaseAdapter
from app.settings import EmailService, Settings

settings = Settings(_env_file=None, EMAIL_SERVICE=EmailService.SENDGRID.value,)


def test_active_adapter_call_returns_adapter_instance():
    get_active_adapter = ActiveAdapter(settings=settings)
    assert isinstance(get_active_adapter(), BaseAdapter)
