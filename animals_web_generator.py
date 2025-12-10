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

def get_html_template():
    """ Returns the HTML template """
    with open("animals_template.html", "r") as template:
       return template.read()

def get_animals_data(animal_data):
    """ Returns the animals data """
    output = ""
    for animal in animal_data:
        if "name" in animal:
            output += f"Name: {animal['name']}\n"
        if "diet" in animal["characteristics"]:
            output += f"Diet: {animal['characteristics']['diet']}\n"
        if "locations" in animal and len(animal["locations"]) > 0:
            output += f"Location: {animal['locations'][0]}\n"
        if "type" in animal["characteristics"]:
            output += f"Type: {animal['characteristics']['type']}\n"
        output += "\n"
    return output

def create_new_html_string():
    """ Creates a new HTML string """
    html_template = get_html_template()
    animal_data = get_animals_data(animals_data)
    new_html_string = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_data)
    return new_html_string

def write_new_html_file():
    """ Writes a new HTML file """
    html_content = create_new_html_string()
    with open("animals.html", "w") as new_file:
        new_file.write(html_content)

write_new_html_file()