from unittest.mock import MagicMock

from pytest import fixture

from app.core.schemas import EmailSchema, TransactionalType
from app.core.services import TransactionalService

mock_template_service = MagicMock()

template_title = "template title"
rendered_template = "rendered template"


@fixture
def transactional_service():
    return TransactionalService(mock_template_service)


def test_transactional_service_builds_email(
    transactional_service, transactional_message
):
    mock_template_service.render_template.return_value = rendered_template
    mock_template_service.get_title.return_value = template_title

    email = transactional_service.build_email(transactional_message)

    mock_template_service.render_template.assert_called_once_with(
        TransactionalType.ACCESS_CODE.template, {}
    )
    mock_template_service.get_title.assert_called_once_with(rendered_template)
    assert isinstance(email, EmailSchema)
    assert email.to_email == transactional_message.to_email
    assert email.from_email == transactional_message.from_email
    assert email.subject == template_title
    assert email.content == rendered_template
