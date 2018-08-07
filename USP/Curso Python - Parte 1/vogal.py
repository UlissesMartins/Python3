def vogal(z):
    if not isinstance(z, str) or len(z) != 1:
        return False

    vogais = ["a", "e", "i", "o", "u"]
    return z.lower() in vogais
