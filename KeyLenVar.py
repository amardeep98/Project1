def person(name,**data):
    print(name)
    for i, j in data.items():
        print(i, ':', j)


person('Amar',age=20,city='Patna',phone=98643567)
