import requests

# Function to fetch data for a Pokémon
def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Return the data as a Python dictionary
    else:
        print(f"Error: Could not fetch data for {pokemon_name}")
        return None

# Function to calculate the average weight
def calculate_average_weight(pokemon_list):
    total_weight = 0
    count = 0

    for pokemon_name in pokemon_list:
        data = fetch_pokemon_data(pokemon_name)
        if data:
            total_weight += data['weight']
            count += 1

    if count > 0:
        return total_weight / count  # Return the average weight
    else:
        return 0

# List of Pokémon names
pokemon_names = ["pikachu", "bulbasaur", "charmander"]

# Loop through Pokémon and print name and abilities
for pokemon in pokemon_names:
    data = fetch_pokemon_data(pokemon)
    if data:
        print(f"\nName: {data['name']}")
        print("Abilities:")
        for ability in data['abilities']:
            print(f"- {ability['ability']['name']}")

# Calculate and print the average weight of the Pokémon
average_weight = calculate_average_weight(pokemon_names)
print(f"\nAverage weight of the Pokémon is: {average_weight:.1f} hectograms")
