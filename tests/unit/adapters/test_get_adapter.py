from app.core.adapters import BaseAdapter, get_adapter


def test_get_adapter_call_returns_adapter_instance(settings):
    adapter = get_adapter(settings=settings)
    assert isinstance(adapter, BaseAdapter)
