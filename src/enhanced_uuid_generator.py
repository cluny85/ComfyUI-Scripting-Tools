import uuid


class EnhancedUUIDGeneratorNode:

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
                raise ValueError(
                    "Invalid custom namespace UUID string."
                )
        else:
            raise ValueError(
                "Invalid namespace type."
            )

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
        if trigger == 0:
            return None

        namespace = self.get_namespace(namespace_type, custom_namespace_uuid)

        if uuid_type == "UUID1":
            generated_uuid = uuid.uuid1()
        elif uuid_type == "UUID3":
            generated_uuid = uuid.uuid3(namespace, name_string)
        elif uuid_type == "UUID4":
            generated_uuid = uuid.uuid4()
        elif uuid_type == "UUID5":
            generated_uuid = uuid.uuid5(namespace, name_string)
        else:
            raise ValueError(
                "Invalid UUID type."
            )

        return f"{prefix}{generated_uuid}{suffix}"


# --- Mapeo para que ComfyUI reconozca el nodo ---
NODE_CLASS_MAPPINGS = {
    "EnhancedUUIDGeneratorNode": EnhancedUUIDGeneratorNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EnhancedUUIDGeneratorNode": "Enhanced UUID Generator"
}
