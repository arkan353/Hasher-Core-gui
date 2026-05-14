from model.hec import HashCore


class Controller:
    def __init__(self):
        self.core = HashCore()

    def compute_hash(self, method_name, text):
        method = getattr(self.core, method_name, None)
        if method is None:
            return "[x] Метод не найден"
        return method(text)

    def get_available_methods(self):
        return [
            {"name": "sl", "label": "Dynamic Salt"},
            {"name": "hech_md5", "label": "MD5"},
            {"name": "hech_SHA1", "label": "SHA-1"},
            {"name": "hech_SHA2", "label": "SHA-256"},
            {"name": "hech_SHA512", "label": "SHA-512"},
        ]
