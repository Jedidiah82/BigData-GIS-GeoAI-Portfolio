import geopandas as gpd
import matplotlib.pyplot as plt

CLEAN = "data_clean/buildings_cleaned.gpkg"
FLOODED = "hazards/buildings_in_floodzones.gpkg"
FLOOD = "hazards/flood_fema_nfhl.gpkg"

def main():
    print("[*] Loading layers...")
    buildings = gpd.read_file(CLEAN)
    flooded = gpd.read_file(FLOODED)
    floodzones = gpd.read_file(FLOOD)

    print("[*] Creating map...")
    fig, ax = plt.subplots(figsize=(12, 12))

    buildings.sample(8000).plot(
        ax=ax, color="lightgrey", markersize=0.5, alpha=0.4, label="Buildings"
    )
    floodzones.boundary.plot(
        ax=ax, color="blue", linewidth=0.6, label="Flood Hazard Boundary"
    )
    flooded.plot(
        ax=ax, color="red", markersize=1, label="Flooded Buildings"
    )

    plt.title("Flood Exposure: Building Footprints in FEMA Flood Zones", fontsize=16)
    plt.legend()
    plt.tight_layout()

    plt.savefig("figures/flood_exposure_map.png", dpi=300)
    print("[SUCCESS] Map saved to figures/flood_exposure_map.png")

if __name__ == "__main__":
    main()
