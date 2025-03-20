from Ganga.Core import Job, Splitter, OutputFile
from Ganga.Lib.File import File
import random
import math

# Define the number of simulations per subjob and the total number of simulations
simulations_per_subjob = 1000
total_simulations = 1000000
num_subjobs = total_simulations // simulations_per_subjob


# Python script to run the simulation and calculate Pi
script = """
import random
import math

def estimate_pi(n):
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_estimate = 4 * inside_circle / n
    return pi_estimate

n_simulations = {simulations_per_subjob}  # Use the variable defined outside
pi_approx = estimate_pi(n_simulations)

# Save the result to a file
with open('pi_result.txt', 'w') as f:
    f.write(str(pi_approx))
""".format(simulations_per_subjob=simulations_per_subjob)  # Inject the value

# Create a temporary file to store the script
with open('estimate_pi.py', 'w') as f:
    f.write(script)


# Define the job
j = Job(name='Pi_Estimation_Simulation')

# Set the application to run
j.application = Executable(exe=File('estimate_pi.py'))

# Define the splitter to create subjobs
j.splitter = Splitter(
    type='NumberOfSubjobs',
    args={'subjobs': num_subjobs}
)


# Backend selection (replace with your desired backend)
j.backend = Local()  # Or e.g., LCG()

# Define output files to retrieve
j.outputfiles = [OutputFile('pi_result.txt')]

# Submit the job
j.submit()

# Print job ID for monitoring
print(f"Job submitted with ID: {j.id}")



# --- Aggregation Script (to be run after job completion) ---
aggregation_script = """
import os
import sys

def aggregate_pi_values(directory):
    pi_values = []
    for filename in os.listdir(directory):
        if filename.startswith('pi_result.txt'):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as f:
                    pi_value = float(f.read().strip())
                    pi_values.append(pi_value)
            except (FileNotFoundError, ValueError) as e:
                print(f"Error reading file {filename}: {e}")

    if not pi_values:
        print("No valid pi_result.txt files found.")
        return None

    average_pi = sum(pi_values) / len(pi_values)
    return average_pi

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python aggregate_results.py <job_output_directory>")
        sys.exit(1)

    output_directory = sys.argv[1]
    estimated_pi = aggregate_pi_values(output_directory)

    if estimated_pi is not None:
        print(f"Estimated value of Pi: {estimated_pi}")

"""

# Create aggregation script file
with open('aggregate_results.py', 'w') as f:
    f.write(aggregation_script)

print("Aggregation script 'aggregate_results.py' created.")
print("After the Ganga job completes, run the aggregation script from the command line:")
print("  python aggregate_results.py <job_output_directory>")
print("  (Replace <job_output_directory> with the Ganga job's output directory, e.g., 'job_<job_id>/output/')")