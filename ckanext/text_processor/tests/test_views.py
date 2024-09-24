"""Tests for views.py."""

import pytest

import ckanext.text_processor.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "text_processor")
@pytest.mark.usefixtures("with_plugins")
def test_text_processor_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("text_processor.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, text_processor!"
