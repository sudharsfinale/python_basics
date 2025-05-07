# String Methods ~ more like a few available fn to work with strings
course = "Python programming"
# all these methods create a copy of the original string that is it wont affect the actual string
print(course.lower(), "~ lower")  # convert string to lowercase
print(course.upper())  # convert string to uppercase
print(course.capitalize())  # capitalize the first letter of the string
print(course.title())  # capitalize the first letter of each word in the string
print(course.split())  # split the string into a list of words
print(course.replace("pro", "Pro"))  # replace a word in the string
# remove the leading and trailing spaces from the string, more like a trim in js
print(course.strip())
# used to check whether the char or sequence of char is not in string or not
print("prod" not in course)
# used to check whether the char or sequence of char is in string or not
print("prod" in course)
