# Collaborators (including web sites where you got help: (enter none if you didn't need help) Faceprep.in
#  

def find_gcf(x,y):   # Do not change function name!
    
    gcf = 1

    while(gcf <= x and gcf <= y): 
        if(x % gcf == 0 and y % gcf == 0):
            answergcf = gcf
        gcf = gcf + 1

    return answergcf


if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    

    # After you are satisfied with your results, use input() to prompt the user for two values:
    print("This program will tell you the greatest common factor of two numbers")
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))

    print(find_gcf(x,y))
