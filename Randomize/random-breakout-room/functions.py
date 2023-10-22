import pandas as pd



def printList(groups): 
  for i, group in enumerate(groups, start=1):
    print(f"Kelompok {i}: {', '.join(group)}")

def exportGroupDataToExcel(groups):
  grouped_data = {}
  for i, group in enumerate(groups, start=1):
      grouped_data[f"Kelompok {i}"] = group

  max_group_size = max(len(group) for group in grouped_data.values())
  for group in grouped_data.values():
      group.extend([''] * (max_group_size - len(group)))

  grouped_df = pd.DataFrame(grouped_data)

  grouped_file_path = 'Randomize_result.xlsx'
  grouped_df.to_excel(grouped_file_path, index=False, engine='openpyxl')

def createGroupDataFromDataframe(FILE_PATH, column_name, group_size):
  data_frame = pd.read_excel(FILE_PATH, engine='openpyxl')

  groups = []
  current_group = []

  for index, row in data_frame.iterrows():
    current_group.append(row[column_name])
    if(len(current_group) == group_size):
      groups.append(current_group.copy())
      current_group.clear()

  if current_group:
    groups.append(current_group)

  return groups