import geopandas as gpd
import pandas as pd

CLEAN = "data_clean/buildings_cleaned.gpkg"

HAZARDS = {
    "flood": "hazards/flood_fema_nfhl.gpkg",
    "storm_surge": "hazards/storm_surge_noaa.tif",   # raster support optional
    "wildfire": "hazards/wildfire_risk_ncfs.tif",     # raster support optional
    "tornado": "hazards/tornado_tracks_noaa.gpkg"
}

def load_vector(path):
    return gpd.read_file(path)

def analyze(buildings, hazard_path, name):
    print(f"[*] Analyzing {name} exposure...")

    hazard = load_vector(hazard_path)
    hazard = hazard.to_crs(buildings.crs)

    exposed = gpd.sjoin(buildings, hazard, predicate="intersects", how="inner")

    pct = round((len(exposed) / len(buildings)) * 100, 4)
    print(f" → {name}: {len(exposed)} exposed buildings ({pct}%)")

    exposed.to_file(f"hazards/{name}_exposed.gpkg", driver="GPKG")

    return len(exposed), pct

def main():
    buildings = gpd.read_file(CLEAN)

    summary_rows = []
    for name, path in HAZARDS.items():
        try:
            count, percent = analyze(buildings, path, name)
            summary_rows.append([name, count, percent])
        except Exception as e:
            print(f"[WARN] Could not process {name}: {e}")

    df = pd.DataFrame(summary_rows, columns=["Hazard", "Exposed Buildings", "Percent"])
    df.to_csv("hazards/multi_hazard_summary.csv", index=False)
    print("\n[SUCCESS] Multi-hazard summary saved.")

if __name__ == "__main__":
    main()
