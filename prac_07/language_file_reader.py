"""CP1404 Practical 07"""

import csv
from programming_language import ProgrammingLanguage

def main():
    languages = load_languages()
    if not languages:
        print("No languages loaded.")
        return
    for language in languages:
        print(language)

def load_languages(filename="languages.csv"):
    languages = []
    try:
        with open(filename, newline='', encoding='utf-8') as in_file:
            reader = csv.reader(in_file)
            header = next(reader, None)
            for row in reader:
                if not row:
                    continue
                name = row[0].strip()
                typing = row[1].strip()
                reflection = (row[2].strip().lower() == "yes")
                year = int(row[3].strip())
                pointer_arithmetic = False
                if len(row) >= 5:
                    pointer_arithmetic = (row[4].strip().lower() == "yes")
                language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
                languages.append(language)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return languages

main()