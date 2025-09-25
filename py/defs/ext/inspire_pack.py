# https://github.com/ltdrdata/ComfyUI-Inspire-Pack
from ..meta import MetaField


SAMPLERS = {
    "KSampler //Inspire": {
        "positive": "positive",
        "negative": "negative",
    },
    "KSamplerAdvanced //Inspire": {
        "positive": "positive",
        "negative": "negative",
    },
    "KSamplerProgress //Inspire": {
        "positive": "positive",
        "negative": "negative",
    },
    "KSamplerAdvancedProgress //Inspire": {
        "positive": "positive",
        "negative": "negative",
    },
}


CAPTURE_FIELD_LIST = {
    "KSampler //Inspire": {
        MetaField.SEED: {"field_name": "seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
    "KSamplerAdvanced //Inspire": {
        MetaField.SEED: {"field_name": "noise_seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
    "KSamplerProgress //Inspire": {
        MetaField.SEED: {"field_name": "seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
    "KSamplerAdvancedProgress //Inspire": {
        MetaField.SEED: {"field_name": "noise_seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
}
