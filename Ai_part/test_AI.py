import subprocess
import os
import sys
import tempfile
import unittest

# Function to install Ganga if it's not already installed
def install_ganga():
    try:
        import ganga
    except ImportError:
        print("Ganga not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "ganga"])
        print("Ganga installed successfully.")
    else:
        print("Ganga is already installed.")

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from generate_pi_code import generate_pi_code


class TestGeneratedCodeExecution(unittest.TestCase):

    def test_generated_code_execution(self):
        install_ganga()
        #gemini response here
        code = generate_pi_code()

        self.assertNotEqual(code, "Generated code is empty.")

        # Clean the code by removing Markdown code block delimiters
        code = self.clean_code(code)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as temp_file:
            temp_file.write(code.encode())
            temp_file_path = temp_file.name

        try:
            env = os.environ.copy()
            env['PYTHONPATH'] = '/path/to/ganga/module'  # Adjust this path as needed

            result = subprocess.run([sys.executable, temp_file_path], capture_output=True, text=True, env=env)

            self.assertEqual(result.returncode, 0, f"Error executing generated code: {result.stderr}")

            print(result.stdout)

        finally:
            if os.path.isfile(temp_file_path):
                os.remove(temp_file_path)

    def clean_code(self, code):
        """
        Removes Markdown code block delimiters and any leading/trailing whitespace
        from the generated code.
        """
        lines = code.splitlines()
        if lines[0].startswith('```python'):
            lines.pop(0) 
        if lines and lines[-1] == '```':
            lines.pop() 
        return '\n'.join(lines)

if __name__ == '__main__':
    unittest.main()
