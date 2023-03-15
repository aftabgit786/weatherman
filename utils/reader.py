import os

def get_contents_for_events(file_content):
    file_values = set()
    for row in file_content.split("\n")[1:-1]:
        values = row.split(",")
        file_values.add(values[-2])
    return file_values


def get_contents_of_one_file(file_content):
    file_values = []
    for row in file_content.split("\n")[1:-1]:
        file_values.append(row.split(","))

    return file_values


def read_files():
    dir_path = os.path.dirname(os.path.realpath("weatherman.weatherfiles/"))
    weatherfiles_path = os.path.join(dir_path, '..', 'weatherfiles')

    file_names = os.listdir(weatherfiles_path)

    file_values = []

    for file_name in file_names:
        with open(os.path.join(weatherfiles_path, file_name), "r") as file_reader:
            file_content = file_reader.read()

            file_values += get_contents_of_one_file(file_content)
            file_reader.close()

    return file_values

def read_files_for_events():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    weatherfiles_path = os.path.join(dir_path, '..', 'weatherfiles')

    file_names = os.listdir(weatherfiles_path)

    file_values = set()
    for file_name in file_names:
        with open(os.path.join(weatherfiles_path, file_name), "r") as file_reader:
            file_content = file_reader.read()
            file_values |= get_contents_for_events(file_content)
            file_reader.close()
    return file_values

