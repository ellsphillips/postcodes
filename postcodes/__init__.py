"""
UK postcodes, created by Royal Mail, are composed of 5 to 7 alphanumeric characters.
A full postcode designates an area with multiple addresses or a single delivery point.
"""

from .patterns import KEY_PATTERNS, UK_PATTERNS
from .postcode import Postcode
