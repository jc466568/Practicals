
from prac_06.programming_languages import ProgrammingLanguage
from random import randint

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [ruby, python, visual_basic]
# for a in x:
#     print(a)

print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.get_name(), language.year)

print(randint(1,10))