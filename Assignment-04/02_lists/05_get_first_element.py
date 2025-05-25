# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.


def main():
    def get_first_element(lst):
        print(lst[0])
        
    user_list = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        user_list.append(element)
    
    get_first_element(user_list)

# Test the function with user input
if __name__ == "__main__":
    main()
   
