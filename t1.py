import os


def get_contents_of_one_file(file_content):
    file_values = []
    for row in file_content.split("\n")[1:-1]:
        file_values.append(row.split(","))

    return file_values


def read_files():
    file_names = os.listdir("weatherfiles")

    # file_reader = open("main.py", "r")
    # file_content = file_reader.read()
    # file_reader.close()

    file_values = []

    for file_name in file_names:
        with open(f"weatherfiles/{file_name}", "r") as file_reader:
            file_content = file_reader.read()

            file_values += get_contents_of_one_file(file_content)
            file_reader.close()

    return file_values


file_values = read_files()

temperatures = {}
for file_value in file_values:
    if file_value and file_value[1]:
        temperatures[file_value[0]] = float(file_value[1])

min_temp = None
min_temp_year = None

for year, temp in temperatures.items():
    if min_temp is None or temp < min_temp:
        min_temp = temp
        min_temp_year = year

print("Minimum temperature C:", min_temp, "in", min_temp_year)