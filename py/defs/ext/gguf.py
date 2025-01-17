# https://github.com/city96/ComfyUI-GGUF
from ..meta import MetaField
from ..formatters import calc_unet_hash


CAPTURE_FIELD_LIST = {
    "UnetLoaderGGUF": {
        MetaField.MODEL_NAME: {"field_name": "unet_name"},
        MetaField.MODEL_HASH: {"field_name": "unet_name", "format": calc_unet_hash},
    },
    "UnetLoaderGGUFAdvanced": {
        MetaField.MODEL_NAME: {"field_name": "unet_name"},
        MetaField.MODEL_HASH: {"field_name": "unet_name", "format": calc_unet_hash},
    },
}
