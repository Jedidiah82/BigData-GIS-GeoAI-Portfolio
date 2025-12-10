import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from shapely.geometry import Point
import contextily as ctx

# ----------------------------------------------------
# FILE PATHS
# ----------------------------------------------------
BUILDINGS_PATH = "hazards/buildings_in_floodzones.gpkg"
FLOOD_PATH = "hazards/flood_fema_nfhl.gpkg"
OUTPUT = "figures/flood_exposure_map_ncem.png"

# ----------------------------------------------------
# NORTH ARROW
# ----------------------------------------------------
def add_north_arrow(ax, size=0.08):
    x, y, arrow_length = 0.95, 0.15, 0.08
    ax.annotate(
        'N',
        xy=(x, y + arrow_length),
        xytext=(x, y),
        arrowprops=dict(facecolor='black', width=4, headwidth=12),
        ha='center',
        va='center',
        xycoords=ax.transAxes
    )

# ----------------------------------------------------
# SCALEBAR
# ----------------------------------------------------
def add_scalebar(ax, length_km=1):
    import numpy as np
    x0, x1 = ax.get_xlim()
    scale_length = length_km * 1000
    ratio = scale_length / (x1 - x0)

    ax.plot([0.1, 0.1 + ratio], [0.1, 0.1], transform=ax.transAxes,
            color='black', linewidth=3)
    ax.text(0.1 + ratio / 2, 0.11, f"{length_km} km",
            transform=ax.transAxes, ha='center')

# ----------------------------------------------------
# MAIN
# ----------------------------------------------------
def main():
    print("[*] Loading buildings and flood data...")
    buildings = gpd.read_file(BUILDINGS_PATH)
    flood = gpd.read_file(FLOOD_PATH)

    print("[*] Reprojecting to Web Mercator...")
    buildings = buildings.to_crs(epsg=3857)
    flood = flood.to_crs(epsg=3857)

    # ----------------------------------------------------
    # FIGURE SETUP
    # ----------------------------------------------------
    print("[*] Creating NCEM-style map...")
    fig, ax = plt.subplots(figsize=(12, 12))

    # Flood Zones
    flood.plot(ax=ax, color="#3182bd", alpha=0.40, linewidth=0)

    # Buildings not impacted
    buildings[buildings["flooded"] == 0].plot(
        ax=ax, color="#cccccc", markersize=1, label="Buildings (Not Flooded)"
    )

    # Buildings impacted
    buildings[buildings["flooded"] == 1].plot(
        ax=ax, color="#e41a1c", markersize=3, label="Flooded Buildings"
    )

    # Basemap
    ctx.add_basemap(ax, crs=buildings.crs.to_string(), source=ctx.providers.Stamen.TonerLite)

    # NCEM cartographic elements
    add_north_arrow(ax)
    add_scalebar(ax)

    # ----------------------------------------------------
    # LEGEND
    # ----------------------------------------------------
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Flooded Buildings',
               markerfacecolor='#e41a1c', markersize=10),
        Line2D([0], [0], marker='o', color='w', label='Non-Flooded Buildings',
               markerfacecolor='#cccccc', markersize=10),
        Line2D([0], [0], color='#3182bd', lw=10, label='FEMA Flood Zone')
    ]

    ax.legend(handles=legend_elements, loc='upper right')

    ax.set_title("Flood Exposure Map — NC Emergency Management (Demo)", fontsize=16)
    ax.axis("off")

    print(f"[SUCCESS] Map saved to {OUTPUT}")
    plt.tight_layout()
    plt.savefig(OUTPUT, dpi=300)
    plt.close()


if __name__ == "__main__":
    main()
