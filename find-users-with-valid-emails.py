import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Use the str.match() method with a regex pattern to find valid emails
    return users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$')]
    
    
