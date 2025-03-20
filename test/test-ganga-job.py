import os
from GangaCore.GPI import Executable, Job, File, ArgSplitter, CustomMerger
import sys
sys.path.insert(0, '/root/GSoC/src')

# Create counter.sh in the current directory
counter_script = """#!/bin/bash
set -e  # Exit on error
echo "Processing PDF file: $1"

# Check if input file exists
if [ ! -f "$1" ]; then
    echo "Error: Input file $1 not found"
    exit 1
fi

# Check if pdftotext is installed
if ! command -v pdftotext &> /dev/null; then
    echo "Error: pdftotext not found. Please install poppler-utils"
    exit 1
fi

# Process the PDF file
pdftotext "$1" - | sed -e 's/ /\n/g' | grep -ci 'it'
"""

# Create script in current working directory
script_path = os.path.abspath("counter.sh")
with open(script_path, "w") as f:
    f.write(counter_script)
os.chmod(script_path, 0o755)

# Set up the job
job = Job()
job.application = Executable()
job.application.exe = File(script_path)

# Create test directory and files if they don't exist
test_dir = os.path.join(os.path.dirname(__file__), "split_pages")
os.makedirs(test_dir, exist_ok=True)

# Generate paths for PDF files
args = [[os.path.abspath(os.path.join(test_dir, f"page_{i}.pdf"))] for i in range(1, 30)]
filelist = [arg[0] for arg in args]

# Configure job
job.application.args = filelist
job.splitter = ArgSplitter(args=args)
job.inputfiles = filelist
job.backend = "Local"

# Configure merger with ignore failed flag
job.postprocessors = CustomMerger(
    module=os.path.abspath("./gangagsoc/merger.py"),
    ignorefailed=True  # Add this flag to handle failed jobs
)

# Submit the job
job.submit()