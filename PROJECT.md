<<<<<<< HEAD
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
### to run tests within the test directory
```
cd /root/GSoC/src/gangagsoc
python -m venv ~/venv
source ~/venv/bin/activate
pip install -e .
pip install -r requirements.txt
python -m pytest test 
```
or 
```pytest test/ -v```

## Communication
- Created CERN guest account
- Joined Ganga Team on MatterMost
- Joined GSoC2025 channel
- Introduced myself to the community

## Task 1: Ganga Initial Task

### Hello World Implementation
![Hello World Ganga](src/gangagsoc/docs/hello-world-showcase.png)


### PDF Processing Implementation
1. **PDF Splitting Job**
   - Implemented in `split-pdf.py`
   - Uses PyPDF2 to split PDF into individual pages
   - Output stored in `split_pages/` directory
   - split using `python split-pdf.py LHC.pdf `


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

![Snapshot of ganga jobs running](src/gangagsoc/docs/image.png)

### Running Instructions
1. Run the Ganga job:
```bash
cd /root/GSoC/src/gangagsoc
```
2. Run PDF processing tests:
```bash
cd /root/GSoC/src/gangagsoc
python test/test_ganga_job.py 
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
   - Verifies code generation
   - output stored at `temp_code.py`

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

2. Start Django app:
```bash
cd /root/GSoC/src/llm_project
python manage.py runserver
```
![Minimal Chat App](src/gangagsoc/docs/frontend-django-chat.png)
![LLM generated code](src/gangagsoc/docs/response.png)

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
=======


>>>>>>> master
