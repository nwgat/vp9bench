# The Fire Escape 4K Benchmark Beta 1
# https://nwgat.ninja/TheFireEscape

import time 
import os
import sys
sys.stdout=open("output.vp9.txt","a")
cmd = 'vpxenc.exe -w 3840 -h 2160 --row-mt=1 --tile-columns=6 --auto-alt-ref=1 --lag-in-frames=25 --aq-mode=0 --target-bitrate=20000 --cpu-used=1 --threads=16 -o test.webm TheFireEscape.raw.y4m'
start_time = time.time()
os.system(cmd)
print("%s" % (time.time() - start_time))
sys.stdout.close()
