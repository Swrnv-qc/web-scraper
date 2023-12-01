file_path = 'output.txt'
target_start = "Adult"
target_end = "."

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

start_index = content.find(target_start)
end_index = content.find(target_end, start_index)

if start_index != -1 and end_index != -1:
    result_substring = content[start_index:end_index + 1]
    print(f"Substring: {result_substring}")
else:
    print("Target substring not found in the file.")
