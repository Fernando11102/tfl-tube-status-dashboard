import pandas as pd

def find_disruptions(df):
    return df[df["status"] != "Good Service"]

def test_disruptions_excludes_good_service():
    data = pd.DataFrame(
        {
            "line": ["Central", "Victoria", "Bakerloo"],
            "status":  ["Severe Delays", "Good Service", "Minor Delays"],
        }
    )

    result = find_disruptions(data)
    assert len(result) == 2
    assert "Victoria" not in result["line"].values

def test_csv_has_expected_columns():
        df = pd.read_csv("tube_status.csv")
        assert list(df.columns) == ["line", "status", "timestamp"]

def test_csv_has_no_missing_statuses():
        df = pd.read_csv("tube_status.csv")
        assert df["status"].notna().all()