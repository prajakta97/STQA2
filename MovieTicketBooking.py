#Online Ticket Booking System

def username():
    a = input("Enter Username: ")
    return a
    
def password():
    a = input("Enter Password: ")
    return a
# This function is used to select the city
def city():
    print("Hi! Welcome to Movie Ticket Booking!")
    print("Where do you want to watch the movie?")
    print("1: Mumbai")
    print("2: Pune")
    print("3: Nashik")
    a = int(input("Choose a city: "))
    return a

# This function is used to select the theatre
def theatre():
    print("In which theater do you wish to see the movie?")
    print("1: Symbosis")
    print("2: Uma")
    print("3: lamninarayan")
    a = int(input("Choose a theatre: "))
    return a

# This function is used to select the movie
def movie():
    print("Which movie do you want to watch?")
    print("1: Surywanshi")
    print("2: Joker")
    print("3: Sigham")
    a = int(input("Choose a movie: "))
    return a

# This function is used to select the screen
def screen():
    print("On which screen do you want to watch the movie?")
    print("1: SCREEN 1")
    print("2: SCREEN 2")
    print("3: SCREEN 3")
    a = int(input("Choose a screen: "))
    b = int(input("How many tickets do you want?" ))
    return a

# This function is used to select the timing
def timing(a):
    time1 = {
        1: "10:00 AM - 1:00 PM",
        2: "1:10 PM - 4:10 PM",
        3: "4:20 PM - 7:20 PM",
        4: "7:30 PM - 10:30 PM"
    }
    time2 = {
        1: "10:15 AM - 1:15 PM",
        2: "1:25 PM -4:25 PM",
        3: "4:35 PM - 7:35 PM",
        4: "7:45 PM-10:45 PM"
    }
    time3 = {
        1: "10:30 AM - 1:30 PM",
        2: "1:40 PM - 4:40 PM",
        3: "4:50 PM - 7:50 PM",
        4: "8:00 PM - 10:45 PM"
    }
    if a == 1:
        print(time1)
        t = int(input("Choose your time: "))
        x = time1[t]
        return t
    elif a == 2:
        print(time2)
        t = int(input("Choose your time: "))
        x = time2[t]
        return t
    elif a == 3:
        print(time3)
        t = int(input("Choose your time: "))
        x = time3[t]
        return t

if __name__ == '__main__':
    username()
    password()
    city()
    theatre()
    movie()
    s=screen()
    tm=timing(s)
    print("Booking successful! Enjoy your movie!")