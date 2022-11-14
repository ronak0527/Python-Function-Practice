#maximum of 3 numbers
def max_num(num1, num2, num3):
        return max([num1, num2, num3])

#multiply list elements
def mult_list(list):
        if len(list) == 0:
                return 0
        else:
                value = list[0]
                for number in list[1:]:
                        value = value * number
                return value


#recursive reverse string
def rev_string(word, i = 0):
        #base case
        if i == len(word) - 1:
                return word[0]
        #recursive case
        else:
                return word[-1-i] + rev_string(word, i + 1)


#find if number in range
def num_within(test_num, min, max):
        if test_num >= min and test_num <= max:
                return True
        else:
                return False


#pascal's triangle
triangle = [[1], [1,1]]
def pascal(num_rows):
        if num_rows < 1:
                print("Select 1 or more rows please")
        elif num_rows == 1:
                print(triangle[0])
        else:
                row_number = 2
                while len(triangle) < num_rows:
                        row = []
                        previous_row = triangle[row_number - 1]
                        row_length = len(previous_row) + 1
                        for individual_row_number in range(row_length):
                                if individual_row_number == 0:
                                        row.append(1)
                                elif individual_row_number > 0 and individual_row_number < row_length - 1:
                                        row.append(triangle[row_number-1][individual_row_number-1]+triangle[row_number-1][individual_row_number])
                                else:
                                        row.append(1) 
                        triangle.append(row)
                        row_number += 1
                for row in triangle:
                        print(row)

#tests
print(max_num(1, 2, 3))
print(max_num(18, 25031831, 4))
print(mult_list([2, 3, 4]))
print(mult_list([5, 5, 10]))
print(rev_string("Kyle"))
print(rev_string("Peanut butter and jelly"))
print(num_within(50, 1, 10))
print(num_within(5, 1, 100))
pascal(5)
pascal(7)