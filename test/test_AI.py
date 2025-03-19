import subprocess
import os
import sys
import tempfile
import unittest

# Add the directory containing generate_pi_code.py to the system path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.Ai_part.generate_pi_code import generate_pi_code

class TestGeneratedCodeExecution(unittest.TestCase):

    def test_generated_code_execution(self):
        code = generate_pi_code()

        self.assertNotEqual(code, "Generated code is empty.")

        # Create a temporary file to save the generated code
        with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as temp_file:
            temp_file.write(code.encode())
            temp_file_path = temp_file.name

        try:
            # Run the generated code using subprocess
            result = subprocess.run([sys.executable, temp_file_path], capture_output=True, text=True)

            # Check if the execution was successful
            self.assertEqual(result.returncode, 0, f"Error executing generated code: {result.stderr}")

            # Optionally, process the result.stdout as needed
            print(result.stdout)

        finally:
            # Clean up the temporary file
            if os.path.isfile(temp_file_path):
                os.remove(temp_file_path)

if __name__ == '__main__':
    unittest.main()
