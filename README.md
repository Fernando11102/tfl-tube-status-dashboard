# London Underground Service Status Dashboard

A Python project that collects live Tube line status data from the Transport for London (TfL) API, analyses it with pandas, and shows the results in an interactive Streamlit dashboard.

## What it does

- Fetches the current status of every London Underground line from the TfL API
- Saves the data to a CSV file with a timestamp
- Cleans the data and finds lines with delays or disruptions
- Displays key numbers, a status chart and a disruptions table in a dashboard

## Tech used

- Python
- pandas
- requests
- Streamlit

## Project files

- `fetch_data.py`: gets live line status from the TfL API
- `save_data.py`: saves the data to `tube_status.csv`
- `analyse_data.py`: summarises the data in the terminal
- `dashboard.py`: the Streamlit dashboard

## How to run it

1. Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

2. Install the packages:

```
pip install pandas requests streamlit
```

3. Collect the data:

```
python save_data.py
```

4. Start the dashboard:

```
streamlit run dashboard.py
```

## Example finding

On the day I collected data (13 October 2026), 8 of 11 lines had good service, and 3 had disruptions: Central and Jubilee (severe delays) and Bakerloo (minor delays).