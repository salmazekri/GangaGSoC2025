import os
from GangaCore.GPI import Executable, Job, File, ArgSplitter, CustomMerger,LocalFile

job = Job()
job.application = Executable()
job.application.exe = File("counter.sh")
# local paths
#replace with your path
args = [["LHC_page_1.pdf"],["LHC_page_2.pdf"],["LHC_page_3.pdf"],["LHC_page_4.pdf"],["LHC_page_5.pdf"],["LHC_page_6.pdf"],["LHC_page_7.pdf"],["LHC_page_8.pdf"],["LHC_page_9.pdf"],["LHC_page_10.pdf"],["LHC_page_11.pdf"],["LHC_page_12.pdf"],["LHC_page_13.pdf"],["LHC_page_14.pdf"],["LHC_page_15.pdf"],["LHC_page_16.pdf"],["LHC_page_17.pdf"],["LHC_page_18.pdf"],["LHC_page_19.pdf"],["LHC_page_20.pdf"],["LHC_page_21.pdf"],["LHC_page_22.pdf"],["LHC_page_23.pdf"],["LHC_page_24.pdf"],["LHC_page_25.pdf"],["LHC_page_26.pdf"],["LHC_page_27.pdf"],["LHC_page_28.pdf"],["LHC_page_29.pdf"]]
splitter = ArgSplitter(args=args)
filelist = []
for i in range(len(args)):
	filename = args[i][0]
	filelist.append(filename)
job.application.args = filelist
job.splitter = splitter
job.inputfiles = filelist
job.backend = "Local"
job.outputfiles = [LocalFile('ans.txt')]
# job.postprocessors = CustomMerger(module="./merger.py")
job.postprocessors = CustomMerger(
    files=['ans.txt'],
    module=File('mymerger.py'),
    ignorefailed=True  # Added to handle failed subjobs
)
job.submit()