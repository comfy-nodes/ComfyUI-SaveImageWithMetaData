# https://github.com/ssitu/ComfyUI_UltimateSDUpscale
from ..meta import MetaField


def get_custom_sampler_name(node_id, obj, prompt, extra_data, outputs, input_data):
    node_inputs = prompt[node_id]["inputs"]
    custom_sampler_input = node_inputs.get("custom_sampler")
    if isinstance(custom_sampler_input, list):
        connected_node_id = custom_sampler_input[0]
        connected_node = prompt[connected_node_id]
        return connected_node["inputs"].get("sampler_name")
    else:
        return obj["inputs"].get("sampler_name")


def get_custom_scheduler(node_id, obj, prompt, extra_data, outputs, input_data):
    node_inputs = prompt[node_id]["inputs"]
    custom_sigmas_input = node_inputs.get("custom_sigmas")
    if isinstance(custom_sigmas_input, list):
        connected_node_id = custom_sigmas_input[0]
        connected_node = prompt[connected_node_id]
        return connected_node["inputs"].get("scheduler")
    else:
        return obj["inputs"].get("scheduler")


SAMPLERS = {
    "UltimateSDUpscale": {
        "positive": "positive",
        "negative": "negative",
    },
    "UltimateSDUpscaleNoUpscale": {
        "positive": "positive",
        "negative": "negative",
    },
    "UltimateSDUpscaleCustomSample": {
        "positive": "positive",
        "negative": "negative",
    },
}

CAPTURE_FIELD_LIST = {
    "UltimateSDUpscale": {
        MetaField.SEED: {"field_name": "seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
    "UltimateSDUpscaleNoUpscale": {
        MetaField.SEED: {"field_name": "noise_seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
    "UltimateSDUpscaleCustomSample": {
        MetaField.SEED: {"field_name": "noise_seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"selector": get_custom_sampler_name},
        MetaField.SCHEDULER: {"selector": get_custom_scheduler},
    },
}
