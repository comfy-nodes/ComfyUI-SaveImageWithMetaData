# https://github.com/mit-han-lab/ComfyUI-nunchaku
from ..meta import MetaField
from ..formatters import calc_lora_hash, get_unet_name


CAPTURE_FIELD_LIST = {
    "NunchakuFluxDiTLoader": {
        MetaField.MODEL_NAME: {"field_name": "model_path", "format": get_unet_name},
    },
    "NunchakuFluxLoraLoader": {
        MetaField.LORA_MODEL_NAME: {"field_name": "lora_name"},
        MetaField.LORA_MODEL_HASH: {"field_name": "lora_name", "format": calc_lora_hash},
        MetaField.LORA_STRENGTH_MODEL: {"field_name": "lora_strength"},
        MetaField.LORA_STRENGTH_CLIP: {"value": 0},
    },
}
