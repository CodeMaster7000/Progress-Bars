from tqdm import tqdm
import time
  
  
for i in tqdm (range (101), 
               desc="Uploadingâ€¦", 
               ascii=False, ncols=75):
    time.sleep(0.01)
      
print("Successfully uploaded!")
