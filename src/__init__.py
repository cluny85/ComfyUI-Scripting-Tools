from .enhanced_uuid_generator import (
    NODE_CLASS_MAPPINGS as enhanced_mappings,
    NODE_DISPLAY_NAME_MAPPINGS as enhanced_display_mappings,
)
from .uuid_generator_node import (
    NODE_CLASS_MAPPINGS as uuid_mappings,
    NODE_DISPLAY_NAME_MAPPINGS as uuid_display_mappings,
)

# Merge the mappings
NODE_CLASS_MAPPINGS = {
    **enhanced_mappings,
    **uuid_mappings
}
NODE_DISPLAY_NAME_MAPPINGS = {
    **enhanced_display_mappings,
    **uuid_display_mappings
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
