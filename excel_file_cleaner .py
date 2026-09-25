import string

import numpy as np
import pandas as pd
a=pd.read_excel("messy_data.xlsx")
pd.set_option("display.max_rows",None)
pd.set_option("display.max_colwidth",None)
a["Name"]=a["Name"].fillna("Not provided")
a["Name"]=a["Name"].apply(lambda x:x.strip() if isinstance(x,str)else None)
a["Age"]=a["Age"].apply(lambda x:x if isinstance(x,int) else np.nan )
a["Age"]=a["Age"].fillna(a["Age"].median())
a["Score"]=a["Score"].fillna(a["Score"].mean())
a["City"]=a["City"].bfill()
a["Time"]=a["Time"].ffill(limit=1).bfill(limit=1)
print(a)
a.to_excel("C:\\Users\\DELL\\Downloads\\cleaned_data.xlsx",index=False)