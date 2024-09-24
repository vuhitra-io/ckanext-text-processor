import ckan.plugins.toolkit as tk
import ckanext.text_processor.logic.schema as schema


@tk.side_effect_free
def text_processor_get_sum(context, data_dict):
    tk.check_access(
        "text_processor_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.text_processor_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'text_processor_get_sum': text_processor_get_sum,
    }
