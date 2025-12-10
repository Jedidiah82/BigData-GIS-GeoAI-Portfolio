import geopandas as gpd

RAW_PATH = "data_raw/microsoft_footprints.geojson"
OUTPUT_PATH = "data_clean/buildings_cleaned.gpkg"
QAQC_PATH = "data_clean/buildings_qaqc_report.md"

def main():

    print("[*] Loading raw building footprints...")
    buildings = gpd.read_file(RAW_PATH)

    print("[*] Reprojecting to EPSG:3857 for correct area calculation...")
    buildings = buildings.to_crs(3857)

    print("[*] Calculating polygon areas...")
    buildings["area_m2"] = buildings.geometry.area

    print("[*] Removing tiny polygons (< 30 m²)...")
    before = len(buildings)
    buildings = buildings[buildings["area_m2"] > 30]
    removed = before - len(buildings)
    print(f"[INFO] Removed {removed} tiny polygons.")

    print("[*] Fixing invalid geometries...")
    buildings["geometry"] = buildings.buffer(0)

    print("[*] Adding perimeter field...")
    buildings["perimeter_m"] = buildings.geometry.length

    print("[*] Saving cleaned dataset to:", OUTPUT_PATH)
    buildings.to_file(OUTPUT_PATH, driver="GPKG")

    print("[*] Writing QA/QC report...")
    with open(QAQC_PATH, "w") as f:
        f.write(f"# QA/QC Report\n")
        f.write(f"Total buildings after cleaning: {len(buildings)}\n")
        f.write(f"Removed small polygons: {removed}\n")

    print("[SUCCESS] Cleaning complete.")

if __name__ == "__main__":
    main()
