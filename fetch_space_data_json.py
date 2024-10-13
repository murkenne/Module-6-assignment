import requests

# Function to fetch data about planets from the API
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    
    if response.status_code == 200:
        planets_data = response.json()['bodies']
        
        # Filter out planets only and return their data
        planets = [planet for planet in planets_data if planet['isPlanet']]
        return planets
    else:
        print("Error: Could not fetch planet data")
        return []

# Function to find the heaviest planet
def find_heaviest_planet(planets):
    heaviest_planet = None
    max_mass = 0

    for planet in planets:
        if 'mass' in planet and 'massValue' in planet['mass']:
            mass = planet['mass']['massValue']
            if mass > max_mass:
                max_mass = mass
                heaviest_planet = planet

    if heaviest_planet:
        return heaviest_planet['englishName'], max_mass
    else:
        return "Unknown", 0

# Fetch the planets
planets = fetch_planet_data()

# Print all planet names
print("Planets:")
for planet in planets:
    print(f"- {planet.get('englishName', 'Unknown')}")

# Find the heaviest planet and display the result
name, mass = find_heaviest_planet(planets)
print(f"\nThe heaviest planet is {name} with a mass of {mass:.2f} x 10^24 kg.")
