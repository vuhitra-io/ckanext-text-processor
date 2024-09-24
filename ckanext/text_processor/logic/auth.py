import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def text_processor_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "text_processor_get_sum": text_processor_get_sum,
    }
