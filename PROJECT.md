# GSoC 2025 Ganga Project Implementation

## Setup and Environment
I set up the project environment following these steps:
1. Created a private duplicate of the GangaGSoC2025 repository
2. Added collaborators: @egede, @alexanderrichards, @mesmith75
3. Set up Python virtual environment:
```bash
python3 -m venv GSoC
cd GSoC/
. bin/activate
python -m pip install --upgrade pip wheel setuptools
python -m pip install -e git+https://github.com/YOUR-GITHUB-USERNAME-HERE/GangaGSoC2025#egg=gangagsoc
```

## Communication
- Created CERN guest account
- Joined Ganga Team on MatterMost
- Joined GSoC2025 channel
- Introduced myself to the community

## Task 1: Ganga Initial Task

### Hello World Implementation
Created a basic Ganga job test in `test/test_hello_world.py`:
```python

```

### PDF Processing Implementation
1. **PDF Splitting Job**
   - Implemented in `split-pdf.py`
   - Uses PyPDF2 to split PDF into individual pages
   - Output stored in `split_pages/` directory

2. **Word Counting Job**
   - Implemented word counting in `counter.sh`
   - Used ArgSplitter for parallel processing
   - Created merger in `merger.py` to combine results

3. **Tests**
   - - `test/test_ganga_job.py`: Test implementation for PDF processing
   - Located in `test/` directory
   - Tests PDF splitting, word counting, and merging
   - Includes job completion verification
   - GitHub Actions configured to run tests automatically

### Running Instructions
1. Run the Ganga job:
```bash
cd /root/GSoC/src/gangagsoc
ganga test/test_ganga_job.py
```
2. Run PDF processing tests:
```bash
cd /root/GSoC/src/gangagsoc
python -m unittest test/test_ganga_job.py -v
```

## Task 2: LLM Integration

### Implementation Files
- `Ai_part/generate_pi_code.py`: Handles Gemini API interaction
- `Ai_part/test_AI.py`: Tests LLM-generated code execution in Ganga

### LLM Integration Components
1. **Gemini API Integration**
   - Implemented in `Ai_part/generate_pi_code.py`
   - Uses Google's Gemini API for code generation
   - Handles API authentication and response parsing

2. **PI Calculation Implementation**
   - Generated code stored in `generated_pi_program.py`
   - Implements Monte Carlo method for PI calculation
   - Splits computation into subjobs

3. **Testing Framework**
   - Test implementation in `Ai_part/test_AI.py`
   - Verifies code generation and execution
   - Tests Ganga job submission functionality

4. **Django Web Interface**
   - Located in `llm_project/` directory
   - Simple HTTP server on localhost
   - Handles LLM queries and displays responses
   - Screenshots/demo video available in `docs/` directory

### Testing Instructions
1. Run Ganga tests:
```bash
cd /root/GSoC/src/gangagsoc
python -m unittest
```

2. Test LLM integration:
```bash
cd /root/GSoC/src/gangagsoc/Ai_part
python test_AI.py
```

3. Start Django app:
```bash
cd /root/GSoC/src/llm_project
python manage.py runserver
```

## Dependencies
Added to setup.py:
- google-generativeai
- django
- pypdf2
- python-dotenv

## Project Structure
```
gangagsoc/
├── Ai_part/
│   ├── generate_pi_code.py
│   └── test_AI.py
├── llm_project/
│   └── manage.py
├── test/
│   └── test_*.py
└── setup.py
```
