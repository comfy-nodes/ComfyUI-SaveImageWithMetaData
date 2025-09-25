import re

from ..meta import MetaField


def get_width(preset, input_data):
    match = re.search(r"\b(\d+)\s*[x×]\s*(\d+)\b", preset)
    return int(match.group(1)) if match else None


def get_height(preset, input_data):
    match = re.search(r"\b(\d+)\s*[x×]\s*(\d+)\b", preset)
    return int(match.group(2)) if match else None


CAPTURE_FIELD_LIST = {
    # https://github.com/nkchocoai/ComfyUI-SizeFromPresets
    "EmptyLatentImageFromPresetsSD15": {
        MetaField.IMAGE_WIDTH: {"field_name": "preset", "format": get_width},
        MetaField.IMAGE_HEIGHT: {"field_name": "preset", "format": get_height},
    },
    "EmptyLatentImageFromPresetsSDXL": {
        MetaField.IMAGE_WIDTH: {"field_name": "preset", "format": get_width},
        MetaField.IMAGE_HEIGHT: {"field_name": "preset", "format": get_height},
    },
    # https://github.com/cubiq/ComfyUI_essentials
    "SDXLEmptyLatentSizePicker+": {
        MetaField.IMAGE_WIDTH: {"field_name": "resolution", "format": get_width},
        MetaField.IMAGE_HEIGHT: {"field_name": "resolution", "format": get_height},
    },
    # https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes
    "CR SD1.5 Aspect Ratio": {
        MetaField.IMAGE_WIDTH: {"field_name": "aspect_ratio", "format": get_width},
        MetaField.IMAGE_HEIGHT: {"field_name": "aspect_ratio", "format": get_height},
    },
    "CR SDXL Aspect Ratio": {
        MetaField.IMAGE_WIDTH: {"field_name": "aspect_ratio", "format": get_width},
        MetaField.IMAGE_HEIGHT: {"field_name": "aspect_ratio", "format": get_height},
    },
    "CR Aspect Ratio": {
        MetaField.IMAGE_WIDTH: {"field_name": "aspect_ratio", "format": get_width},
        MetaField.IMAGE_HEIGHT: {"field_name": "aspect_ratio", "format": get_height},
    },
    "CR Aspect Ratio SDXL": {
        MetaField.IMAGE_WIDTH: {"field_name": "aspect_ratio", "format": get_width},
        MetaField.IMAGE_HEIGHT: {"field_name": "aspect_ratio", "format": get_height},
    },
    # TODO RandomEmptyLatentImageFromPresetsSD..
}
