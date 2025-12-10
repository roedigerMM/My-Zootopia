import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")

def display_animal_info(animal_data):
    """ Displays information about an animal """
    for animal in animal_data:
        if "name" in animal:
            print(f"\nName: {animal['name']}")
        if "diet" in animal["characteristics"]:
            print(f"Diet: {animal['characteristics']['diet']}")
        if "locations" in animal and len(animal["locations"]) > 0:
            print(f"Location: {animal['locations'][0]}")
        if "type" in animal["characteristics"]:
            print(f"Type: {animal['characteristics']['type']}")

display_animal_info(animals_data)
