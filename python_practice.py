counties = ["Araphoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])


counties_dict = {"Araphoe": 422829, "Denver":463353, "Jefferson":432438}
for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county + " county has ", str(voters) + " registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict["registered_voters"])

for county_dict in voting_data:
    print(county_dict['county'])

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
    print(f'{county} county has {voters} registered voters')


candidate_votes = int(input("How many votes did the candidate get in the election ?"))
total_votes = int(input("What is the total number of votes in the election ?"))
message_to_candidate = (
    f'You recevied {candidate_votes:,} number of votes. '
    f'The total number of votes in the election was {total_votes:,} .'
    f'You received {candidate_votes / total_votes * 100:.2f} % of the total votes.'
)

print(message_to_candidate)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters.')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(f'{county_dict["county"]} has {county_dict["registered_voters"]:,} registered voters. ')
    