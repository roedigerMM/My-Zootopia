def get_html_template():
    """ Reads and returns the HTML template """
    with open("animals_template.html", "r") as template:
       return template.read()

def create_new_html_string(formatted_animals_data):
    """ Creates a new HTML string with the animals data inserted into the HTML template """
    html_template = get_html_template()
    new_html_string = html_template.replace("__REPLACE_ANIMALS_INFO__", formatted_animals_data)
    return new_html_string

def write_new_html_file(formatted_animals_data):
    """ Writes the content to a new HTML file """
    html_content = create_new_html_string(formatted_animals_data)
    with open("animals.html", "w") as new_file:
        new_file.write(html_content)