from .category_options import CATEGORY_CHOICES

FIX_BASE = 1000
CASEMENT_BASE = 2000
SLIDING_BASE = 4000

def calculate_price(construction):
    if construction.category == "FW":
        price = FIX_BASE + construction.width * construction.height * 0.000001 * 500
    if construction.category == "CW":
        price = CASEMENT_BASE + construction.width * construction.height * 0.000001 * 1000
    if construction.category == "SW":
        price = SLIDING_BASE + construction.width * construction.height * 0.000001 * 1500
    return price