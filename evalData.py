import os
import matplotlib.pyplot as plt

# Folder containing .dat files
folder_path = "./data"  # Change this to your folder path

# Function to read the second and third columns from a .dat file
def read_dat_file(file_path):
    second_col, third_col = [], []
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.split()  # Split the line into columns
            if len(parts) >= 3:  # Ensure there are at least three columns
                second_col.append(float(parts[1].replace(',', '.')))
                third_col.append(float(parts[2].replace(',', '.')))
    return second_col, third_col

# Get all .dat files in the folder, sorted lexicographically
dat_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.dat')])

# Group files into 3 sets of 5 files and 1 set of 4 files
grouped_files = [dat_files[i:i + 5] for i in range(0, 15, 5)]
grouped_files.append(dat_files[15:])  # Remaining 4 files

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 10))  # 2x2 grid
axes = axes.flatten()  # Flatten the axes for easy indexing

# Plot each group in a separate subplot
for idx, group in enumerate(grouped_files):
    ax = axes[idx]
    for file in group:
        second_col, third_col = read_dat_file(os.path.join(folder_path, file))
        ax.plot(second_col, third_col, label=file)  # Plot second vs. third column
    ax.set_title(f"Group {idx + 1}")
    ax.set_xlabel("Second Column")
    ax.set_ylabel("Third Column")
    ax.legend()
    ax.grid()

# Adjust layout and display the plots
plt.tight_layout()
plt.show()

