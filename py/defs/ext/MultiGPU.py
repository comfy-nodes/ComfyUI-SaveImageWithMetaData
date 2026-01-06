# https://github.com/pollockjj/ComfyUI-MultiGPU
from ..meta import MetaField
from ..formatters import (
    get_model_name,
    calc_model_hash,
    get_unet_name,
    calc_unet_hash
)


CAPTURE_FIELD_LIST = {
    "CheckpointLoaderAdvancedMultiGPU": {
        MetaField.MODEL_NAME: {"field_name": "ckpt_name", "format": get_model_name},
        MetaField.MODEL_HASH: {"field_name": "ckpt_name", "format": calc_model_hash},
    },
    "CheckpointLoaderAdvancedDisTorch2MultiGPU": {
        MetaField.MODEL_NAME: {"field_name": "ckpt_name", "format": get_model_name},
        MetaField.MODEL_HASH: {"field_name": "ckpt_name", "format": calc_model_hash},
    },
    "CheckpointLoaderSimpleMultiGPU": {
        MetaField.MODEL_NAME: {"field_name": "ckpt_name", "format": get_model_name},
        MetaField.MODEL_HASH: {"field_name": "ckpt_name", "format": calc_model_hash},
    },
    "CheckpointLoaderSimpleDisTorch2MultiGPU": {
        MetaField.MODEL_NAME: {"field_name": "ckpt_name", "format": get_model_name},
        MetaField.MODEL_HASH: {"field_name": "ckpt_name", "format": calc_model_hash},
    },
    "UNETLoaderMultiGPU": {
        MetaField.MODEL_NAME: {"field_name": "model_name", "format": get_unet_name},
        MetaField.MODEL_HASH: {"field_name": "model_name", "format": calc_unet_hash},
    },
    "UNETLoaderDisTorch2MultiGPU": {
        MetaField.MODEL_NAME: {"field_name": "model_name", "format": get_unet_name},
        MetaField.MODEL_HASH: {"field_name": "model_name", "format": calc_unet_hash},
    },
    "UnetLoaderGGUFDisTorchMultiGPU": {
        MetaField.MODEL_NAME: {"field_name": "model_name", "format": get_unet_name},
        MetaField.MODEL_HASH: {"field_name": "model_name", "format": calc_unet_hash},
    },
    "UnetLoaderGGUFAdvancedDisTorchMultiGPU": {
        MetaField.MODEL_NAME: {"field_name": "model_name", "format": get_unet_name},
        MetaField.MODEL_HASH: {"field_name": "model_name", "format": calc_unet_hash},
    },
    "UnetLoaderGGUFDisTorch2MultiGPU": {
        MetaField.MODEL_NAME: {"field_name": "model_name", "format": get_unet_name},
        MetaField.MODEL_HASH: {"field_name": "model_name", "format": calc_unet_hash},
    },
    "UnetLoaderGGUFAdvancedDisTorch2MultiGPU": {
        MetaField.MODEL_NAME: {"field_name": "model_name", "format": get_unet_name},
        MetaField.MODEL_HASH: {"field_name": "model_name", "format": calc_unet_hash},
    },
    "UnetLoaderGGUFMultiGPU": {
        MetaField.MODEL_NAME: {"field_name": "model_name", "format": get_unet_name},
        MetaField.MODEL_HASH: {"field_name": "model_name", "format": calc_unet_hash},
    },
    "UnetLoaderGGUFAdvancedMultiGPU": {
        MetaField.MODEL_NAME: {"field_name": "model_name", "format": get_unet_name},
        MetaField.MODEL_HASH: {"field_name": "model_name", "format": calc_unet_hash},
    },
}
