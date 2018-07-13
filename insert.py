import os
os.system("ps -eaf | grep python |awk '{print $2}' > processes.txt")
