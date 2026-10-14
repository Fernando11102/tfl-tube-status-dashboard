import requests
import json

URL = "https://api.tfl.gov.uk/Line/Mode/tube/status"

response = requests.get(URL, timeout=10)
response.raise_for_status()

data = response.json()

print(json.dumps(data[0], indent=4))

for line in data:
    name = line.get("name", "Unkown")

    statuses = line.get("lineStatuses", [])

    if statuses:
        status = statuses[0].get(
            "statusSeverityDescription",
            "Unknown status"
        )

    else:
        status = "No status available"


   
    print(name, "-", status)
