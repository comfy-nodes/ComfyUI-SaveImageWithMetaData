# CheckpointLoaderKJ
# https://github.com/kijai/ComfyUI-KJNodes
from ..meta import MetaField
from ..formatters import (
    get_model_name,
    calc_model_hash,
    get_unet_name,
    calc_unet_hash
)


CAPTURE_FIELD_LIST = {
    "CheckpointLoaderKJ": {
        MetaField.MODEL_NAME: {"field_name": "ckpt_name", "format": get_model_name},
        MetaField.MODEL_HASH: {"field_name": "ckpt_name", "format": calc_model_hash},
    },
    "DiffusionModelLoaderKJ": {
        MetaField.MODEL_NAME: {"field_name": "model_name", "format": get_unet_name},
        MetaField.MODEL_HASH: {"field_name": "model_name", "format": calc_unet_hash},
    },
    "GGUFLoaderKJ": {
        MetaField.MODEL_NAME: {"field_name": "model_name", "format": get_unet_name},
        MetaField.MODEL_HASH: {"field_name": "model_name", "format": calc_unet_hash},
    },
}
