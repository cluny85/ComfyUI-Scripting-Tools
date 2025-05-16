import uuid


class UUIDGeneratorNode:
    """
    A simple node to generate a v4 UUID and return it as a string.
    """

    # Define how the node will be displayed in ComfyUI's menu
    NODE_NAME = "UUID Generator"  # Internal name, used in NODE_CLASS_MAPPINGS
    NODE_DISPLAY_NAME = "Generate UUID String"  # Name the user sees

    # Define the input types the node accepts
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},  # No required inputs to generate a random UUID
            "optional": {
                # The 'trigger' here doesn't affect the UUID (uuid4 is random)
                # but allows the user to change a value to force
                # re-execution of the node if needed.
                "trigger": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "prefix": ("STRING", {"default": "", "multiline": False}),
                "suffix": ("STRING", {"default": "", "multiline": False}),
            }
        }

    # Define the output types the node produces
    RETURN_TYPES = ("STRING",)
    # Optional: names for the outputs (if there's more than one, it's more useful)
    RETURN_NAMES = ("uuid_string",)

    # Define the main function that will be executed
    FUNCTION = "generate_uuid"

    # Define the category where the node will appear in ComfyUI's menu
    CATEGORY = "utils/text"  # You can change "utils/text" to your preference

    # Indicates if this node is a final output node (like SaveImage)
    # In this case, it is not.
    OUTPUT_NODE = False

    def __init__(self):  # E302: expected 2 blank lines, found 1
        self.value = None  # E261: at least two spaces before inline comment
        self.another_value = 0  # E261: at least two spaces before inline comment
        self.some_flag = True  # E261: at least two spaces before inline comment
        self.last_value = False  # E261: at least two spaces before inline comment

    def reset(self):
        pass

    def get_value(self):
        return self.value  # E261: at least two spaces before inline comment

    def generate_uuid(self, trigger=0, prefix="", suffix=""):
        """
        Generates a v4 UUID and returns it as a string, optionally with a prefix and suffix.
        The 'trigger' parameter is not used for UUID generation itself,
        but changing it can force ComfyUI to re-run this node.
        """
        # Generate a random v4 UUID
        generated_uuid = str(uuid.uuid4())

        # Concatenate with prefix and suffix if provided
        result_string = f"{prefix}{generated_uuid}{suffix}"

        # ComfyUI nodes must return a tuple of results
        return (result_string,)


# --- Mappings for ComfyUI to recognize the node ---
# This dictionary maps an internal name (key) to the node class (value).
NODE_CLASS_MAPPINGS = {
    "UUIDGeneratorNode": UUIDGeneratorNode  # "UUIDGeneratorNode" is the name used in saved workflows (JSON)
}

# This dictionary maps the internal name to a human-readable name for the UI.
# Optional, but recommended for clarity.
NODE_DISPLAY_NAME_MAPPINGS = {
    "UUIDGeneratorNode": "Generate UUID String"
}

# Message for the console when the script is loaded (optional)
print("--- Custom Node: UUID Generator loaded ---")