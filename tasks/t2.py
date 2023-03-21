from weatherman.utils.reader import read_files_for_t2

file_values = read_files_for_t2()

temperatures = {}
for file_value in file_values:
    if len(file_value) >= 4 and file_value[1] and file_value[3]:
        temperatures[file_value[0]] = (float(file_value[1]), float(file_value[3]))

dates_with_difference_of_7 = set()
for date1, temp1 in temperatures.items():
    for date2, temp2 in temperatures.items():
        if date1 < date2 and abs(temp1[0] - temp2[1]) == 7:
            dates_with_difference_of_7.add((date1, date2))

if dates_with_difference_of_7:
    print("Dates with a difference of exactly 7 between Min and Max TemperatureC:")
    for date1, date2 in dates_with_difference_of_7:
        print(date1, "and", date2)
else:
    print("No dates found")
