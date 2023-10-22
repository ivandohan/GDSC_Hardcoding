import pandas as pd
import functions as fc

FILE_PATH = "Names.xlsx"
COLUMN_NAME = "Full Name"
GROUP_SIZE = 100

df = pd.read_excel(FILE_PATH, engine='openpyxl')

groups = fc.createGroupDataFromDataframe(FILE_PATH=FILE_PATH, column_name=COLUMN_NAME, group_size=GROUP_SIZE)

fc.exportGroupDataToExcel(groups=groups)




