#Download colorama pakage first
from colorama import Fore

a = Fore.LIGHTBLUE_EX + '#########'
b = Fore.LIGHTYELLOW_EX + '\n#       #'
c ='\n' + a
d = '\n'

print(a, b*3, c, d, b*2, c, b*2, '\a')

