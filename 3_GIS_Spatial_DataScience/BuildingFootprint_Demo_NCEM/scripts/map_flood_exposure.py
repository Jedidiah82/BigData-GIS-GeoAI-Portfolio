import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ---------------------------
# PATHS
# ---------------------------
FLOOD_PATH = "hazards/flood_fema_nfhl.gpkg"
BUILDINGS_CLEAN = "data_clean/buildings_cleaned.gpkg"
BUILDINGS_FLOODED = "hazards/buildings_in_floodzones.gpkg"
OUTPUT_MAP = "figures/flood_exposure_map.png"

def main():
    print("[*] Loading datasets...")

    flood = gpd.read_file(FLOOD_PATH)
    buildings = gpd.read_file(BUILDINGS_CLEAN)
    flooded = gpd.read_file(BUILDINGS_FLOODED)

    # ---------------------------
    # Ensure same CRS
    # ---------------------------
    flood = flood.to_crs(epsg=3857)
    buildings = buildings.to_crs(epsg=3857)
    flooded = flooded.to_crs(epsg=3857)

    print("[*] Creating NCEM-style map...")

    fig, ax = plt.subplots(figsize=(14, 14))
    ax.set_aspect('equal')

    # ---------------------------
    # 1️⃣ Plot main building footprints (light grey)
    # ---------------------------
    buildings.plot(
        ax=ax,
        color="lightgrey",
        linewidth=0,
        markersize=0.05,
        alpha=0.3,
        label="All Buildings"
    )

    # ---------------------------
    # 2️⃣ Plot FEMA flood hazard zones (semi-transparent blue)
    # ---------------------------
    flood.plot(
        ax=ax,
        color="#4DA6FF",
        edgecolor="#1A75FF",
        linewidth=0.4,
        alpha=0.45,
        label="Flood Hazard Zone"
    )

    # ---------------------------
    # 3️⃣ Plot flooded buildings (red)
    # ---------------------------
    if not flooded.empty:
        flooded.plot(
            ax=ax,
            color="red",
            markersize=0.8,
            label="Buildings in Flood Zones"
        )
    else:
        print("[INFO] No flooded buildings to plot.")

    # ---------------------------
    # 4️⃣ Auto-zoom to the flood extent (critical fix)
    # ---------------------------
    xmin, ymin, xmax, ymax = flood.total_bounds
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # ---------------------------
    # 5️⃣ Title & Legend
    # ---------------------------
    plt.title("Flood Exposure: Buildings in FEMA Flood Zones\nNC Emergency Management Style", fontsize=16, fontweight="bold")

    legend_elements = [
        Line2D([0], [0], color='lightgrey', marker='s', markersize=8, label='All Buildings'),
        Line2D([0], [0], color='#1A75FF', linewidth=6, label='Flood Hazard Zone'),
        Line2D([0], [0], color='red', marker='s', markersize=8, label='Flooded Buildings')
    ]

    ax.legend(handles=legend_elements, loc='upper right', frameon=True)

    # ---------------------------
    # 6️⃣ Remove axes for clean cartographic output
    # ---------------------------
    ax.axis('off')

    # ---------------------------
    # 7️⃣ Save Figure
    # ---------------------------
    plt.savefig(OUTPUT_MAP, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"[SUCCESS] Clean NCEM-style map saved to: {OUTPUT_MAP}")

if __name__ == "__main__":
    main()
