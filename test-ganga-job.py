import os
from GangaCore.GPI import Executable, Job, File, ArgSplitter, CustomMerger

job = Job()
job.application = Executable()
job.application.exe = File("counter.sh")
# local paths
#replace with your path
args = [[f"/gangagsoc/split_pages/page_{i}.pdf"] for i in range(1, 30)]
splitter = ArgSplitter(args=args)
filelist = []
for i in range(len(args)):
	filename = args[i][0]
	filelist.append(filename)
job.application.args = filelist
job.splitter = splitter
job.inputfiles = filelist
job.backend = "Local"
job.postprocessors = CustomMerger(module="./merger.py")
job.submit()