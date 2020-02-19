ex18
def print_two(*args):
    arg1, arg2=args
    print("arg1:%r,arg2:%r"%(arg1,arg2))

def print_two_again(arg1, arg2):
    print("arg1:%r,arg2:%r" % (arg1,arg2))

def print_one(arg1):
    print("arg1:%r" % arg1)

def print_none():
    print("I got nothin.")

print_two("Zed","shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

ex19
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print("You have %d cheeses!"% cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese=10
amount_of_crackers=50


cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
ex20

from sys import argv

script, input_file=argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline())

current_file=open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")


current_line=1
print_a_line(current_line, current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)


for i in reversed("You are in Cape Town"):
    print(i)

ex21


def add(a,b):
    print("ADDING %d + %d" %(a,b))
    return a+b

def subtract(a,b):
    print("SUBTRACTING %d - %d "%(a, b))
    return a-b

def multiply(a,b):
    print("MULTIPLYING %d * %d"%(a,b))
    return a*b


def divide(a,b):
    print("DIVIDING %d / %d"%(a,b))
    return a/b

print("Let's do some math with just functions!")


age=add(30,5)
height=subtract(78, 4)
weight=multiply(90, 2)
iq = divide(100, 2)


print("Age: %d, Height:%d, Weight:%d, IQ: %d"%(age,height,weight,iq))

print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes: ",what, "Can you do it by hand?")
ex25
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with\\ that do \n newlines and \t tabs.')

poem="""
\tThe lovely world with logic so firmly planted cannot discern \n the needs of love nor comprehend passion from intuition and requires an explanation \n\t\twhere there is none."""

print("------------")
print(poem)
print("-------------")

five=10-2+3-6
print("This should be five :%s"%five)

def secret_formula(started):
    jelly_beans=started*500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates=secret_formula(start_point)

print("With a starting point of:%d"% start_point)
print("We'd have %d beans, %d jars,and %d crates."%(beans,jars,crates))

start_point=start_point/10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates."%secret_formula(start_point))
ex25
def break_words(stuff):
    """This function will break up words for us,"""
    words=stuff.split('')
    return words
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
def print_first_word(woords):
    """Print the first word after popping it off."""
    word=words.pop(-1)
    print(word)
def print_last_word(words):
    """Takes in a full sentence and returns the sorted words."""
    word=words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words=break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the and last words of the sentence."""
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

        