import geopandas as gpd

class GeoDataLoader:
    def __init__(self, path="cleaned_catchments.geojson"):
        self.gdf = gpd.read_file(path)

    def get_data(self):
        return self.gdf

    def get_summary(self):
        return {
            "total_zones": len(self.gdf),
            "unique_schools": self.gdf["catchment"].nunique(),
            "area_min": self.gdf["shape_Area"].min(),
            "area_max": self.gdf["shape_Area"].max()
        }

    def detect_overlaps(self):
        overlaps = []
        for i, zone1 in self.gdf.iterrows():
            for j, zone2 in self.gdf.iterrows():
                if i < j and zone1["geometry"].intersects(zone2["geometry"]):
                    area = zone1["geometry"].intersection(zone2["geometry"]).area
                    if area > 0:
                        overlaps.append((zone1["catchment"], zone2["catchment"], area))
        return overlaps

    def get_extreme_zones(self):
        largest = self.gdf.nlargest(1, "shape_Area").iloc[0]
        smallest = self.gdf.nsmallest(1, "shape_Area").iloc[0]
        return largest, smallest
