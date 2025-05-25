import string

#globabl const var to hold password
PASSWORD = input("enter your password: ")
#global val to hold password strength%
strength = 0

class Adders: 
    #function to determine password strength based on length of password
    def len_check(self, pwd):
        return len(pwd)*4

    #function to determine password strength based on difference in character cases
    def case_check(self, pwd):
        # variables to hold count of different cases
        upper_count = 0
        lower_count = 0

        # variable to hold password len
        len_pwd = len(pwd)

        #variables to hold strength add per case char
        up_adder = 0
        low_adder = 0
        
        #check and update case count
        for char in pwd:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
        
        # calculate case strength adders
        if upper_count > 0:
            up_adder = (len_pwd-upper_count)*2
        if lower_count > 0:
            low_adder = (len_pwd-lower_count)*2

        return [up_adder, low_adder]

    # strength adder based on numbers
    def num_check(self, pwd):
        num_count = 0
        for char in pwd: 
            if char in '0123456789': num_count += 1
        return num_count*4

    # strength adder based on special chars
    def special_check(self, pwd):
        special_count = 0
        for char in pwd: 
            if char in string.punctuation: special_count += 1
        return special_count*6

    # Strength adder if password meets minimum requirements:
    # Minimum requirements:
    # > Minimum 8 characters in length
    # > Contains 3/4 of the following:
    #     >> Uppercase Letters
    #     >> Lowercase Letters
    #     >> Numbers
    #     >> Special characters
    def req_check(self, pwd):
        len_req = True if len(pwd) >= 8 else False
        cases = self.case_check(pwd)
        case_req = 0
        case_req += 1 if cases[0] != 0 else 0
        case_req += 1 if cases[1] != 0 else 0
        num_req = 1 if self.num_check(pwd) != 0 else 0
        special_req = 1 if self.special_check(pwd) != 0 else 0

        if len_req and (case_req + num_req + special_req) >= 3:
            return len(pwd)*2
        else:
            return 0

class Subtractors: 

    def __init__(self):
        self.adder = Adders()
        self.len = len(PASSWORD)
    
    # check if the password is letters only
    def letters_only(self, pwd):
        if self.adder.num_check(pwd) + self.adder.special_check(pwd) == 0:
            return self.len
        else: return 0
    
    # check if the password is numbers only
    def num_only(self, pwd):
        upper, lower = self.adder.case_check(pwd)
        if upper + lower + self.adder.special_check(pwd) == 0:
            return self.len
        else: return 0

    # check if the password has consecutive lowercase or uppercase letters
    def consecutive_case(self, pwd):
        matches = []
        for i in range(len(pwd) - 1):
            pair = pwd[i:i+2]
            if pair.islower():
                matches.append(pair)
            elif pair.isupper():
                matches.append(pair)
        return len(matches)*2
    
    # check if the password has consecutive numbers
    def consecutive_digits(self, pwd):
        matches = []
        for i in range(len(pwd) - 1):
            pair = pwd[i:i+2]
            if pair.isdigit():
                matches.append(pair)
        return len(matches)*2
    
    # check if the password has sequential characters
    def sequential_check(self, pwd):
        matches = []
        for i in range(len(pwd) - 2):
            chars = pwd[i:i+3]
            if (int(ord(chars[0])) == int(ord(chars[1])) - 1 and int(ord(chars[1])) == int(ord(chars[2])) - 1) or (int(ord(chars[0])) == int(ord(chars[1])) + 1 and int(ord(chars[1])) == int(ord(chars[2])) + 1):
                matches.append(chars)
        return len(matches)*2

    #function to check if the password is a common password
    def common_check(self, pwd):
        with open("common-passwords.txt", "r") as file:
            passwordList = file.read().splitlines()

        if pwd in passwordList:
            return True
        return False
    
#final password strength check
def fullcheck():
    # password strength additions
    adder = Adders()
    strength = adder.len_check(PASSWORD)
    strength += adder.num_check(PASSWORD)
    strength += adder.special_check(PASSWORD)
    strength += adder.req_check(PASSWORD)
    up_adder, low_adder = adder.case_check(PASSWORD)
    strength += (up_adder + low_adder)

    subber = Subtractors()
    strength -= subber.letters_only(PASSWORD)
    strength -= subber.num_only(PASSWORD)
    strength -= subber.consecutive_case(PASSWORD)
    strength -= subber.consecutive_digits(PASSWORD)
    strength -= subber.sequential_check(PASSWORD)
    ifcommon = subber.common_check(PASSWORD)
    if ifcommon: 
        print("\n!!!The provided password is a common password and susceptable to dictionary attack!!!\n")
        if strength < 50:
            strength = 0
        else:
            strength -= 50
    
    if strength > 100:
        print("Password strength: 100%\n")
    else:
        print("Password strength:", strength, "%\n")
    

fullcheck()