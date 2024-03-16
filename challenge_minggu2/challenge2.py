input = [
    {'nama': 'Budi', 'nilai': '90'},
    {'nama': 'Dwi', 'nilai': '85'},
    {'nama': 'Tri', 'nilai': '75'}
    ]

def firstRank(input):
    for data in input:
        data['nilai'] = int(data['nilai'])

    sorted_data = sorted(input, key=lambda x: x['nilai'], reverse=True)
    highest_score = sorted_data[0]
    return highest_score

def lastRank(input):
    for data in input:
        data['nilai'] = int(data['nilai'])

    sorted_data = sorted(input, key=lambda x: x['nilai'])
    lowest_score = sorted_data[0]
    return lowest_score

print(firstRank(input))
print(lastRank(input))

