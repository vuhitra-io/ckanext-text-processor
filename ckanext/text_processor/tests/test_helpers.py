"""Tests for helpers.py."""

import ckanext.text_processor.helpers as helpers


def test_text_processor_hello():
    assert helpers.text_processor_hello() == "Hello, text_processor!"
