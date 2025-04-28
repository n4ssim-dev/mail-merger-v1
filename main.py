# 1. Read names and clean them (keeping your original code)
with open('./Input/Names/invited_names.txt', mode="r") as name_file:
    names = name_file.readlines()
    cleaned_names = [name.strip() for name in names]  # Removes \n and whitespace

# 2. Read the starting letter TEMPLATE (read-only, no modifications)
with open('./Input/Letters/starting_letter.txt', mode="r") as letter_file:
    original_letter = letter_file.read()  # Preserves original content

# 3. Create personalized letters in ReadyToSend folder
for name in cleaned_names:
    # Create a new modified version (leaving original_letter unchanged)
    personalized_letter = original_letter.replace("[name]", name)

    # Save to Output folder with unique filename
    output_path = f"./Output/ReadyToSend/letter_for_{name}.txt"
    with open(output_path, mode="w") as output_file:
        output_file.write(personalized_letter)

print(f"Generated {len(cleaned_names)} letters in /Output/ReadyToSend/")