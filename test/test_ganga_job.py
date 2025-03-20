from ganga.GangaCore.testlib.GangaUnitTest import GangaUnitTest

class TestPDFProcessing(GangaUnitTest):
    def testPDFProcessing(self):
        from GangaCore.GPI import Job, Executable, File, ArgSplitter
        from ganga.GangaTest.Framework.utils import sleep_until_completed, file_contains
        import os

        # Create counter.sh
        counter_script = """#!/bin/bash
set -e  # Exit on error
echo "Processing PDF file: $1"
pdftotext "$1" - | sed -e 's/ /\n/g' | grep -ci 'it' || true
"""
        script_path = os.path.join(os.path.dirname(__file__), "counter.sh")
        with open(script_path, "w") as f:
            f.write(counter_script)
        os.chmod(script_path, 0o755)

        # Create test PDFs (reduced number for faster testing)
        test_dir = os.path.join(os.path.dirname(__file__), "split_pages")
        os.makedirs(test_dir, exist_ok=True)
        num_pages = 29
        for i in range(1, num_pages + 1):
            pdf_path = os.path.join(test_dir, f"page_{i}.pdf")
            with open(pdf_path, "w") as f:
                f.write(f"Test PDF {i} with it word")
            print(f"Created test PDF: {pdf_path}")

        j = Job()
        j.application = Executable()
        j.application.exe = File(script_path)

        args = [[os.path.abspath(os.path.join(test_dir, f"page_{i}.pdf"))] 
                for i in range(1, num_pages + 1)]
        j.splitter = ArgSplitter(args=args)

        print("Checking initial job state...")
        self.assertTrue(not j.subjobs)
        self.assertEqual(len(j.subjobs), 0)

        print("Submitting job...")
        j.submit()

        print(f"Verifying {num_pages} subjobs were created...")
        self.assertEqual(len(j.subjobs), num_pages)

        print("Checking subjob properties...")
        for s in j.subjobs:
            self.assertEqual(s.master, j)
            self.assertIn(s.status, ['submitted', 'running', 'completed'])

        print("Waiting for job completion (120s timeout)...")
        self.assertTrue(sleep_until_completed(j, 120), 'Timeout on completing job')

        print("Verifying job completion...")
        for i, s in enumerate(j.subjobs, 1):
            self.assertEqual(s.status, 'completed')
            print(f"Checking output of subjob {i}...")
            self.assertTrue(file_contains(
                s.outputdir + '/stdout', 
                'Processing PDF file:'
            ))

        print("Cleaning up...")
        if os.path.exists(script_path):
            os.remove(script_path)
        if os.path.exists(test_dir):
            import shutil
            shutil.rmtree(test_dir)
        print("Test completed successfully!")