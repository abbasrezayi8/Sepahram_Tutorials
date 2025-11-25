import pandas as pd
import requests as req
import time

# Get Data For 100 Times
list = []
dict = {}
print("Fetching Data...")
for i in range (100) :
    result = req.get("https://randomuser.me/api/").json()
    data =  result["results"][0]
    dict = {
    "Gender" : data.get("gender") ,
    "First_Name" : data.get("name").get("first") ,
    "Last_name" : data.get("name").get("last"),
    "Age" : data.get("dob").get("age") ,
    "Country" : data.get("location").get("country") ,
    "State" : data.get("location").get("state") ,
    "City" : data.get("location").get("city"),
    "PostCode" : data.get("location").get("postcode") ,
    "Email" : data.get("email")  ,
    "Phone" : data.get("phone")  ,
    "Cell" : data.get("cell")  
    }
    list.append(dict)
    print(f"Data Fetched For {i} Time")
    time.sleep(3)
# Make DataFrame
df = pd.DataFrame(list)
df["PostCode"] = df["PostCode"].astype(str)
print(f"Data Frame Created With {len(df)} Records")
# Save DataFrame to Parquet
df.to_parquet("/tmp/report.parquet", engine="pyarrow")
print(f"Data Frame Saved To /tmp/report.parquet")
