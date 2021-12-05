import hashlib, json
from datetime import date

cousins = "Megan", "Josiah", "Emi", "Ellie", "Bella", "Kalyn", "Abby", "Robert", "Tyler", "Truett", "Rah Rah", "Nana", "Papa", "Aunt Sissy"

class person():

    def __init__(self, name):
        self.name = name
        self.cipher = self.name + str(date.today().year)
        self.hash = hashlib.md5(self.cipher.encode()).hexdigest()
        self.URL = "https://chart.googleapis.com/chart?chs=75x75&cht=qr&chl=" + self.hash+ "&choe=UTF-8"
cousin_dict = {}
if __name__ == '__main__':
    for x in cousins:
        my_dict = person(x)
        cousin_dict[x] = my_dict

for x in cousin_dict:
    print(', '.join((cousin_dict[x].name, cousin_dict[x].hash, cousin_dict[x].URL)))
keylookup_dict ={}
for x in cousin_dict:
    keylookup_dict[cousin_dict[x].hash] = cousin_dict[x].name
print(json.dumps(keylookup_dict))


