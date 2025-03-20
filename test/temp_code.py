from Ganga.GPI import *
import random
import math

# Number of total simulations and simulations per subjob
TOTAL_SIMULATIONS = 1000000
SIMULATIONS_PER_SUBJOB = 1000
NUM_SUBJOBS = TOTAL_SIMULATIONS // SIMULATIONS_PER_SUBJOB


# Python function to estimate Pi using Monte Carlo method
def estimate_pi(n):
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_estimate = 4 * inside_circle / n
    return pi_estimate


# Ganga job script
script = """
import random
import sys

def estimate_pi(n):
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_estimate = 4 * inside_circle / n
    return pi_estimate

n_simulations = int(sys.argv[1])
pi_approximation = estimate_pi(n_simulations)

# Write the result to a file. Ganga will automatically collect this.
with open('pi_result.txt', 'w') as f:
    f.write(str(pi_approximation))
"""

# Create a Job object
job = Job(name='PiApproximation')

# Set the application to be a script execution
job.application = Executable(exe=File(''), script=script)

# Set the arguments for the script (number of simulations)
job.application.args = [SIMULATIONS_PER_SUBJOB]

# Backend configuration (choose a backend based on your setup)
# Example: Local backend
# job.backend = Local()

# Example: LSF backend
# job.backend = LSF()

# Example: Dirac backend
#job.backend = Dirac()
#job.backend.settings['BannedSites'] = ['LCG.IN2P3-CC.fr']


# Define the splitter
job.splitter = ArgSplitter(args=[str(SIMULATIONS_PER_SUBJOB)] * NUM_SUBJOBS)


# Output files
job.outputfiles = [LocalFile('pi_result.txt')]

# Submit the job
job.submit()

# Monitor the job (optional)
print("Job submitted. Job ID:", job.id)

# Add a function to aggregate results automatically
def aggregate_pi_estimates(jobid):
    """Aggregates Pi estimates from subjobs and prints the final estimate."""
    try:
        j = Job(jobid)
    except:
        print(f"Job with ID {jobid} not found")
        return

    if j.status != 'completed':
        print(f"Job {jobid} is not completed yet.")
        return

    pi_estimates = []
    for sj in j.subjobs:
        try:
            with open(sj.outputdir + '/pi_result.txt', 'r') as f:
                pi_estimates.append(float(f.read()))
        except Exception as e:
            print(f"Error reading result from subjob {sj.id}: {e}")
            continue

    if not pi_estimates:
        print("No valid Pi estimates found in the output files.")
        return

    final_pi_estimate = sum(pi_estimates) / len(pi_estimates)
    print(f"Final Pi estimate: {final_pi_estimate}")

# Example usage:  After the job is completed, you can run:
# aggregate_pi_estimates(job.id)