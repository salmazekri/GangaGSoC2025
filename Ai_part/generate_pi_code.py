import google.generativeai as genai
import os

# Configure the API with your key
genai.configure(api_key="AIzaSyBJrC0hdk7-x-pOOO4C2NNwsrP08hCWX9o")

# Create a model instance
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_pi_code():
    # Initialize chat history (short-term memory)
    chat_history = []

    # Define the task prompt specifically for Pi approximation with Ganga task splitting
    prompt = """
    I need to approximate the value of Pi using the accept-reject simulation method with Ganga. The program should:

    1. Perform 1 million simulations to approximate Pi using random points.
    2. Split the job into subjobs, with each subjob performing 1000 simulations.
    3. Each subjob should run independently and the results should be aggregated to estimate Pi.

    The code should be in Python and use Ganga to manage and submit the subjobs. Here's a breakdown of the approach:

    1. Use Ganga's Job API to define the jobs that will run the simulation.
    2. Each subjob will perform 1000 random simulations to calculate Pi using the accept-reject method.
    3. Aggregate the results from all subjobs to get an approximation of Pi.
    don't output anything other than code
    """

    # Send the request with the prompt to Gemini
    chat_history.append({"role": "user", "parts": [{"text": prompt}]})


    # Generate response with memory
    response = model.generate_content(contents=chat_history)

    # Extract the code from the response
    code = response.text.strip() if response.text else ""

    # Check if the code is non-empty
    if code:
        # Define the file path

        # Attempt to create and write to the file if it doesn't exist

        print(code)

    return code

if __name__ == "__main__":
    generate_pi_code()
