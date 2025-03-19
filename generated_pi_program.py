```python
# Ganga script to approximate Pi using accept-reject method

from Ganga.Core import *
import random

# Number of simulations per subjob
simulations_per_job = 1000
# Total number of simulations
total_simulations = 1000000
# Number of subjobs
n_subjobs = total_simulations // simulations_per_job

# Python script that performs the Pi approximation
pi_script = """
import random

def estimate_pi(n_points):
    inside_circle = 0
    for _ in range(n_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_estimate = 4 * (inside_circle / n_points)
    return pi_estimate

n_points = {simulations_per_job}
pi_approx = estimate_pi(n_points)

# Print the result so that Ganga can capture it
print(f"Pi Approximation: {pi_approx}")
""".format(simulations_per_job=simulations_per_job)


# Create a job
j = Job(name='Pi_Approximation')

# Define the backend
j.backend = Local()  # Or use your preferred backend like LSF, PBS, etc.

# Define the application
j.application = Executable(exe=File("pi_estimator.py"), script=pi_script)
j.application.args = []  # No need for command-line arguments

# Create a Python file with the script
with open("pi_estimator.py", "w") as f:
    f.write(pi_script)

j.inputsandbox = ['pi_estimator.py']

# Splitting the job into subjobs
j.splitter = SplitByFiles(filesPerJob=1) #dummy, as we already embed everything into the python script

# Create a list of input files (dummy files to control the number of subjobs). Ganga requires a splitter, even though we hardcode the number of events in the embedded script.
import os
input_files = []
for i in range(n_subjobs):
    file_name = f"dummy_{i}.txt"
    with open(file_name, "w") as f:
        f.write(f"Dummy file for subjob {i}")
    input_files.append(file_name)

j.inputsandbox.extend(input_files)

j.splitter.files = [File(f) for f in input_files]

# Cleanup input files
for f in input_files:
    os.remove(f)

# Define the merger to aggregate results
j.merger = RootMerger() #Dummy merger because the output is only a single line of text.

# Define the post-processing script to calculate the final Pi estimate

post_script = """
import os
import re

def aggregate_pi_estimates(output_dir):
    pi_estimates = []
    for filename in os.listdir(output_dir):
        if filename.startswith('stdout'):
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'r') as f:
                for line in f:
                    match = re.search(r"Pi Approximation: (\d+\.\d+)", line)
                    if match:
                        pi_estimates.append(float(match.group(1)))
                        break

    if not pi_estimates:
        print("No Pi estimates found in output files.")
        return None

    average_pi = sum(pi_estimates) / len(pi_estimates)
    return average_pi

output_dir = os.getcwd()
pi_estimate = aggregate_pi_estimates(output_dir)

if pi_estimate is not None:
    print(f"Final Pi Approximation: {pi_estimate}")
"""


# Define the postprocessor
j.postprocessors.append(RootPostProcessor(script=post_script)) #Dummy post processor becausethe output is a string

# Submit the job
j.submit()
```