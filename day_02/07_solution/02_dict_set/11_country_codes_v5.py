# Add more country codes
country_codes = {
	"PH": "Philippines",
	"US": "United States",
    "AU": "Australia",
    "CA": "Canada",
}

# Print the country for the given country code
country_code = input("Enter country code: ")
print(country_codes.get(country_code, "Unknown"))

print("Keys:\t", country_codes.keys())
print("Values:\t", country_codes.keys())
