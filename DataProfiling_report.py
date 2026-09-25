import pandas as pd
import numpy as np
df=pd.DataFrame(
    {
        "Name":["ammar",199,"136","999","523"],
        "Age":[16,18,19,17,78]
    }
)
def profile_df(args):
    report = {}
    for col in df.columns:
      series = df[col]
      info = {}
    #missing
      info["missing_pct"] = series.isna().mean() * 100
      # type guess
      if series.dtype == "object":
         numeric_try = pd.to_numeric(series, errors = "coerce")
         numeric_success = numeric_try.notna().mean() * 100

         if numeric_success >= 80:
                info["type_guess"] = "numeric-like string"
         else:
                info["type_guess"] = "text"
      elif "datetime" in str(series.dtype):
           info["type_guess"] = "datetime"
      else:
          info["type_guess"] = str(series.dtype)
      report[col] = info
    return pd.DataFrame(report).T
result= profile_df(df)
print(result)