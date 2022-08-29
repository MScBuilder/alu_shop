from django.core.exceptions import ValidationError
import shop.aluminium_system_info.size_restrictions as alu_info



def width_validator(value):
    if value >= alu_info.FIX_MIN_WIDTH and value <= alu_info.FIX_MAX_WIDTH:
        return value
    else:
        raise ValidationError(f"Width of the FIX windows should be between {alu_info.FIX_MIN_WIDTH} and {alu_info.FIX_MAX_WIDTH} ")

def height_validator(value):
    if value >= alu_info.FIX_MIN_HEIGHT and value <= alu_info.FIX_MAX_HEIGHT:
        return value
    else:
        raise ValidationError(f"Width of the FIX windows should be between {alu_info.FIX_MIN_HEIGHT} and {alu_info.FIX_MAX_HEIGHT} ")