import hashlib
import random

salts = [
    "0a1b2c3d4e5f6g7h",
    "0i8j9k0l1m2n3o4p",
    "0q5r6s7t8u9v0w1x",
    "0y2z3a4b5c6d7e8f",
    "0g9h0i1j2k3l4m5n",
    "0o6p7q8r9s0t1u2v",
    "0w3x4y5z6a7b8c9d",
    "0e0f1g2h3i4j5k6l",
    "0m7n8o9p0q1r2s3t",
    "0u4v5w6x7y8z9a0b",
    "0c1d2e3f4g5h6i7j",
    "0k8l9m0n1o2p3q4r",
    "0s5t6u7v8w9x0y1z",
    "0a2b3c4d5e6f7g8h",
    "0i9j0k1l2m3n4o5p",
    "0q6r7s8t9u0v1w2x",
    "0y3z4a5b6c7d8e9f",
]


class HashCore:
    def __init__(self) -> None:
        pass

    def sl(self, inp):
        try:
            sa = random.choice(salts)
            s = inp + sa
            return s
        except Exception as e:
            return f"[x] Ошибка получения солей {e}"

    def hech_md5(self, inp):
        try:
            res = hashlib.md5(inp.encode()).hexdigest()
            return res
        except Exception as e:
            return f"[x] Ошибка хеширования {e}"

    def hech_SHA1(self, inp):
        try:
            res = hashlib.sha1(inp.encode()).hexdigest()
            return res
        except Exception as e:
            return f"[x] Ошибка хеширования {e}"

    def hech_SHA2(self, inp):
        try:
            res = hashlib.sha256(inp.encode()).hexdigest()
            return res
        except Exception as e:
            return f"[x] Ошибка хеширования {e}"

    def hech_SHA512(self, inp):
        try:
            res = hashlib.sha512(inp.encode()).hexdigest()
            return res
        except Exception as e:
            return f"[x] Ошибка хеширования {e}"
