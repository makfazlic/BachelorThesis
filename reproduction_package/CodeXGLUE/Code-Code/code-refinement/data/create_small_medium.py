import os

small_files = os.listdir('./small')
medium_files = os.listdir('./medium')

os.mkdir('./merged')

assert len(small_files) == len(medium_files)

for small_file, medium_file in zip(small_files, medium_files):
    print("Opened files: ", small_file, medium_file)
    with open('./small/' + small_file, 'r') as f:
        small_lines = f.readlines()
    with open('./medium/' + medium_file, 'r') as f:
        medium_lines = f.readlines()
    merged = small_lines + medium_lines
    with open('./merged/' + small_file, 'w') as f:
        f.writelines(merged)
    print("Merged files: ", small_file, medium_file, "into", "./merged/" + small_file)
