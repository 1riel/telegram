import os
import time


os.system("flutter build web --release --base-href /telegram/")

time.sleep(1)

os.system("git add .")
os.system(f'git commit -m "update"')
os.system("git push")
