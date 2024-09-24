"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.text_processor.logic import validators


def test_text_processor_reauired_with_valid_value():
    assert validators.text_processor_required("value") == "value"


def test_text_processor_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.text_processor_required(None)
