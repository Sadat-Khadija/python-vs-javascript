# Get Name
# Write a method that accepts a name from the user and then returns it.

#1 Get name
def get_name():
    """Ask the user for their name and return it."""
    name = input("What is your name? ")  # prompt the user for their name
    return name  # return whatever the user entered


#2 reverse it

def reverse_it():
    string = "a man, a plan, a canal, frenemies!"  # phrase to reverse
    reversed_str = ""  # accumulator for the reversed string
    
    for i in range(len(string)):  # walk through each index in the string
        reversed_str += string[len(string) - (i + 1)]  # append characters from the end
        
    print(reversed_str)  # show the reversed phrase
reverse_it()  # run the reversal once when the file loads

def swap_em():
    """Swap the values of two variables and print the result."""
    a = 10  # first value
    b = 30  # second value

    temp = b  # hold b temporarily
    b = a  # move a into b
    a = temp  # move original b (temp) into a

    print("a is now " + str(a) + ", and b is now " + str(b))  # display results


def multiply_array(ary):
    """
    Multiply all numbers in a list and return the product.
    If the list is empty, return 1.
    """
    if len(ary) == 0:  # handle empty list
        return 1  # neutral element for multiplication

    total = 1  # running product
    for i in range(len(ary)):  # iterate through list
        total = total * ary[i]  # multiply by each element

    return total  # give back the product


def fizzbuzzer(x):
    """
    Return 'fizz' if x divisible by 3,
    'buzz' if divisible by 5,
    'fizzbuzz' if divisible by both,
    otherwise 'archer'.
    """
    if x % (3 * 5) == 0:  # divisible by 15
        return "fizzbuzz"  # both factors
    elif x % 3 == 0:  # divisible by 3 only
        return "fizz"
    elif x % 5 == 0:  # divisible by 5 only
        return "buzz"
    else:  # not divisible by 3 or 5
        return "archer"


def nth_fibonacci_number():
    """
    Ask the user which Fibonacci number they want,
    compute it, and print the result (like the JS version).
    """
    fibs = [1, 1]  # seed list with first two Fibonacci numbers
    num_str = input("Which Fibonacci number do you want? ")  # ask user for position
    num = int(num_str)  # convert input to integer

    while len(fibs) < num:  # grow list until it has desired length
        next_fib = fibs[-2] + fibs[-1]  # calculate next number
        fibs.append(next_fib)  # append to list

    print(f"{fibs[-1]} is the fibonacci number at position {num}")  # report result


def search_array(array, value):
    """
    Search for value in array.
    Return True if found, otherwise False.
    (JS version returned true or -1; here we keep it purely boolean.)
    """
    for i in range(len(array)):  # look at each index
        if array[i] == value:  # check for match
            return True  # found it
    return False  # value not present


def is_palindrome(s):
    """
    Check if a string is a palindrome.
    Return True or False.
    """
    for i in range(len(s) // 2):  # only need to check first half
        if s[i] != s[len(s) - i - 1]:  # compare mirrored characters
            return False  # mismatch means not a palindrome
    return True  # all characters matched


def has_dupes(arr):
    """
    Check whether a list has any duplicates.
    Uses a dict (like JS object) to track seen values.
    """
    seen = {}  # dictionary to store values we've encountered
    for i in range(len(arr)):  # iterate over list
        if arr[i] in seen:  # check if value already seen
            return True  # duplicate found
        else:
            seen[arr[i]] = True  # record value as seen
    return False  # no duplicates discovered


# Optional: some quick tests when you run this file directly
if __name__ == "__main__":  # only run these examples when invoked as a script, not when imported
    print("Name test:", get_name())  # demonstrate get_name
    reverse_it()  # show reversal
    swap_em()  # swap two numbers
    print("multiply_array([1, 2, 3, 4]) ->", multiply_array([1, 2, 3, 4]))  # multiply list
    print("fizzbuzzer(15) ->", fizzbuzzer(15))  # fizzbuzz example
    nth_fibonacci_number()  # ask user for Fibonacci position and compute
    print("search_array([1, 2, 3], 2) ->", search_array([1, 2, 3], 2))  # search example
    print("is_palindrome('racecar') ->", is_palindrome("racecar"))  # palindrome check
    print("has_dupes([1, 2, 3, 2]) ->", has_dupes([1, 2, 3, 2]))  # duplicate detection
