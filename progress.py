def getProgressBar(curPercentage): 
  curPercentage = int(curPercentage)
  curString = "-"
  if curPercentage >= 10: 
    curString = "-"
    
  if curPercentage >= 20: 
    curString = "--"
    
  if curPercentage >= 30: 
    curString = "---"
    
  if curPercentage >= 40: 
    curString = "----"
    
  if curPercentage >= 50: 
    curString = "-----"
    
  if curPercentage >= 60: 
    curString = "------"
    
  if curPercentage >= 70: 
    curString = "-------"
    
  if curPercentage >= 80: 
    curString = "--------"
    
  if curPercentage >= 90: 
    curString = "---------"
    
  if curPercentage >= 99: 
    curString = "----------"

  return curString