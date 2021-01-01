

NUM_OF_CITIZENS = 10000
NUM_OF_UPVOTES = 1000


types = {
    "311-service-requests-abandoned-vehicles": "Abandoned Vehicle Complaint",
    "311-service-requests-alley-lights-out": "Alley Light Out",
    "311-service-requests-garbage-carts": "Garbage Cart Black Maintenance/Replacement",
    "311-service-requests-graffiti-removal": "Graffiti Removal",
    "311-service-requests-pot-holes-reported": "Pothole in Street",
    "311-service-requests-rodent-baiting": "Rodent Baiting/Rat Complaint",
    "311-service-requests-sanitation-code-complaints": "Sanitation Code Violation",
    "311-service-requests-street-lights-all-out": "Street Lights - All/Out",
    "311-service-requests-street-lights-one-out": "Street Light Out",
    "311-service-requests-tree-debris": "Tree Debris",
    "311-service-requests-tree-trims": "Tree Trim"
}

int_type = list([
    "ssa", "zip_code", "ward", "police_district", "community_area", "historical_wards", "zip_codes", "community_areas",
    "census_tracts", "wards", "number_of_black_carts_delivered", "number_of_potholes_filled_on_black",
    "number_of_premises_baited", "number_of_premises_with_garbage", "number_of_premises_with_rats","days_as_parked"    
    ])

float_type = list([
    "x_coordinate", "y_coordinate"
    ])

checked_type = int_type+float_type+list(["creation_date","completion_date","type_of_service_request","latitude","longitude"])