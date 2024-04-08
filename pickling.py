import pickle
from dataclasses import dataclass

@dataclass
class testClass:
    name: str
    age: int
    
    def name_age(self) -> str:
        return str(self.name) + " " + str(self.age) 
    

hello = testClass("liam", 403)

    
print(hello.__repr__())

# trying to do things.
pickle_string = pickle.dumps(hello)

with open("hello.pickle", 'wb') as file:
    pickle.dump(hello, file, pickle.HIGHEST_PROTOCOL)
    
    


print(pickle_string)

print(pickle.loads(pickle_string))

with open("hello.pickle", "rb") as file:
    data = pickle.load(file)
print(data.name_age())