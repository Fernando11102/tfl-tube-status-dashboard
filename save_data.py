import requests
import pandas as pd
from datetime import datetime

URL = "https://api.tfl.gov.uk/Line/Mode/tube/Status"

response = requests.get(URL, timeout=10)
response.raise_for_status()

data =  response.json()

records = []

for line in data:
    name = line.get("name", "Unknown")
    statuses = line.get("lineStatuses", [])

    for status in statuses:
        records.append({
            "line" : name,
            "status": status.get(
                "statusSeverityDescription",
                "Unknown"

            ), 
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            )
            
        })

        df = pd.DataFrame(records)

        df.to_csv("tube_status.csv", index=False)

        print(df)
        print("Data saved successfully")