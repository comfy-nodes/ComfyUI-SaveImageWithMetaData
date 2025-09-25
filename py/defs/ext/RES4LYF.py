# https://github.com/ClownsharkBatwing/RES4LYF
from ..meta import MetaField


SAMPLERS = {
    "BongSampler": {
        "positive": "positive",
        "negative": "negative",
    },
    "ClownsharKSampler": {
        "positive": "positive",
        "negative": "negative",
    },
    "ClownsharKSampler_Beta": {
        "positive": "positive",
        "negative": "negative",
    },
}


CAPTURE_FIELD_LIST = {
    "BongSampler": {
        MetaField.SEED: {"field_name": "seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
    "ClownsharKSampler": {
        MetaField.SEED: {"field_name": "noise_seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
    "ClownsharKSampler_Beta": {
        MetaField.SEED: {"field_name": "seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
}
