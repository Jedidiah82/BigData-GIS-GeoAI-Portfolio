import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from matplotlib_scalebar.scalebar import ScaleBar
from shapely.geometry import Point

BUILDINGS_ALL = "data_clean/buildings_cleaned.gpkg"
BUILDINGS_FLOOD = "hazards/buildings_in_floodzones.gpkg"
OUTPUT = "figures/flood_exposure_map_ncem.png"


def add_north_arrow(ax, size=0.12):
    x, y, width, height = 0.95, 0.15, size, size
    ax.annotate(
        'N', xy=(x + width/2, y + height), xytext=(x + width/2, y + height),
        ha='center', va='bottom', fontsize=14, xycoords=ax.transAxes
    )
    ax.arrow(
        x + width/2, y + height*0.1, 0, height*0.7, 
        transform=ax.transAxes, linewidth=2, head_width=0.02, color='black'
    )


def main():
    print("[*] Loading buildings...")
    buildings_all = gpd.read_file(BUILDINGS_ALL)
    flooded = gpd.read_file(BUILDINGS_FLOOD)

    print("[*] Tagging flooded buildings...")
    flooded["flooded"] = 1

    # Combine flooded + nonflooded
    flooded_ids = set(flooded.index)
    buildings_all["flooded"] = buildings_all.index.isin(flooded_ids).astype(int)

    print("[*] Reprojecting...")
    buildings_all = buildings_all.to_crs(3857)
    flooded = flooded.to_crs(3857)

    print("[*] Generating NCEM-style map...")
    fig, ax = plt.subplots(figsize=(12, 12))

    # Background basemap
    ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)

    # Plot non-flooded
    buildings_all[buildings_all["flooded"] == 0].plot(
        ax=ax, color="#C8C8C8", markersize=1, linewidth=0
    )

    # Plot flooded
    flooded.plot(
        ax=ax, color="#E31A1C", markersize=2, linewidth=0, label="Flooded Buildings"
    )

    # Add title
    plt.title("NCEM Flood Exposure — Building Footprints", fontsize=16, weight="bold")

    # Add legend
    plt.legend(loc="lower left")

    # Add north arrow
    add_north_arrow(ax)

    # Add scale bar
    scalebar = ScaleBar(dx=1, units="m", location="lower right")
    ax.add_artist(scalebar)

    ax.set_axis_off()

    print("[*] Saving map...")
    plt.savefig(OUTPUT, dpi=300, bbox_inches="tight")
    print("[SUCCESS] Saved:", OUTPUT)


if __name__ == "__main__":
    main()
