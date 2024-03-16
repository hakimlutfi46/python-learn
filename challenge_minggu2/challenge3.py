input = [
    {'nama': 'Budi', 'gaji': '5000'},
    {'nama': 'Dwi', 'gaji': '8000'},
    {'nama': 'Tri', 'gaji': '6000'}
    ]

highest = max(input, key=lambda x : x['gaji'])
total = sum(map(lambda x: int(x['gaji']), input))

output = {
    "highest_salary": highest['nama'],
    "total_salary": total
}

print(output)
    


     


    
