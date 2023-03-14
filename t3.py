import os

def get_contents_of_one_file(file_content):
    file_values = set()
    for row in file_content.split("\n")[1:-1]:
        values = row.split(",")
        file_values.add(values[-2])
    return file_values

def read_files():
    file_names = os.listdir("weatherfiles")

    # file_reader = open("main.py", "r")
    # file_content = file_reader.read()
    # file_reader.close()

    file_values = set()
    for file_name in file_names:
        with open(f"weatherfiles/{file_name}", "r") as file_reader:
            file_content = file_reader.read()
            file_values |= get_contents_of_one_file(file_content)
            file_reader.close()
    return file_values

unique_events = read_files()

print("Unique Events \n ↓↓↓↓↓↓↓↓")
for event in unique_events:
    print(event)
