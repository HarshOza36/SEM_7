from functools import reduce
class User:
     def __init__(self, code):
          self.code = code
     def __mul__(self, num):
          return [num * bit for bit in self.code]
     def __add__(self, oth):
          return [a + b for a, b in zip(self.code, oth)]
     def __repr__(self):
          return self.code.__str__()
     __rmul__ = __mul__


def CDMA():
     avail_codes = [
          [1] * 4,
          [1, -1, 1, -1],
          [1, 1, -1, -1],
          [1, -1, -1, 1]
     ]
     users = [User(code) for code in avail_codes]
     data = tuple(map(int, input("Enter the data of the four stations: ").split()))
     garbled = [num * user for num, user in zip(data, users)]
     final_code = User([sum(codes) for codes in zip(*garbled)])
     which_channel = int(input('Enter the channel you want to listen to[0-4]: '))
     decoded = sum([num * user for num, user in zip(final_code.code, users[which_channel].code)]) >> 2
     print(decoded, 'is the data.')
     
if __name__ == '__main__':
     CDMA()

