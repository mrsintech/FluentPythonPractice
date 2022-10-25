
# since python2.7 the syntax of listcomps and genexp was adapted to dict
# comprehentions (and set comprehentions as well) a dictcomp builds a dict
# instace by taking key:value pairs from any iterable.

dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

# dictcomp
country_dial = {country: code for code, country in dial_codes}

print(country_dial)

# this code return items in dict in a list of tuples
print(country_dial.items())

a = {code: country.upper()
     for country, code in sorted(country_dial.items())
     if code < 70
     }

print(a)

print(country_dial.items())
print(sorted(country_dial.items()))
