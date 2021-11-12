import re

pattern = r'((^|(?<=\s))(-*)(\d+)((\.\d+)*)($|(?=\s)))'
text = input()
matches = re.findall(pattern, text)

for match in matches:
    number, *others = match
    print(number, end=' ')

# vrushta tuple
# v others sabira vsichki ostanali elementi na tuple
# number e na index 0 i shte e chisloto ot matcha


# purvo e positive look behind - proverqva dali predniq znak e white space ili nachalo na string
# posle - proverqva dali ima -, kato - e opcionalen
# posle - proverqva dali ima digit edin ili poveche pati
# posle, ima grupa s pod grupa v neq, gledame dali grupata e povtorena 0 ili pove4e pati, tai kato drobnata chast moje i da ne sashtestvuva
# posleden red - positive look ahead, proverqva dali znaka napred e krai na string ili krai na duma