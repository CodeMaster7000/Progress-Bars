from tqdm import tqdm
import time
  
  
for i in tqdm (range (101), 
               desc="Uploading…", 
               ascii=False, ncols=75):
    time.sleep(0.01)
      
print("Successfully uploaded!")
