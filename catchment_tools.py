from langchain.agents import tool
from geo_loader import GeoDataLoader
import numpy as np

# Load the data
loader = GeoDataLoader()
gdf = loader.get_data()

@tool
def audit_fairness() -> str:
    """
    Analyze catchment zones for fairness based on area size. 
    Flags zones that are significantly too small or large.
    """
    areas = gdf["shape_Area"]
    q1, q3 = areas.quantile(0.25), areas.quantile(0.75)
    iqr = q3 - q1
    low = gdf[areas < (q1 - 1.5 * iqr)]["catchment"].tolist()
    high = gdf[areas > (q3 + 1.5 * iqr)]["catchment"].tolist()
    return f"Too Small Zones: {low or 'None'}\nToo Large Zones: {high or 'None'}"

@tool
def find_overlaps() -> str:
    """
    Detect overlapping catchment zones.
    Returns a summary of the overlaps between zones.
    """
    overlaps = loader.detect_overlaps()
    return "\n".join(f"{a} ↔ {b} — {round(area)} m²" for a, b, area in overlaps[:5]) or "No overlaps"

@tool
def transport_load() -> str:
    """
    Categorize zones based on their estimated travel burden.
    The classification is based on the radius derived from zone area.
    """
    g = gdf.copy()
    g["estimated_radius_km"] = np.sqrt(g["shape_Area"] / np.pi) / 1000
    g["load"] = g["estimated_radius_km"].apply(lambda r: "High" if r > 3 else "Medium" if r > 1.5 else "Low")
    return g["load"].value_counts().to_string()

@tool
def scenario_suggest() -> str:
    """
    Simulate possible planning scenarios such as shrinking, merging, or splitting zones.
    Provides actionable recommendations for catchment area restructuring.
    """
    big, small = loader.get_extreme_zones()
    return (
        f"Shrink: {big['catchment']}\n"
        f"Merge: {small['catchment']} + nearby\n"
        f"Split: {big['catchment']} → two medium zones"
    )
