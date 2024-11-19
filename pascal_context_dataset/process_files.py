import json
import random

def process_and_split_files(input_file1, input_file2, output_file1, output_file2):
    # Read and combine input files
    entries = []
    for input_file in [input_file1, input_file2]:
        with open(input_file, 'r') as infile:
            for line in infile:
                if ": " in line:
                    file_name, prompt = line.strip().split(": ", 1)
                    entries.append({"file_name": file_name, "prompt": prompt})
    
    # Shuffle entries for randomness
    random.shuffle(entries)
    
    # Split into 80% and 20%
    split_index = int(len(entries) * 0.8)
    train_entries = entries[:split_index]
    test_entries = entries[split_index:]
    
    # Format entries as JSON objects
    def format_entries(entries):
        return [
            {
                "source": f"VOCdevkit/VOC2012/JPEGImages/{entry['file_name']}",
                "target": f"VOCdevkit/VOC2012/SegmentationClass/{entry['file_name']}",
                "prompt": entry["prompt"]
            }
            for entry in entries
        ]
    
    # Save entries to output files with one JSON object per line
    def save_minimal_json(output_file, data):
        with open(output_file, 'w') as outfile:
            for entry in data:
                outfile.write(f"{json.dumps(entry)}\n")
    
    save_minimal_json(output_file1, format_entries(train_entries))
    save_minimal_json(output_file2, format_entries(test_entries))

# Specify input and output files
input_file1 = 'train_prompts.txt'
input_file2 = 'val_prompts.txt'
output_file1 = 'prompt.json'
output_file2 = 'prompt_20.json'

# Run the function
process_and_split_files(input_file1, input_file2, output_file1, output_file2)

print(f"Train output saved to {output_file1}")
print(f"Test output saved to {output_file2}")
