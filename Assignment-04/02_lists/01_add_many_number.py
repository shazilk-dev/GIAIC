# Write a function that takes a list of numbers and returns the sum of those numbers.

def main():
    nums = [1,2,3,4]

    def add_nums(nums):
        sum = 0
        for num in nums:
            sum += num
        return sum
    
    total_sum = add_nums(nums)
    print(total_sum)



if __name__ == "__main__":
    main()