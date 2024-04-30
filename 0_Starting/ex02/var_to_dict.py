# Filename: var_to_dict.py

def convert_list_to_dict():
    d = [
        ('Hendrix', '1942'), ('Allman', '1946'), ('King', '1925'),
        ('Clapton', '1945'), ('Johnson', '1911'), ('Berry', '1926'),
        ('Vaughan', '1954'), ('Cooder', '1947'), ('Page', '1944'),
        ('Richards', '1943'), ('Hammett', '1962'), ('Cobain', '1967'),
        ('Garcia', '1942'), ('Beck', '1944'), ('Santana', '1947'),
        ('Ramone', '1948'), ('White', '1975'), ('Frusciante', '1970'),
        ('Thompson', '1949'), ('Burton', '1939')
    ]

    year_dict = {}
    for name, year in d:
        if year in year_dict:
            year_dict[year] += " " + name
        else:
            year_dict[year] = name
    
    return year_dict  # Return the dictionary instead of printing

if __name__ == "__main__":
    print_dict = convert_list_to_dict()
    for year in sorted(print_dict):
        print(f"{year} : {print_dict[year]}")

