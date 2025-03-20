#!/bin/bash
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
pdftotext "$1" - | sed -e 's/ /
/g' | grep -ci 'it'
