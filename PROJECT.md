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
   - Implemented in `ganga -i test_split_merge.py`
   - Uses PyPDF2 to split PDF into individual pages
   - Output stored in `split_pages/` directory
   - split using `python split-pdf.py LHC.pdf `


2. **Word Counting Job**
   - Implemented word counting in `counter.sh`
   - Used ArgSplitter for parallel processing
   - Created merger in `mymerger.py` to combine results

3. **Tests**
   - - `test/test_ganga_job.py`: Test implementation for PDF processing
   - Located in `test/` directory
   - Includes job completion verification
   - GitHub Actions configured to run tests automatically

![Snapshot of ganga jobs running](src/gangagsoc/docs/image.png)
![28 jobs](src/gangagsoc/docs/28_jobs.png)


### Running Instructions
1. Run the Ganga job:
```bash
ganga -i test_split_merge.py
```
2. Run PDF processing tests:
```bash
cd /root/GSoC/src/gangagsoc
python test/test_ganga_job.py 
```

## Task 2: LLM Integration

### Implementation Files
- `Ai_part/generate_pi_code.py`: Handles Gemini API interaction
- `test/test_AI.py`: Asserts LLM Code generation ensuring correct pipeling, it generates a `temp_code.py`

### LLM Integration Components
1. **LLM Handler (generate_pi_code.py)**
   - Manages Gemini API communication
    - Handles API authentication and response parsing
   - Functions:
     - `generate_code()`: Gets PI calculation code from LLM
     - `parse_response()`: Extracts code from LLM response
   - Handles API authentication via environment variables

2. **PI Calculation Implementation**
    -can be seen in `test/temp_code.py`
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
   - Features:
     - Simple HTTP server (localhost)
     - Query input form
     - Response display
     - Code highlighting

### Testing Instructions

 Start Django app:
```bash
cd /Ai_part/llm_project
python manage.py runserver
```

![Minimal Chat App](src/gangagsoc/docs/frontend-django-chat.png)
![LLM generated code](src/gangagsoc/docs/response.png)

## Dependencies
```python
# Added to setup.py
install_requires=[
    'google-generativeai',
    'django>=4.2',
    'pypdf2',
    'python-dotenv',
]

## Project Structure
```
gangagsoc/
├── src/
│   └── gangagsoc/
│       ├── docs/                          # Documentation assets
│       │   ├── hello-world-showcase.png
│       │   ├── image.png
│       │   ├── 28_jobs.png
│       │   ├── frontend-django-chat.png
│       │   └── response.png
│       ├── split_pages/                   # Output directory for split PDFs
│       ├── split-pdf.py                   # PDF splitting script
│       ├── counter.sh                     # Word counting implementation
│       ├── mymerger.py                    # Results merger for word count
│       └── test_split_merge.py           # Main Ganga job implementation
├── Ai_part/
│   ├── generate_pi_code.py               # LLM API interaction handler
│   ├── test_AI.py                        # LLM code generation tests
│   └── temp_code.py                      # Generated PI calculation code
├── llm_project/                          # Django web application
│   ├── manage.py                         # Django management script
│   ├── chat/                             # Chat application
│   │   ├── views.py                      # Chat view handlers
│   │   ├── urls.py                       # URL routing
│   │   └── templates/                    # HTML templates
│   └── static/                           # Static assets
├── test/
│   ├── test_ganga_job.py                 # PDF processing tests
│   ├── test_AI.py                        # LLM integration tests
│   └── LHC.pdf                           # Test PDF file
├── setup.py                              # Project configuration
├── requirements.txt                       # Project dependencies
├── PROJECT.md                            # Project documentation
└── CV.pdf                                # Curriculum 
```
