import glob
import pandas as pd
from pathlib import Path

# Define the header
header = ['papercode', 'bookname', 'chapter', 'quizefile', 'displayfield']

# Directory path (current directory)
dir_path = Path('data/')
print(dir_path)

# Iterate over CSV files starting with 'quize_list'
for file_path in dir_path.glob('quiz_list*.csv'):
    # Read the CSV without headers
    df = pd.read_csv(file_path, header=None)
    print('Read:', file_path)
    # Assign the header
    df.columns = header
    
    # Save the file with the header
    df.to_csv(file_path, index=False)
    print('saved:', file_path)

