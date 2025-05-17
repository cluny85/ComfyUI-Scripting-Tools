import uuid


class EnhancedUUIDGeneratorNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "uuid_type": (["UUID1", "UUID3", "UUID4", "UUID5"], {"default": "UUID4"}),
                "namespace_type": (["DNS", "URL", "OID", "X500", "CUSTOM"], {"default": "DNS"}),
                "name_string": ("STRING", {"default": "example.com"}),
                "trigger": ("INT", {"default": 0, "min": 0, "max": 1}),
            },
            "optional": {
                "custom_namespace_uuid": ("STRING", {"default": ""}),
                "prefix": ("STRING", {"default": ""}),
                "suffix": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_uuid_enhanced"
    CATEGORY = "ComfyUI-Scripting-Tools"

    def get_namespace(self, namespace_type, custom_namespace_uuid_str):
        if namespace_type == "DNS":
            return uuid.NAMESPACE_DNS
        elif namespace_type == "URL":
            return uuid.NAMESPACE_URL
        elif namespace_type == "OID":
            return uuid.NAMESPACE_OID
        elif namespace_type == "X500":
            return uuid.NAMESPACE_X500
        elif namespace_type == "CUSTOM":
            try:
                return uuid.UUID(custom_namespace_uuid_str)
            except ValueError:
                raise ValueError("Invalid custom namespace UUID string.")
        else:
            raise ValueError("Invalid namespace type.")

    def generate_uuid_enhanced(
        self,
        uuid_type,
        namespace_type="DNS",
        custom_namespace_uuid="",
        name_string="example.com",
        prefix="",
        suffix="",
        trigger=0,
    ):
        # Siempre genera el UUID, ignora trigger
        if uuid_type == "UUID1":
            generated_uuid = uuid.uuid1()
        elif uuid_type == "UUID4":
            generated_uuid = uuid.uuid4()
        elif uuid_type == "UUID3":
            namespace = self.get_namespace(namespace_type, custom_namespace_uuid)
            generated_uuid = uuid.uuid3(namespace, name_string)
        elif uuid_type == "UUID5":
            namespace = self.get_namespace(namespace_type, custom_namespace_uuid)
            generated_uuid = uuid.uuid5(namespace, name_string)
        else:
            raise ValueError("Invalid UUID type")

        result = f"{prefix}{str(generated_uuid)}{suffix}"
        return (result,)  # ComfyUI expects a tuple


# --- Mapeo para que ComfyUI reconozca el nodo ---
NODE_CLASS_MAPPINGS = {
    "EnhancedUUIDGeneratorNode": EnhancedUUIDGeneratorNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EnhancedUUIDGeneratorNode": "Enhanced UUID Generator"
}
