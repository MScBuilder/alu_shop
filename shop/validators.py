from django.core.exceptions import ValidationError
import shop.aluminium_system_info.size_restrictions as alu_info



def width_validator(category, width):
    if category == "FW":
        if width >= alu_info.FIX_MIN_WIDTH and width <= alu_info.FIX_MAX_WIDTH:
            return width
        else: 
            raise ValidationError(f"Width of the FIX windows should be between {alu_info.FIX_MIN_WIDTH} and {alu_info.FIX_MAX_WIDTH} ")
    elif category == 'CW':
        if width >= alu_info.CASEMENT_MIN_WIDTH and width <= alu_info.CASEMENT_MAX_WIDTH:
            return width
        else: 
            raise ValidationError(f"Width of the CASEMENT windows should be between {alu_info.CASEMENT_MIN_WIDTH} and {alu_info.CASEMENT_MAX_WIDTH} ")
    else:
        if width >= alu_info.SLIDE_MIN_WIDTH and width <= alu_info.SLIDE_MAX_WIDTH:
            return width
        else: 
            raise ValidationError(f"Width of the SLIDING windows should be between {alu_info.SLIDE_MIN_WIDTH} and {alu_info.SLIDE_MAX_WIDTH} ")


def height_validator(category, height):
    if category == "FW":
        if height >= alu_info.FIX_MIN_HEIGHT and height <= alu_info.FIX_MAX_HEIGHT:
            return height
        else: 
            raise ValidationError(f"Width of the FIX windows should be between {alu_info.FIX_MIN_HEIGHT} and {alu_info.FIX_MAX_HEIGHT} ")
    elif category == 'CW':
        if height >= alu_info.CASEMENT_MIN_HEIGHT and height <= alu_info.CASEMENT_MAX_HEIGHT:
            return height
        else: 
            raise ValidationError(f"Width of the CASEMENT windows should be between {alu_info.CASEMENT_MIN_HEIGHT} and {alu_info.CASEMENT_MAX_HEIGHT} ")
    else:
        if height >= alu_info.SLIDE_MIN_HEIGHT and height <= alu_info.SLIDE_MAX_HEIGHT:
            return height
        else: 
            raise ValidationError(f"Width of the SLIDING windows should be between {alu_info.SLIDE_MIN_HEIGHT} and {alu_info.SLIDE_MAX_HEIGHT} ")
