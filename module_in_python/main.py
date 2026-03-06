# import random
#
# print(random.random())
# print(random.choifce([1,2,3,4,5,6,7,8,9,10]))

import random







import pyjokes
joke = pyjokes.get_joke(language='en')
print(joke)

#useful modules

from collections import Counter, OrderedDict, defaultdict

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 2, 3,2,22,22]
print(Counter(list))

dictionary = defaultdict(lambda: "does not exist", {"a": "a", "b": "b", "c": "c"})
print(dictionary["d"])


# Date Time module
from datetime import datetime
print(datetime.now())