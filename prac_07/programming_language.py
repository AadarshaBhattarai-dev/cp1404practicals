"""CP1404 Practical 07"""

class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year, pointer_arithmetic=False):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        return (f"ProgrammingLanguage(name={self.name!r}, typing={self.typing!r}, "
                f"reflection={self.reflection}, year={self.year}, "
                f"pointer_arithmetic={self.pointer_arithmetic})")

    def __str__(self):
        refl = "Yes" if self.reflection else "No"
        ptr = "Yes" if self.pointer_arithmetic else "No"
        return (f"{self.name}, {self.typing} Typing, Reflection={refl}, "
                f"Pointer Arithmetic={ptr}, First appeared in {self.year}")

    def is_dynamic(self):
        return self.typing.lower() == "dynamic"

    def supports_pointer_arithmetic(self):
        return bool(self.pointer_arithmetic)


def run_tests():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    cpp = ProgrammingLanguage("C++", "Static", False, 1983, True)

    languages = [ruby, python, cpp]
    for lang in languages:
        print(lang)

    print("\nDynamically typed languages:")
    for lang in languages:
        if lang.is_dynamic():
            print(f"- {lang.name}")