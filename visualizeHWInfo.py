import pandas as pd
import os
import matplotlib.pyplot as plt
import chardet

# get current directory location
current_dir = os.getcwd()

# get list of files in current directory
current_dir_files = [item for item in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, item)) and (item.endswith(".csv") or item.endswith(".CSV"))]

# display the list to the user
if len(current_dir_files) == 0:
    print("No csv files found!!!. Exiting...")
    os._exit()
for (idx, file) in enumerate(current_dir_files):
    print(f"{idx}) {file} \n")

# get the user input for which file
print("Please enter 1 option: \n")
selected_file_option = None
try:
    selected_file_option = int(input())
except ValueError:
    print("Value Error")
    os._exit()
print(f"The selected option is: {selected_file_option}")
selected_file_path = os.path.join(current_dir, current_dir_files[selected_file_option])

# get the csv file encoding
with open(selected_file_path, 'rb') as file:
    file_encodig = chardet.detect(file.read())
print(file_encodig)

# load the file using pandas
selected_csv_file = pd.read_csv(selected_file_path, encoding=file_encodig["encoding"])

# get all the columns and display it to the user
# ask the user to select 1 or more columns from the list
print("Please select 1 or more columns by enter their index with spaces in-between, then when you are done press enter: ")
for (idx, col_name) in enumerate(selected_csv_file.columns):
    print(f"{idx} {col_name}")
try:
    selected_columns = list(map(int, input().split()))
except ValueError:
    print("Value Error")
    os._exit()
print(f"The selected columns are: {selected_columns}")

# visualize the data 
# (x-axis is time y is arbitary and based on selected column)
selected_csv_file[selected_csv_file.columns[selected_columns]].plot(kind="line", figsize=(10, 6))
plt.title("HWInfo data")
plt.xlabel("Time")
plt.ylabel("Column Unit")
plt.show()