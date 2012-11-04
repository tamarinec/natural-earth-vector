# ---------------------------------------------------------------------------
# build_b6_ne_50m_admin_1_all.py
# Created on: Sun Nov 04 2012 03:09:16 AM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Set the necessary product code
gp.SetProduct("ArcInfo")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Analysis Tools.tbx")


# Local variables...
ne_50m_admin_1_states_provinces_lakes_shp_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_cultural\\ne_50m_admin_1_states_provinces_lakes_shp.shp"
ne_50m_lakes_tmp_admin_1_erase_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_physical\\ne_50m_lakes_tmp_admin_1_erase.shp"
ne_50m_lakes_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_physical\\ne_50m_lakes.shp"
ne_10m_admin_1_states_provinces_geodb_tmp__2_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_cultural\\ne_50m_admin_1_states_provinces_shp.shp"
ne_50m_admin_1_states_provinces_shp_scale_rank_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_cultural\\ne_50m_admin_1_states_provinces_shp_scale_rank.shp"
ne_10m_admin_1_label_points_details = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\10m_cultural\\ne_10m_admin_1_label_points.gdb\\ne_10m_admin_1_label_points_details"
ne_50m_admin_1_states_provinces_shp_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_cultural\\ne_50m_admin_1_states_provinces_shp.shp"

# Process: Select (2)...
gp.Select_analysis(ne_50m_admin_1_states_provinces_shp_scale_rank_shp, ne_50m_admin_1_states_provinces_shp_shp, "\"scalerank\" >= 0")

# Process: Join Field...
gp.JoinField_management(ne_50m_admin_1_states_provinces_shp_shp, "adm1_code", ne_10m_admin_1_label_points_details, "adm1_code", "")

# Process: Select (3)...
gp.Select_analysis(ne_50m_lakes_shp, ne_50m_lakes_tmp_admin_1_erase_shp, "\"admin\" = 'admin-0' Or \"admin\" = 'admin-0 more'")

# Process: Erase...
gp.Erase_analysis(ne_10m_admin_1_states_provinces_geodb_tmp__2_, ne_50m_lakes_tmp_admin_1_erase_shp, ne_50m_admin_1_states_provinces_lakes_shp_shp, "")

