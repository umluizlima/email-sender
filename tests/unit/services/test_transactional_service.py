from unittest.mock import MagicMock

from pytest import fixture, raises

from app.core.schemas import EmailSchema, TransactionalSchema
from app.core.services import TransactionalService

mock_template_service = MagicMock()

transactional_name = "ABC"
template_name = "testing"
template_title = "template title"
rendered_template = "rendered template"
transactional_templates = {
    transactional_name: template_name,
}


@fixture
def transactional_dict():
    return {
        "to": "to@email.com",
        "from": "from@email.com",
        "type": transactional_name,
        "data": {},
    }


@fixture
def transactional_service(settings):
    settings.TRANSACTIONAL_TEMPLATES = transactional_templates
    return TransactionalService(settings, mock_template_service)


def test_transactional_service_builds_email(transactional_service, transactional_dict):
    mock_template_service.render_template.return_value = rendered_template
    mock_template_service.get_title.return_value = template_title

    transactional = TransactionalSchema(**transactional_dict)
    email = transactional_service.build_email(transactional)

    mock_template_service.render_template.assert_called_once_with(template_name, {})
    mock_template_service.get_title.assert_called_once_with(rendered_template)
    assert isinstance(email, EmailSchema)
    assert email.to_email == transactional_dict["to"]
    assert email.from_email == transactional_dict["from"]
    assert email.subject == template_title
    assert email.content == rendered_template


def test_transactional_service_raises_error_if_template_not_found(
    transactional_service, transactional_dict
):
    transactional_dict["type"] = "DEF"
    transactional = TransactionalSchema(**transactional_dict)

    with raises(KeyError):
        transactional_service.build_email(transactional)
