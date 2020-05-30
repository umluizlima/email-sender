from app.core.adapters import ActiveAdapter, BaseAdapter


def test_active_adapter_call_returns_adapter_instance(settings):
    get_active_adapter = ActiveAdapter(settings=settings)
    assert isinstance(get_active_adapter(), BaseAdapter)
