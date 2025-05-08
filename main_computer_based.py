import random
from data import random_replacements  # Importing your placeholder values
from data1 import category

# Sentence templates organized by category
categories = category

# State tracking
used_patterns = set()
used_templates = set()
last_category = None

def generate_sentence():
    global last_category
    attempts = 0

    while attempts < 1000:
        category_name = random.choice(list(categories.keys()))

        if category_name == last_category:
            attempts += 1
            continue

        template = random.choice(categories[category_name])

        if template in used_templates:
            attempts += 1
            continue

        sentence = template
        for placeholder in random_replacements:
            if f"{{{placeholder}}}" in sentence:
                sentence = sentence.replace(f"{{{placeholder}}}", random.choice(random_replacements[placeholder]))

        if sentence not in used_patterns:
            used_patterns.add(sentence)
            used_templates.add(template)
            last_category = category_name
            return sentence

        attempts += 1

    return "No unique sentence could be generated."

# Example usage
if __name__ == "__main__":
    print(generate_sentence())
