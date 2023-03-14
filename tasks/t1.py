from weatherman.utils.reader import read_files

file_values = read_files()

temperatures = {}
for file_value in file_values:
    if file_value and file_value[1]:
        temperatures[file_value[0]] = float(file_value[1])

min_temp_year = min(temperatures, key=temperatures.get)
max_temp_year = max(temperatures, key=temperatures.get)

print("Minimum temperature C:", temperatures[min_temp_year], "in", min_temp_year)
print("Maximum temperature C:", temperatures[max_temp_year], "in", max_temp_year)

