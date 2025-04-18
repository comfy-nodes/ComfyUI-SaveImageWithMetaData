from .meta import MetaField
from .validators import is_positive_prompt, is_negative_prompt
from .formatters import (
    calc_model_hash,
    calc_vae_hash,
    calc_lora_hash,
    calc_unet_hash,
    get_model_name,
    get_vae_name,
    get_unet_name,
    convert_skip_clip,
    get_scaled_width,
    get_scaled_height,
    extract_embedding_names,
    extract_embedding_hashes,
)


CAPTURE_FIELD_LIST = {
    "CheckpointLoaderSimple": {
        MetaField.MODEL_NAME: {"field_name": "ckpt_name", "format": get_model_name},
        MetaField.MODEL_HASH: {"field_name": "ckpt_name", "format": calc_model_hash},
    },
    "CLIPSetLastLayer": {
        MetaField.CLIP_SKIP: {
            "field_name": "stop_at_clip_layer",
            "format": convert_skip_clip,
        },
    },
    "VAELoader": {
        MetaField.VAE_NAME: {"field_name": "vae_name", "format": get_vae_name},
        MetaField.VAE_HASH: {"field_name": "vae_name", "format": calc_vae_hash},
    },
    "EmptyLatentImage": {
        MetaField.IMAGE_WIDTH: {"field_name": "width"},
        MetaField.IMAGE_HEIGHT: {"field_name": "height"},
    },
    "CLIPTextEncode": {
        MetaField.POSITIVE_PROMPT: {
            "field_name": "text",
            "validate": is_positive_prompt,
        },
        MetaField.NEGATIVE_PROMPT: {
            "field_name": "text",
            "validate": is_negative_prompt,
        },
        MetaField.EMBEDDING_NAME: {
            "field_name": "text",
            "format": extract_embedding_names,
        },
        MetaField.EMBEDDING_HASH: {
            "field_name": "text",
            "format": extract_embedding_hashes,
        },
    },
    "CLIPTextEncodeSDXL": {
        MetaField.POSITIVE_PROMPT: {
            "field_name": "text_g",
            "validate": is_positive_prompt,
        },
        MetaField.NEGATIVE_PROMPT: {
            "field_name": "text_g",
            "validate": is_negative_prompt,
        },
        MetaField.EMBEDDING_NAME: {
            "field_name": "text_g",
            "format": extract_embedding_names,
        },
        MetaField.EMBEDDING_HASH: {
            "field_name": "text_g",
            "format": extract_embedding_hashes,
        },
    },
    "CLIPTextEncodeFlux": {
        MetaField.POSITIVE_PROMPT: {
            "field_name": "t5xxl",
            "validate": is_positive_prompt,
        },
        MetaField.EMBEDDING_NAME: {
            "field_name": "t5xxl",
            "format": extract_embedding_names,
        },
        MetaField.EMBEDDING_HASH: {
            "field_name": "t5xxl",
            "format": extract_embedding_hashes,
        },
    },
    "KSampler": {
        MetaField.SEED: {"field_name": "seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
    "KSamplerAdvanced": {
        MetaField.SEED: {"field_name": "noise_seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
    "LatentUpscale": {
        MetaField.IMAGE_WIDTH: {"field_name": "width"},
        MetaField.IMAGE_HEIGHT: {"field_name": "height"},
    },
    "LatentUpscaleBy": {
        MetaField.IMAGE_WIDTH: {"field_name": "scale_by", "format": get_scaled_width},
        MetaField.IMAGE_HEIGHT: {
            "field_name": "scale_by",
            "format": get_scaled_height,
        },
    },
    "LoraLoader": {
        MetaField.LORA_MODEL_NAME: {"field_name": "lora_name"},
        MetaField.LORA_MODEL_HASH: {
            "field_name": "lora_name",
            "format": calc_lora_hash,
        },
        MetaField.LORA_STRENGTH_MODEL: {"field_name": "strength_model"},
        MetaField.LORA_STRENGTH_CLIP: {"field_name": "strength_clip"},
    },
    "LoraLoaderModelOnly": {
        MetaField.LORA_MODEL_NAME: {"field_name": "lora_name"},
        MetaField.LORA_MODEL_HASH: {
            "field_name": "lora_name",
            "format": calc_lora_hash,
        },
        MetaField.LORA_STRENGTH_MODEL: {"field_name": "strength_model"},
        MetaField.LORA_STRENGTH_CLIP: {"value": 0},
    },
    # Flux - https://comfyanonymous.github.io/ComfyUI_examples/flux/
    "UNETLoader": {
        MetaField.MODEL_NAME: {"field_name": "unet_name", "format": get_unet_name},
        MetaField.MODEL_HASH: {"field_name": "unet_name", "format": calc_unet_hash},
    },
    "RandomNoise": {
        MetaField.SEED: {"field_name": "noise_seed"},
    },
    "BasicScheduler": {
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
    "KSamplerSelect": {
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
    },
    "FluxGuidance": {
        MetaField.GUIDANCE: {"field_name": "guidance"},
    },
    "CFGGuider": {
        MetaField.CFG: {"field_name": "cfg"},
    },
}
