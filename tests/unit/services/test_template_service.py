from unittest.mock import patch

from jinja2 import DictLoader
from jinja2.exceptions import TemplateNotFound
from pytest import fixture, raises

from app.core.services import TemplateService


def get_test_template(title, variable):
    return f"""
        <html>
        <head>
        <title>{title}</title>
        </head>
        <body>
        <p>{variable}</p>
        </body>
        </html>
    """


test_title = "template title"
test_variable = "variable for testing"
test_templates = {
    "test.html": get_test_template("{{ title }}", "{{ variable }}"),
}


@fixture
@patch(
    "app.core.services.template.FileSystemLoader",
    return_value=DictLoader(test_templates),
)
def template_service(settings):
    return TemplateService(settings)


def test_template_service_renders_template_if_exists(template_service):
    rendered_template = template_service.render_template(
        "test.html", {"title": test_title, "variable": test_variable},
    )
    assert rendered_template == get_test_template(test_title, test_variable)


def test_template_service_renders_with_no_attributes(template_service):
    rendered_template = template_service.render_template("test.html", {})
    assert rendered_template == get_test_template("", "")


def test_template_service_raises_exception_if_not_found(template_service):
    with raises(TemplateNotFound):
        template_service.render_template("abcdef.html", {})


def test_template_service_get_title_from_render(template_service):
    rendered_template = template_service.render_template(
        "test.html", {"title": test_title, "variable": test_variable},
    )
    assert TemplateService.get_title(rendered_template) == test_title


def test_template_service_get_title_returns_none_if_not_found(template_service):
    rendered_template = "<p>this is a rendered template without title tag</p>"
    assert TemplateService.get_title(rendered_template) is None
