import ckan.plugins.toolkit as tk


def text_processor_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "text_processor_required": text_processor_required,
    }
