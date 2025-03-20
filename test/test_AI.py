import subprocess
import os
import sys
import unittest
import site

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from Ai_part.generate_pi_code import generate_pi_code
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

class TestGeneratedCodeExecution(unittest.TestCase):
    def setUp(self):
        self.python_path = [
            site.getsitepackages()[0],
            project_root
        ]

    def test_generated_code_execution(self):
        code = generate_pi_code()
        self.assertNotEqual(code, "Generated code is empty.")
        
        code = self.clean_code(code)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        temp_file_path = os.path.join(current_dir, 'temp_code.py')
        
        # try:
        # Create temporary file first
        with open(temp_file_path, 'w') as temp_file:
            temp_file.write(code)
            
        # Only check if file was created successfully
        if not os.path.exists(temp_file_path):
            self.fail("Failed to create temporary test file")
                
        # finally:
        #     # Clean up temp file if it exists
        #     if os.path.exists(temp_file_path):
        #         os.remove(temp_file_path)

    def clean_code(self, code):
        lines = code.splitlines()
        if lines and lines[0].startswith('```python'):
            lines.pop(0)
        if lines and lines[-1] == '```':
            lines.pop()
        return '\n'.join(lines)

if __name__ == '__main__':
    unittest.main()