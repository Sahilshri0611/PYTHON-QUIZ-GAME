questions = (
    ("Which of the following is the correct syntax for defining a function in C?",),
    ("What will be the output of the following C code?\n"
     "int main(){\n"
     "    int x = 5;\n"
     "    int y = ++x * 2;\n"
     "    printf(\"%d\", y);\n"
     "    return 0;\n"
     "}",),
    ("What is the result of the following C expression?\n"
     "int a = 10;\n"
     "int b = 5;\n"
     "printf(\"%d\", a / b * 2);",),
    ("Which of the following is NOT a valid data type in C?",),
    ("What is the purpose of the `break` statement in C?",),
    ("Which of the following functions is used to find the length of a string in C?",),
    ("What does the following C code do?\n"
     "int arr[5] = {1, 2, 3, 4, 5};\n"
     "printf(\"%d\", *(arr + 3));",),
    ("Which of the following is the correct way to create a dictionary in Python?",),
    ("What will be the output of the following Python code?\n"
     "x = 3\n"
     "y = 4\n"
     "print(x * y + 1)",),
    ("Which of the following is used to define an anonymous function in Python?",),
    ("How would you define a function that accepts an arbitrary number of arguments in Python?",),
    ("What does the following Python code do?\n"
     "a = [1, 2, 3]\n"
     "b = [4, 5, 6]\n"
     "print(a + b)",),
    ("Which of the following is NOT a valid Python data type?",),
    ("What will be the output of the following Python code?\n"
     "x = \"Hello\"\n"
     "y = \"World\"\n"
     "z = x + \" \" + y\n"
     "print(z)",),
    ("Which of the following is the correct syntax for defining a class in Python?",),
    ("What will be the output of the following Python code?\n"
     "x = 10\n"
     "def func():\n"
     "    x = 5\n"
     "    print(x)\n"
     "func()",),
    ("Which of the following is used to handle exceptions in Python?",)
)

options = (
    ("a) function_name() {}\n"
     "b) void function_name() {}\n"
     "c) function void function_name() {}\n"
     "d) def function_name() {}",),
    
    ("a) 10\n"
     "b) 12\n"
     "c) 11\n"
     "d) 14",),
    
    ("a) 4\n"
     "b) 6\n"
     "c) 8\n"
     "d) 2",),
    
    ("a) int\n"
     "b) char\n"
     "c) float\n"
     "d) real",),
    
    ("a) To skip the current iteration of a loop\n"
     "b) To stop the execution of a loop entirely\n"
     "c) To return from a function\n"
     "d) To declare a variable",),
    
    ("a) strlen()\n"
     "b) strlength()\n"
     "c) length()\n"
     "d) string_length()",),
    
    ("a) Prints `4`\n"
     "b) Prints `3`\n"
     "c) Prints `5`\n"
     "d) Prints `2`",),
    
    ("a) dict = {\"name\": \"John\", \"age\": 30}\n"
     "b) dict = [\"name\": \"John\", \"age\": 30]\n"
     "c) dict = (\"name\"=\"John\", \"age\"=30)\n"
     "d) dict = [\"name\", \"John\", \"age\", 30]",),
    
    ("a) 10\n"
     "b) 12\n"
     "c) 13\n"
     "d) 11",),
    
    ("a) lambda\n"
     "b) def\n"
     "c) funct\n"
     "d) func",),
    
    ("a) def func(*args):\n"
     "b) def func(args*):\n"
     "c) def func(...args):\n"
     "d) def func(args):",),
    
    ("a) It creates a list of tuples\n"
     "b) It merges the lists\n"
     "c) It prints `[1, 2, 3, 4, 5, 6]`\n"
     "d) It causes a TypeError",),
    
    ("a) int\n"
     "b) str\n"
     "c) float\n"
     "d) character",),
    
    ("a) `HelloWorld`\n"
     "b) `Hello World`\n"
     "c) `Hello World!`\n"
     "d) `Hello World?`",),
    
    ("a) class MyClass:\n"
     "b) class MyClass[]:\n"
     "c) class MyClass():\n"
     "d) class MyClass {}",),
    
    ("a) `5`\n"
     "b) `10`\n"
     "c) `None`\n"
     "d) `Error`",),
    
    ("a) try\n"
     "b) catch\n"
     "c) throw\n"
     "d) except",)
)

correct_answers = (
    "d) def function_name() {}",   
    "b) 12",                    
    "b) 6", 
    "d) real",                
    "b) To stop the execution of a loop entirely",   
    "a) strlen()",                
    "a) Prints `4`",             
    "a) dict = {\"name\": \"John\", \"age\": 30}",   
    "c) 13",                      
    "a) lambda",               
    "a) def func(*args):",    
    "c) It prints `[1, 2, 3, 4, 5, 6]`",  
    "d) character",               
    "b) `Hello World`",         
    "a) class MyClass:",       
    "a) `5`",                    
    "a) try",                     
)

guesses = []
score = 0
q_n = 0

for q in questions:
    print("------------------------------------------------------------------------------------------")
    print(q[0])  
    
    
    for opt in options[q_n]:
        for line in opt.split("\n"):
            print(line)   
    guess = input("Enter the correct option (a.)(b.)(c.)(d.): ").lower()
    guesses.append(guess)
    
     
    if guess == correct_answers[q_n].lower():
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer was: {correct_answers[q_n]}")
    
    
    q_n += 1

 
print(f"Your total score is: {score}/{len(questions)}")
