class Field:
    def __init__(self, path: str) -> None:
        self.path = path

    def __get__(self, instance, owner):

        keys = split(self.path)
        current = instance.payload
        for key in keys:
            if not isinstance(current, dict):
                return None

            if key not in current:
                return None

            current = current[key]
        return current

    def __set__(self, instance, value):
        keys = split(self.path)
        current = instance.payload

        for key in keys[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]

        current[keys[-1]] = value


class Model:
    def __init__(self, payload: dict):
        self.payload = payload

    name = Field("name")
    slug = Field("meta.slug")
    href = Field("meta.remote.href")


payload = {
    "name": "model-name",
    "meta": {
        "slug": "model-slug",
        "remote": {
            "href": "https://example.com"
        }
    }
}

model = Model(payload)

print(model.name)
print(model.slug)
print(model.href)

model.slug = "new-slug"
print(model.slug)
