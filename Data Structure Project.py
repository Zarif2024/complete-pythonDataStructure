import sys
import os
def data_structure():
    print(
        """                                            Welcome!
                  Thisprogram is about Data Structur&Algorithm.
                  You can use it to learn some basic concepts of Data structure.
          
                   Worked on by:
                   Mohammad Zarif""")
    
#++++++++++++++++++++++++Start of Algorithms++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def algorithm():# Define A function called algorithms
        algorithm_choose = input("Select one option:\n1:definition \n2: example\n3: code\n4: categories \n0: Back\nYour Choice:")# choose from algorithm parts

        if algorithm_choose == "1":
            print(
                """Algorithm are:
            Well defined list of steps for solving a problem.
            A finite sequence of instructions, each of which has a clear meaning and can be performed with a finite amount of effort in a finite length of time.

            """
            )
            algorithm()
        elif algorithm_choose == "2":
            print(
                """
Adding two Numbers and Displaying the result:
Step 1 − START 
Step 2 − declare three integers a, b & c 
Step 3 − define values of a & b 
Step 4 − add values of a & b 
Step 5 − store output of step 4 to c 
Step 6 − print c 
Step 7 − STOP

            """
            )
            algorithm()
        elif algorithm_choose == "3":
            print("Algorithms For Adding Two Numbers:")
            print("enter tow numbers for adding them")
            a = int(input("enter a: "))
            b = int(input("enter b: "))
            c = a + b
            print("The Result:", c)
            algorithm()
        elif algorithm_choose == "0":
            data_structure()
        elif algorithm_choose == "4":
            def Categories():# Define A function called categories
                categories = input("Select one option:\n  1:sort \n  2: search\n  0: Back \n   Your Choice:\n")
                if categories == "0":
                    algorithm()
                elif categories == "1":
                    def Sort_Algorithms():# Define A function called Sort algorithms
                        sort_algorithm =input("Select one option:\n1:heap sort \n2: radix sort\n3: bingo sort\n4: selection sort\n5: insertion sort\n6: merge sort\n7: tim sort\n8: quick sort\n0: Back \nYour Choice:\n" )
                        if sort_algorithm == "0":
                            algorithm()
                        elif sort_algorithm == "1":
                            def Heap_Sort():# Define A function called Sort algorithms
                                heap_sort =input("Select one option:\n1: defination \n2: Algorithms And example\n0: Back\nYour Choice:\n")

                                if heap_sort == "1":
                                    print(
                                        """
            heap sort: 
            Heap sort is a sorting algorithm that uses a binary heap data structure to sort an array of elements. 
            It works by building a heap from the array and repeatedly extracting the maximum element from the heap and placing it at the end of the array. 
            This process is repeated until the entire array is sorted in ascending or descending order.
            Heap sort has a time complexity of O(n log n) and is an efficient sorting algorithm for large datasets.
                                    """
                                    )
                                    Heap_Sort()
                                elif heap_sort == "0":
                                    Sort_Algorithms()
                                elif heap_sort == "2":
                                    print(
                                        """Algorithm for Heap Sort:
                                        1. Build a max heap from the given array.
                                        2. Swap the root node with the last element in the heap.
                                        3. Remove the last element from the heap and reduce the size of the heap.
                                        4. Heapify the root node to maintain the max heap property.
                                        5. Repeat steps 2-4 until the heap size is 1.
                                        """
                                    )

                                    def create_array(size, data_type):# Define A function called Create Array
                                        array = []
                                        print(f"Enter {size} elements of type {data_type.__name__}:")
                                        for i in range(size):
                                            while True:
                                                try:
                                                    element = input("Enter Element:")
                                                    if data_type == int:
                                                        element = int(element)
                                                    elif data_type == str:
                                                        element = str(element)
                                                    else:
                                                        raise ValueError("Invalid data type.")
                                                    array.append(element)
                                                    break
                                                except ValueError:
                                                    print(f"Invalid data type. Expected {data_type.__name__}. Please try again.")
                                        return array

                                    def heapify(array, n, i):# Define A function called Heapify
                                        largest = i
                                        left = 2 * i + 1
                                        right = 2 * i + 2

                                        if left < n and array[i] < array[left]:
                                            largest = left

                                        if right < n and array[largest] < array[right]:
                                            largest = right

                                        if largest != i:
                                            array[i], array[largest] = array[largest], array[i]
                                            print(f"Swapped {array[i]} and {array[largest]}")#print how the  sort is done
                                            print(f"Array: {array}")

                                            heapify(array, n, largest)

                                    def heap_sort(array):# Define A function called heap sort
                                        n = len(array)

                                        # Build max heap
                                        for i in range(n, -1, -1):
                                            heapify(array, n, i)

                                        print(f"\nMax Heap: {array}")
                                        print("------------------------------")

                                        # Extract elements from heap
                                        for i in range(n - 1, 0, -1):
                                            array[i], array[0] = array[0], array[i]
                                            print(f"Swapped {array[i]} and {array[0]}")
                                            print(f"Array: {array}")

                                            heapify(array, i, 0)

                                        print("\nSorted Array:", array)

                                    # Main program
                                    try:
                                        size = int(input("Enter the size of the array: "))# Promptinting the size of the array
                                    except ValueError:
                                        print("Invalid size. Size must be an integer.")
                                        Heap_Sort()

                                    while True:
                                        data_type = input("Enter 'int' for integer array or 'str' for string array: ")#Choose Data type
                                        if data_type == "int":
                                            data_type = int
                                            break
                                        elif data_type == "str":
                                            data_type = str
                                            break
                                        else:
                                            print("Invalid choice. Please try again.")

                                    array = create_array(size, data_type)
                                    print("\nOriginal Array:", array)
                                    heap_sort(array)
                                    Heap_Sort()
                                else:
                                    print("invalid Input")
                                    Heap_Sort()
                            Heap_Sort()

                        elif sort_algorithm == "2":
                            def Radix_Sort():# Define A function called radix sort
                                radix_sort =input("Select one option:\n1: defination \n2: Algorithms and example\n0:Back \nYour Choice:\n")#prompt the radix sort parts
                                if radix_sort=="0":#call the sort algorithms to go back
                                    Sort_Algorithms()

                                elif radix_sort == "1":
                                    print(
                                        """
            radix sort: 
            Radix sort is a sorting algorithm that sorts elements by their digits, starting from the least significant digit to the most significant digit.
                                    """
                                    )
                                    Radix_Sort()
                                elif radix_sort == "2":
                                    print(
                                        """Algorithm for Radix Sort:
                                        1. Find the maximum element in the array.
                                        2. Count the number of digits in the maximum element.
                                        3. For each digit position from least significant to most significant:
                                            a. Create a bucket for each digit (0-9).
                                            b. Iterate through the array and place each element in the appropriate bucket based on the current digit.
                                            c. Concatenate all the buckets in order to create a new array.
                                        4. Repeat step 3 until all digit positions have been processed.
                                        """
                                    )

                                    def counting_sort(arr, digit):  # function for counting sort
                                        n = len(arr)
                                        output = [0] * n
                                        count = [0] * 256  # initialize count array with 256 zeros

                                        for i in range(n):
                                            index = ord(arr[i][digit]) if isinstance(arr[i], str) else arr[i] // (
                                                        10 ** digit) % 10
                                            count[index] += 1  # count the occurrence of each element

                                        for i in range(1, 256):
                                            count[i] += count[
                                                i - 1]  # modify the count array by adding the previous counts

                                        for i in range(n - 1, -1, -1):
                                            index = ord(arr[i][digit]) if isinstance(arr[i], str) else arr[i] // (
                                                        10 ** digit) % 10
                                            output[count[index] - 1] = arr[i]
                                            count[index] -= 1

                                        for i in range(n):
                                            arr[i] = output[i]

                                    def radix_sort(arr):
                                        """
                                        Sorts the elements of the given list using radix sort algorithm.

                                        Parameters:
                                        arr (list): List of elements to be sorted.

                                        Returns:
                                        list: Sorted list.
                                        """
                                        if len(arr) == 0:
                                            return arr# arr (list): List of elements to be sorted.

                                        max_len = max(len(str(x)) if isinstance(x, int) else len(x) for x in arr)

                                        for digit in range(max_len):
                                            # Sort the elements based on the specified digit
                                            counting_sort(arr, digit)

                                        return arr

                                    try:
                                        size = int(input("Enter the size of the array: "))
                                        array_type = input(
                                            "Enter 'int' for array of integers, 'str' for array of strings: ")

                                        if array_type == "int":
                                            array = []
                                            for i in range(size):
                                                val = int(input(f"Enter integer at index {i}: "))
                                                array.append(val)
                                        elif array_type == "str":
                                            array = []
                                            for i in range(size):
                                                val = input(f"Enter string at index {i}: ")
                                                array.append(val)
                                        else:
                                            raise ValueError("Invalid array type")

                                        # Print the original and sorted arrays
                                        print("\nOriginal Array:", array)
                                        sorted_array = radix_sort(array)
                                        print("\nSorted Array:", sorted_array)

                                    except Exception as e:
                                        print(e)

                                    Radix_Sort()
                                else:
                                    print("invalid Input")
                                    Radix_Sort()

                            Radix_Sort()


                        elif sort_algorithm == "3":
                            def Bingo_Sort():
                                bingo_sort =input("Select one option:\n1: defination \n2: Algorithms And example\n0:Back\nWhich One:")
                                if bingo_sort=="0":
                                    Sort_Algorithms()
                                if bingo_sort == "1":
                                    print(
                                        """
            bingo sort: 
            Bingo sort is a sorting algorithm that works by repeatedly picking two elements at random and swapping them if they are in the wrong order.
            It continues until the array is sorted."""
                                    )
                                    Bingo_Sort()
                                elif bingo_sort == "2":
                                    print(
                                        """Algorithm for Bingo Sort:
                                            1. Divide the input array into subarrays of size sqrt(n), where n is the size of the input array.
                                            2. Sort each subarray using any sorting algorithm.
                                            3. Create a bucket for each subarray.
                                            4. Iterate through the input array and place each element in the appropriate bucket based on which subarray it belongs to.
                                            5. Iterate through each bucket and sort its contents using any sorting algorithm.
                                            6. Concatenate the sorted subarrays to create the final sorted array.
                                            """
                                    )
                                    def bingo_sort(arr):# function for bingo sort
                                        n = len(arr)

                                        while True:
                                            swapped = False

                                            for i in range(0, n-1, 2):
                                                if arr[i] > arr[i+1]:
                                                    arr[i], arr[i+1] = arr[i+1], arr[i]
                                                    swapped = True
                                                    print(f"Swapped {arr[i]} and {arr[i+1]}")#Print the Swapping Mechanism
                                                    print("Current array:", arr)

                                            for i in range(1, n-1, 2):
                                                if arr[i] > arr[i+1]:
                                                    arr[i], arr[i+1] = arr[i+1], arr[i]
                                                    swapped = True
                                                    print(f"Swapped {arr[i]} and {arr[i+1]}")#Print the Swapping Mechanism
                                                    print("Current array:", arr)

                                            if not swapped:#breaks if no swapping occurred
                                                break

                                    def create_array():# function for bingo sort
                                        size = int(input("Enter the size of the array: "))# gets the size of the Array

                                        valid_input = False
                                        while not valid_input:
                                            try:
                                                element_type = int(input("Enter 1 for integers or 2 for strings: "))
                                                valid_input = True
                                            except ValueError:
                                                print("Invalid input. Please enter a valid option.")

                                        arr = []
                                        for i in range(size):
                                            valid_input = False
                                            while not valid_input:
                                                try:
                                                    if element_type == 1:
                                                        element = int(input(f"Enter integer at index {i}: "))
                                                    elif element_type == 2:
                                                        element = input(f"Enter string at index {i}: ")
                                                    valid_input = True
                                                except ValueError:
                                                    print("Invalid input. Please enter a valid element.")

                                            arr.append(element)

                                        return arr

                                    try:
                                        arr = create_array()
                                        print("Input array:", arr)

                                        bingo_sort(arr)
                                        print("Sorted array:", arr)# prints the sorted Array
                                    except Exception as e:
                                        print("An error occurred:", str(e))
                                    Bingo_Sort()
                                else:
                                    print("Invalid Input!!!!")
                                    Bingo_Sort()
                            Bingo_Sort()

                        elif sort_algorithm == "4":
                            def Selection_Sort():# function for Selection sort
                                selection_sort = input("Select one option:\n   1: defination \n   2:Algorithms and example\n   0:Back \n   Which One:")#input parts of selection sort
                                if selection_sort=="0":
                                    Sort_Algorithms()
                                if selection_sort == "1":
                                    print(
                                        """
            selection sort: 
            Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element
            from an unsorted portion of the array and swapping it with the first element of the unsorted portion.
                                    """
                                    )
                                    Selection_Sort()
                                elif selection_sort == "2":
                                    print(
                                        """
            Algorithm for Selection Sort:
            1. Start with the first element of the array.
            2. Find the smallest element in the array and swap it with the first element.
            3. Move to the second element and repeat step 2 for the remaining elements in the array.
            """
                                    )

                                    def selection_sort(arr):
                                        for i in range(len(arr)):
                                            # Find the index of the minimum element in the unsorted portion of the list
                                            min_index = i
                                            for j in range(i + 1, len(arr)):
                                                if arr[j] < arr[min_index]:
                                                    min_index = j

                                            # Swap the minimum element with the first element in the unsorted portion of the list
                                            arr[i], arr[min_index] = arr[min_index], arr[i]

                                            # Print the current state of the list after each iteration
                                            print(f"Step {i + 1}: {arr}")

                                        return arr

                                    try:
                                        size = int(input("Enter the size of the array: "))
                                        arr_type = input("Choose the type of array (int/str): ")

                                        if arr_type not in ["int", "str"]:
                                            raise ValueError("Invalid array type")

                                        arr = []
                                        for i in range(size):
                                            if arr_type == "int":
                                                value = int(input(f"Enter the {i+1}th integer: "))
                                            else:
                                                value = input(f"Enter the {i+1}th string: ")
                                            arr.append(value)

                                        sorted_arr = selection_sort(arr[:]) # Create a copy of array for sorting

                                        print(f"\nOriginal Array: {arr}")
                                        print(f"Sorted Array: {sorted_arr}")
                                    except ValueError as e:
                                        print(f"Error: {e}")
                                    except Exception as e:
                                        print(f"An error occurred: {e}")
                                    Selection_Sort()
                                else:
                                    print("Invalid Input!!!!")
                                    Selection_Sort()


                            Selection_Sort()

                        elif sort_algorithm == "5":
                            def Insertion_Sort():# function for Selection sort
                                insertion_sort = input("Select one option:\n1: definition \n2:Algorithms and example\n0:Back \nWhich One:")
                                if insertion_sort=="0":
                                    Sort_Algorithms()
                                if insertion_sort == "1":
                                    print(
                                        """
            insertion sort: 
            Insertion sort is a simple sorting algorithm that works by repeatedly inserting each element in the correct position in a sorted subarray.
                                    """
                                    )
                                    Insertion_Sort()
                                elif insertion_sort == "2":
                                    print(
                                        """Algorithm for Insertion Sort:
            1. Start with the second element of the array.
            2. Compare the second element with the first element. If the second element is smaller, swap them.
            3. Move to the third element and compare it with the second element. If it is smaller, swap them. If not, compare it with the first element and swap if necessary.
            4. Repeat step 3 for all remaining elements in the array.
            """
                                    )

                                    def insertion_sort(arr):
                                        for i in range(1, len(arr)):
                                            # Store the current element in a variable
                                            key = arr[i]
                                            j = i - 1

                                            # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
                                            while j >= 0 and arr[j] > key:
                                                arr[j + 1] = arr[j]
                                                j -= 1

                                            # Insert the key element at its correct position in the sorted sequence
                                            arr[j + 1] = key

                                            # Print the current state of the list after each iteration
                                            print(f"Step {i}: {arr}")

                                        return arr

                                    try:
                                        size = int(input("Enter the size of the array: "))
                                        arr_type = input("Choose the type of array (int/str): ")

                                        if arr_type not in ["int", "str"]:
                                            raise ValueError("Invalid array type")

                                        arr = []
                                        for i in range(size):
                                            if arr_type == "int":
                                                value = int(input(f"Enter the {i + 1}th integer: "))
                                            else:
                                                value = input(f"Enter the {i + 1}th string: ")
                                            arr.append(value)

                                        sorted_arr = insertion_sort(arr[:])  # Create a copy of array for sorting

                                        print(f"\nOriginal Array: {arr}")
                                        print(f"Sorted Array: {sorted_arr}")
                                    except ValueError as e:
                                        print(f"Error: {e}")
                                    except Exception as e:
                                        print(f"An error occurred: {e}")
                                    Insertion_Sort()
                                else:
                                    print("Invalid InPUt!!!")
                                    Insertion_Sort()
                            Insertion_Sort()

                        elif sort_algorithm == "6":
                            def Merge_Sort():# function for Merge sort
                                merge_sort = input("Select one option:\n1: definition \n2:Algorithms and example\n 0:Back \nWhich One:")
                                if merge_sort=="0":
                                    Sort_Algorithms()
                                elif merge_sort == "1":
                                    print(
                                        """
            merge sort:
            Merge sort is a sorting algorithm that works by dividing the array into two halves, 
            sorting each half recursively, and then merging the two sorted halves.
                                    """
                                    )
                                    Merge_Sort()

                                elif merge_sort == "2":
                                    print(
                            """Algorithm for Merge Sort:
        1. Divide the array into two halves.
        2. Recursively sort each half.
        3. Merge the two sorted halves
        """
                                )

                                def merge_sort(arr):
                                    print(f"Splitting array: {arr}")

                                    # Base case: return if the list has only one element
                                    if len(arr) <= 1:
                                        return arr

                                    # Divide the list into two halves
                                    mid = len(arr) // 2
                                    left = arr[:mid]
                                    right = arr[mid:]

                                    # Recursively sort the two halves
                                    left = merge_sort(left)
                                    right = merge_sort(right)

                                    # Merge the sorted halves
                                    return merge(left, right)

                                def merge(left, right):
                                    merged = []
                                    left_index = right_index = 0

                                    while left_index < len(left) and right_index < len(right):
                                        if left[left_index] < right[right_index]:
                                            merged.append(left[left_index])
                                            left_index += 1
                                        else:
                                            merged.append(right[right_index])
                                            right_index += 1

                                    merged.extend(left[left_index:])
                                    merged.extend(right[right_index:])

                                    print(f"Merging: {left} and {right} -> {merged}")
                                    return merged

                                def create_array(size, datatype):#Function for creating the array
                                    arr = []#initializing array

                                    for i in range(size):
                                        while True:
                                            try:
                                                if datatype == "1":
                                                    item = int(input(f"Enter integer at index {i}: "))
                                                elif datatype == "2":
                                                    item = input(f"Enter string at index {i}: ")
                                                else:
                                                    raise ValueError("Invalid datatype choice! Only '1' or '2' allowed.")

                                                arr.append(item)
                                                break
                                            except ValueError:
                                                print("Invalid input! Please try again.")

                                    return arr

                                try:
                                    size = int(input("Enter the size of the array: "))
                                    datatype = input("Enter the datatype for the array (1 for integers, 2 for strings): ")

                                    array = create_array(size, datatype)
                                    print("Original Array:", array)

                                    sorted_array = merge_sort(array)
                                    print("Sorted Array:", sorted_array)
                                    Merge_Sort()

                                except ValueError as err:
                                    print("Error:", err)
                                    Merge_Sort()
                                else:
                                    print("Invalid Input!!!")
                                    Merge_Sort()
                            Merge_Sort()



                        elif sort_algorithm == "7":
                            def Tim_Sort():# Function For Tim sort
                                tim_sort = input("Select one option:\n1: defination \n2:Algorithms And example\n0:Back \n Which One:" )
                                if tim_sort=="0":
                                    Sort_Algorithms()
                                if tim_sort == "1":
                                    print(
                                        """
            Tim sort is a hybrid sorting algorithm that combines insertion sort and merge sort. 
            It works by dividing the array into small subarrays, sorting them using insertion sort, and then merging them using merge sort.
                                    """
                                    )
                                    Tim_Sort()
                                elif tim_sort == "2":
                                    print(
                                        """Tim Sort Algorithm:
        
            1. Divide the array into small subarrays of size RUN. The size of the RUN can be any value, but it is usually set to 32 or 64.
            2. Sort each subarray using insertion sort algorithm.
            3. Merge the sorted subarrays using merge sort algorithm.
            4. Repeat the above steps until the entire array is sorted.
            """
                                    )

                                    # Function to sort an array based on the type of items it contains
                                    def tim_sort(arr, item_type):
                                        # If the items are integers
                                        if item_type == 'int':
                                            # Sort the array in ascending order
                                            arr.sort()
                                        # If the items are strings
                                        elif item_type == 'str':
                                            # Sort the array in alphabetical order, ignoring case
                                            arr.sort(key=str.lower)
                                        # If the item type is neither 'int' nor 'str'
                                        else:
                                            # Raise an error
                                            raise ValueError("Invalid item type. Please choose 'int' or 'str'.")

                                    # Function to merge two sorted arrays into a single sorted array
                                    def merge(left, right, arr):
                                        i, j, k = 0, 0, 0

                                        # Merge elements from both arrays in sorted order
                                        while i < len(left) and j < len(right):
                                            if left[i] <= right[j]:
                                                arr[k] = left[i]
                                                i += 1
                                            else:
                                                arr[k] = right[j]
                                                j += 1
                                            k += 1

                                        # Copy remaining elements of left array if any
                                        while i < len(left):
                                            arr[k] = left[i]
                                            i += 1
                                            k += 1

                                        # Copy remaining elements of right array if any
                                        while j < len(right):
                                            arr[k] = right[j]
                                            j += 1
                                            k += 1

                                    # Function to implement TimSort algorithm on an array and print each step
                                    def tim_sort_steps(arr, item_type):
                                        # Base case: if the array has one or no elements, it is already sorted
                                        if len(arr) <= 1:
                                            return arr

                                        # Find the middle point of the array
                                        mid = len(arr) // 2
                                        # Divide the array into two halves
                                        left = arr[:mid]
                                        right = arr[mid:]

                                        # Recursively sort both halves
                                        tim_sort_steps(left, item_type)
                                        tim_sort_steps(right, item_type)

                                        # Merge both halves back into a single sorted array
                                        merge(left, right, arr)

                                        # Print the current state of the array after each merge step
                                        print("Current state of the array:", arr)

                                    def create_array(size, item_type):
                                        arr = []
                                        for _ in range(size):
                                            if item_type == 'int':
                                                num = int(input("Enter an integer number: "))
                                                arr.append(num)
                                            elif item_type == 'str':
                                                string = input("Enter a string: ")
                                                arr.append(string)
                                            else:
                                                raise ValueError("Invalid item type. Please choose 'int' or 'str'.")
                                        return arr

                                    size = int(input("Enter the size of the array: "))
                                    item_type = input(
                                        "Enter 'int' for an array of integers or 'str' for an array of strings: ")

                                    try:
                                        arr = create_array(size, item_type)
                                        print("Original array:", arr)
                                        tim_sort_steps(arr, item_type)
                                        print("Final sorted array:", arr)
                                        Tim_Sort()
                                    except ValueError as e:
                                        print(str(e))
                                        Tim_Sort()
                                else:
                                    print("Invalid Input!!!")
                                    Tim_Sort()

                            Tim_Sort()
                        elif sort_algorithm == "8":
                            def Quick_Sort():
                                quick_sort = input("Select one option:\n1: definition \n2:Algorithms and example\n0:Back \nWhich One:")
                                if quick_sort=="0":
                                    Sort_Algorithms()
                                if quick_sort == "1":
                                    print(
                                        """
            Quick sort is a popular sorting algorithm that works by partitioning the array into two subarrays based on a pivot element, 
            and then recursively sorting the subarrays.
                                    """
                                    )
                                    Quick_Sort()
                                elif quick_sort == "2":
                                    print(
                                        """Algorithm for Quick Sort:
            1. Choose a pivot element from the input array.
            2. Partition the input array into two subarrays: one containing elements smaller than the pivot, and one containing elements larger than the pivot.
            3. Recursively apply steps 1 and 2 to each subarray until the subarrays have length 1 or 0.
            4. Concatenate the sorted subarrays to create the final sorted array.
            """)

                                    # Function to implement QuickSort algorithm on an array
                                    def quicksort(arr):
                                        # Base case: if the array has one or no elements, it is already sorted
                                        if len(arr) <= 1:
                                            return arr
                                        else:
                                            # Choose the first element as the pivot
                                            pivot = arr[0]
                                            print("Pivot:", pivot)  # Print the pivot

                                            # Partition the array into two sub-arrays: one with elements less than or equal to the pivot and one with elements greater than the pivot
                                            lesser = [x for x in arr[1:] if x <= pivot]
                                            print("Elements less than or equal to pivot:",
                                                  lesser)  # Print the elements less than or equal to the pivot
                                            greater = [x for x in arr[1:] if x > pivot]
                                            print("Elements greater than pivot:",
                                                  greater)  # Print the elements greater than the pivot

                                            # Recursively sort both sub-arrays and combine them with the pivot in between
                                            sorted_array = quicksort(lesser) + [pivot] + quicksort(greater)
                                            print("Sorted array:", sorted_array)  # Print the sorted array

                                            # Return the sorted array
                                            return sorted_array

                                    try:
                                        size = int(input("Enter the size of the array: "))
                                        if size <= 0:
                                            raise ValueError("Size should be a positive integer.")

                                        array_type = input(
                                            "Enter 'int' to create an array of integers or 'str' to create an array of strings: ")
                                        if array_type not in ['int', 'str']:
                                            raise ValueError("Invalid array type specified. Please choose 'int' or 'str'.")

                                        array = []
                                        for i in range(size):
                                            if array_type == 'int':
                                                element = int(input(f"Enter element {i + 1}: "))
                                            else:
                                                element = input(f"Enter element {i + 1}: ")
                                            array.append(element)

                                        print("Original array:", array)
                                        sorted_array = quicksort(array)
                                        print("Final sorted array:", sorted_array)

                                    except ValueError as ve:
                                        print("Error:", ve)
                                        Quick_Sort()
                                    except Exception as e:
                                        print("An error occurred:", e)
                                        Quick_Sort()
                                else:
                                    print("Invalid Input!!!")
                                    Quick_Sort()
                            Quick_Sort()
                        else:
                            print("Invalid Input!!!")
                            Sort_Algorithms()
                    Sort_Algorithms()

                elif categories == "2":
                    def search():
                        search_input =input("Select One Option: \n 1: definition\n 2:Types\n0:Back\n Your Choice: ")
                        if search_input =="0":
                            Categories()

                        elif search_input == "1":
                            print("Search:\nSearch algorithms work to retrive information stored within a particular data structure")
                            search()
                        elif search_input == "2":
                            def all_types():
                                type =input("There are four types of searching!\n\t 1: Linear Search\n\t 2: Binary search\n\t 3: Hash search\n\t 4: tree-based\n\t0 : Back\n")
                                def types():
                                    if type=="0":
                                        search()
                                    elif type == "1":
                                        def linear():
                                            linear_input =input("Choose an option:\n\t 1: Definition\n\t2:Algorithm and Implementation\n\t0 : Back\n")
                                            if linear_input=="0":
                                                all_types()
                                            elif linear_input =="1":
                                                print("Linear Search:\n This is the simplest searching algorithm, where each element in the data structure is checked one by one until the desired element is found or the end of the structure is reached. ")
                                                linear()
                                            elif linear_input == "2":
                                                print( """ Here is how we create:
                                                            start
                                                            1. Initialize a variable "found" as False.
                                                            2. Request the user to enter the size of the data structure.
                                                            3. Create an empty list called "data".
                                                            4. Request the user to enter the elements of the data structure one by one and append them to the "data" list.
                                                            5. Request the user to enter the element to be searched and store it in a variable called "search_element".
                                                            6. Iterate through each element in the "data" list:
                                                            - If the current element is equal to the "search_element", set "found" as True and break the loop.
                                                            7. If "found" is True, print "Element found at position: " followed by the index of the element in the "data" list.
                                                            8. If "found" is False, print "Element not found in the data structure
                                                            End
                                                            """)
                                                print("Implementation of Linear Search:")

                                                # Function to perform linear search on an array of integers
                                                def linear_search_integers(data, element):
                                                    steps = 0  # Initialize a counter for the number of steps taken
                                                    for i, item in enumerate(
                                                            data):  # Loop through each item in the data
                                                        steps += 1  # Increment the steps counter
                                                        if item == element:  # If the current item is equal to the search element
                                                            # Return a message indicating that the element was found, its index, and the number of steps taken
                                                            return f"The element '{element}' found at index {i} in the data structure. Steps taken: {steps}"
                                                    # If the loop completes without finding the element, return a message indicating that the element was not found and the number of steps taken
                                                    return f"The element '{element}' was not found in the data structure. Steps taken: {steps}"

                                                # Function to perform linear search on an array of strings
                                                def linear_search_strings(data, element):
                                                    steps = 0  # Initialize a counter for the number of steps taken
                                                    for i, item in enumerate(
                                                            data):  # Loop through each item in the data
                                                        steps += 1  # Increment the steps counter
                                                        if item == element:  # If the current item is equal to the search element
                                                            # Return a message indicating that the element was found, its index, and the number of steps taken
                                                            return f"The element '{element}' found at index {i} in the data structure. Steps taken: {steps}"
                                                    # If the loop completes without finding the element, return a message indicating that the element was not found and the number of steps taken
                                                    return f"The element '{element}' was not found in the data structure. Steps taken: {steps}"

                                                try:
                                                    size = int(input("Enter the size of the data structure: "))
                                                    data_type = input("Choose the data type (integers/strings): ")

                                                    if data_type not in ['integers', 'strings']:
                                                        raise ValueError("Invalid data type selected.")

                                                    if data_type == 'integers':
                                                        data = []
                                                        for i in range(size):
                                                            data.append(int(input(f"Enter an integer for index {i}: ")))

                                                        search_element = int(
                                                            input("Enter the element to search (integer): "))
                                                        result = linear_search_integers(data, search_element)
                                                    else:
                                                        data = []
                                                        for i in range(size):
                                                            data.append(input(f"Enter a string for index {i}: "))

                                                        search_element = input("Enter the element to search (string): ")
                                                        result = linear_search_strings(data, search_element)

                                                    # Print each step of the linear search
                                                    print("Step-by-step search process:")
                                                    for i, item in enumerate(data):
                                                        print(f"Checking index {i} with value: {item}")
                                                        if item == search_element:
                                                            print(f"The element '{search_element}' found at index {i}")
                                                            linear()
                                                    else:
                                                        print(f"The element '{search_element}' was not found in the data structure")
                                                        linear()
                                                    print(result)

                                                except ValueError as e:
                                                    print(f"An error occurred: {str(e)}")
                                                    linear()
                                            else:
                                                print("Invalid Input!!!")
                                                linear()
                                        linear()


                                    elif type == "2":

                                        def binary():
                                            binary_input =input("Choose an option:\n\t 1: Definition\n\t 2:Algorithm And Implementation\n\t 0 : Back\n")
                                            if binary_input=="0":
                                                all_types()
                                            elif binary_input=="1":
                                                print("Binary Search:\n This algorithm is used for searching in sorted arrays or lists."+ ""
                                                    "It divides the search space in half with each comparison, eliminating half of the remaining elements until the desired element is found. ")
                                                binary()

                                            elif binary_input == "2":
                                                print(
                                                            """ Here is Algorithm:
                                                        Start
                                                        1. Get the input from the user for the search element.
                                                            2. Initialize variables low and high to the first and last index of the list.
                                                            3. Repeat the following steps until low is less than or equal to high:
                                                            - Calculate the middle index, mid, as the average of low and high.
                                                            - If the middle element is equal to the search element, return the middle index.
                                                            - If the middle element is greater than the search element, update high to mid - 1.
                                                            - If the middle element is less than the search element, update low to mid + 1.
                                                            4. If the search element is not found, return -1
                                                            End
                                                       """
                                                        )
                                                print("Implementation of Binary Search")

                                                # Function to perform binary search on a sorted array
                                                def binary_search(arr, target):
                                                    # Initialize the low and high pointers
                                                    low = 0
                                                    high = len(arr) - 1

                                                    # While the low pointer is less than or equal to the high pointer
                                                    while low <= high:
                                                        # Calculate the mid index
                                                        mid = (low + high) // 2
                                                        # If the element at the mid index is equal to the target
                                                        if arr[mid] == target:
                                                            # Return the mid index
                                                            return mid
                                                        # If the element at the mid index is less than the target
                                                        elif arr[mid] < target:
                                                            # Move the low pointer to mid + 1
                                                            low = mid + 1
                                                        # If the element at the mid index is greater than the target
                                                        else:
                                                            # Move the high pointer to mid - 1
                                                            high = mid - 1

                                                    # If the target is not found in the array, return -1
                                                    return -1

                                                # Function to create a data structure of a specified size and datatype
                                                def create_data_structure(size, datatype):
                                                    # Initialize an empty list for the data structure
                                                    data_structure = []

                                                    # For each index in the range of the specified size
                                                    for i in range(size):
                                                        while True:
                                                            try:
                                                                # If the datatype is 'int'
                                                                if datatype == "int":
                                                                    # Prompt the user to enter an integer and store it in 'data'
                                                                    data = int(input("Enter an integer: "))
                                                                # If the datatype is 'str'
                                                                elif datatype == "str":
                                                                    # Prompt the user to enter a string and store it in 'data'
                                                                    data = input("Enter a string: ")
                                                                else:
                                                                    # If the datatype is neither 'int' nor 'str', raise a ValueError with an appropriate message
                                                                    raise ValueError(
                                                                        "Invalid datatype! Only 'int' or 'str' allowed.")

                                                                # Append 'data' to 'data_structure'
                                                                data_structure.append(data)
                                                                break

                                                            except ValueError:
                                                                print(
                                                                    "Value error occurred! Please enter a valid input.")

                                                    # Return 'data_structure'
                                                    return data_structure

                                                def main():
                                                    try:
                                                        size = int(input("Enter the size of the data structure: "))
                                                        datatype = input("Choose the datatype (int/str): ")

                                                        data_structure = create_data_structure(size, datatype)

                                                        if datatype == "int":
                                                            data_structure.sort()  # Binary search requires a sorted list

                                                        target = None
                                                        while True:
                                                            try:
                                                                if datatype == "int":
                                                                    target = int(input("Enter the element to search: "))
                                                                elif datatype == "str":
                                                                    target = input("Enter the string to search: ")
                                                                else:
                                                                    raise ValueError(
                                                                        "Invalid datatype! Only 'int' or 'str' allowed.")
                                                                break
                                                            except ValueError:
                                                                print(
                                                                    "Value error occurred! Please enter a valid input.")

                                                        index = binary_search(data_structure, target)

                                                        if index != -1:
                                                            print(f"Element '{target}' found at index {index}.")
                                                            binary()
                                                        else:
                                                            print(f"Element '{target}' not found.")
                                                            binary()

                                                    except ValueError:
                                                        print("Value error occurred! Please enter a valid input.")
                                                        binary()
                                                if __name__ == "__main__":
                                                    main()
                                            else:
                                                print("invalid input!!")
                                                binary()
                                        binary()

                                    elif type == "3":
                                        def hash():
                                            hash_input = input("Choose an option:\n\t 1: Definition\n\t 2:Algorithm And Implementation\n\t 0 : Back\n Your Choice:")
                                            if hash_input=="0":
                                                all_types()
                                            elif hash_input=="1":
                                                print("Hashing:\n Hashing is a technique that uses a hash function to map keys to specific positions in a data structure called a hash table.\n Searching in a hash table involves calculating the hash value of the key and then accessing the corresponding position in the table.")
                                                hash()
                                            elif hash_input == "2":
                                                print(
                                                  """  
                                                        Algorithm:
                                                        
                                                        start
                                                        1. Initialize an empty dictionary to store the key-value pairs.
                                                        2. Prompt the user to enter the number of elements they want to store in the dictionary.
                                                        3. Iterate over the range of the entered number of elements.
                                                        - Inside the loop, prompt the user to enter a key-value pair.
                                                        - Store the key-value pair in the dictionary.
                                                        4. Prompt the user to enter a key they want to search for.
                                                        5. Check if the entered key exists in the dictionary using the in operator.
                                                        - If the key exists, print the corresponding value.
                                                        - If the key does not exist, print a message indicating that the key was not found.
                                                        End"""
                                                )
                                                print("Implementation of Hash Search")

                                                # Function to perform hash search
                                                def hash_search(data_structure, num_elements, search_element):
                                                    print("Performing hash search...")

                                                    # Loop through each element in the data structure
                                                    for i in range(num_elements):
                                                        # If the current element matches the search element
                                                        if data_structure[i] == search_element:
                                                            print(
                                                                f"Checking index {i + 1}: Match found! Element '{search_element}' found at index {i + 1}.")
                                                            return

                                                        print(f"Checking index {i + 1}: No match.")

                                                    print(
                                                        f"The element '{search_element}' is not found in the data structure.")

                                                # Get the size of the data structure from the user
                                                size = int(input("Enter the size of the data structure: "))
                                                # Get the data type of the elements from the user
                                                data_type = input("Enter the data type (int/str): ")

                                                data_structure = []

                                                # Get each element of the data structure from the user
                                                for i in range(size):
                                                    element = input(f"Enter the element at index {i + 1}: ")
                                                    if data_type == 'int':
                                                        # Convert the element to integer if the data type is 'int'
                                                        element = int(element)
                                                    # Add the element to the data structure
                                                    data_structure.append(element)

                                                # Get the search element from the user
                                                search_element = input("Enter the element to search: ")
                                                if data_type == 'int':
                                                    # Convert the search element to integer if the data type is 'int'
                                                    search_element = int(search_element)

                                                # Call the hash_search function with the user's inputs
                                                hash_search(data_structure, size, search_element)

                                                hash()
                                            else:
                                                print("Invalid input!!")
                                                hash()
                                        hash()

                                    elif type == "4":
                                        def tree_base():
                                            tree_input = input("Choose an option:\n\t 1: Definition\n\t 2:Algorithm and Implementation\n\t 0:Back \n Your Choice: ")
                                            if tree_input=="0":
                                               all_types()
                                            elif tree_input=="1":
                                                print("ee-based Searching:\n Various tree data structures like Binary Search Trees (BST), AVL Trees, Red-Black Trees, etc.\n, provide efficient searching capabilities. These trees are organized in a specific way that allows for faster searching by traversing the tree based on certain conditions.")
                                                tree_base()
                                            elif tree_input == "2":
                                                print(
                                                    """To implement a tree-based searching algorithm in Python, we need to define the tree structure and the searching algorithm. Let's start by defining the tree structure
                                                    In a tree structure, each node can have multiple child nodes. We can represent a tree using classes and objects. Each node in the tree will be an object with pointers to its child nodes."""
                                                        )
                                                print("Implementation of Tree Base Search")

                                                # Node class represents the nodes in the tree
                                                class Node:
                                                    # Each node has a value, and a left and right child
                                                    def __init__(self, value=None):
                                                        self.value = value
                                                        self.left_child = None
                                                        self.right_child = None

                                                # Tree class represents the binary search tree
                                                class Tree:
                                                    # The tree has a root node
                                                    def __init__(self):
                                                        self.root = None

                                                    # Method to insert a new value into the tree
                                                    def insert(self, value):
                                                        # If the tree is empty, create a new root node
                                                        if self.root is None:
                                                            self.root = Node(value)
                                                        else:
                                                            # Otherwise, use the helper method _insert to add the new value
                                                            self._insert(value, self.root)

                                                    # Helper method for insert, which adds a new value to the tree
                                                    def _insert(self, value, current_node):
                                                        # If the new value is less than the current node's value
                                                        if value < current_node.value:
                                                            # If there's no left child, add the new value here
                                                            if current_node.left_child is None:
                                                                current_node.left_child = Node(value)
                                                            else:
                                                                # Otherwise, repeat the process for the left child
                                                                self._insert(value, current_node.left_child)
                                                        # If the new value is greater than the current node's value
                                                        elif value > current_node.value:
                                                            # If there's no right child, add the new value here
                                                            if current_node.right_child is None:
                                                                current_node.right_child = Node(value)
                                                            else:
                                                                # Otherwise, repeat the process for the right child
                                                                self._insert(value, current_node.right_child)
                                                        else:
                                                            # If the new value is already in the tree, don't add it again
                                                            print("Value already exists in tree")

                                                    # Method to search for a value in the tree
                                                    def search(self, value):
                                                        # If the tree isn't empty, use the helper method _search to find the value
                                                        if self.root is not None:
                                                            return self._search(value, self.root)
                                                        else:
                                                            return False

                                                    # Helper method for search, which finds a value in the tree
                                                    def _search(self, value, current_node):
                                                        # If we've found the value, return True
                                                        if value == current_node.value:
                                                            return True
                                                        # If the desired value is less than the current node's and there's a left child,
                                                        elif value < current_node.value and current_node.left_child is not None:
                                                            # Repeat the process for the left child
                                                            return self._search(value, current_node.left_child)
                                                        # If the desired value is greater than the current node's and there's a right child,
                                                        elif value > current_node.value and current_node.right_child is not None:
                                                            # Repeat the process for the right child
                                                            return self._search(value, current_node.right_child)
                                                        else:
                                                            return False  # The desired value isn't in the tree.

                                                def create_array():
                                                    while True:
                                                        try:
                                                            size = int(input("Enter the size of the array: "))
                                                            break
                                                        except ValueError:
                                                            print("Invalid input. Please enter an integer.")

                                                    array_type = input(
                                                        "Enter the type of elements in the array (int/str): ")

                                                    if array_type == "int":
                                                        array = []
                                                        for i in range(size):
                                                            while True:
                                                                try:
                                                                    element = int(input(f"Enter element {i + 1}: "))
                                                                    array.append(element)
                                                                    break
                                                                except ValueError:
                                                                    print("Invalid input. Please enter an integer.")
                                                    elif array_type == "str":
                                                        array = []
                                                        for i in range(size):
                                                            element = input(f"Enter element {i + 1}: ")
                                                            array.append(element)
                                                    else:
                                                        print("Invalid input. Please enter 'int' or 'str'.")

                                                    return array

                                                def main():
                                                    array = create_array()
                                                    tree = Tree()
                                                    for element in array:
                                                        tree.insert(element)

                                                    while True:
                                                        search_element = input("Enter the element to search: ")
                                                        if str(array[0]).isdigit():
                                                            try:
                                                                search_element = int(search_element)
                                                            except ValueError:
                                                                print("Invalid input. Please enter an integer.")
                                                                continue

                                                        found = tree.search(search_element)
                                                        if found:
                                                            print(f"{search_element} found in the tree.")
                                                            tree_base() 
                                                        else:
                                                            print(f"{search_element} not found in the tree.")
                                                            tree_base()

                                                if __name__ == "__main__":
                                                    main()
                                            else:
                                                print("Invalid Input!!")
                                                tree_base()
                                        tree_base()
                                    else:
                                        print("Invalid input!!")
                                        search()
                                types()
                            all_types()
                        else:
                            print("Invalid Input!!")
                            search()
                    search()
                else:
                    print("Invalid Inp0ut!!")
                    Categories()
            Categories()
        else:
            print("Invalid input!!")
            algorithm()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++End of Algorithms+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def Arrays():
        a_choose =input("Choose one option From array Types:\n 0: Main Menu\n 1: List\n 2: Dictionary\n 3: Tuple\n 4: Set \n Your Choice: ")

        def My_list():
            def operations():
                list_type = input("Do you want to create a list of integers or strings?\n type i for integers s for strings  ")# Ask user for the type of list to create

                my_list = []# Initialize an empty list
                if list_type.lower() == "i":# Check user input and create the list accordingly
                    while True:# Ask user to enter integers and append them to the list
                        num = input("Enter an integer to add to the list (press '#' to stop): ")
                        if num == '#':
                            break
                        else:
                            try:# Check if the num is an integer and convert it if necessary
                                num = int(num)
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                continue
                            my_list.append(int(num))
                    print("List: ", my_list)
                elif list_type.lower() == "s":
                    while True:# Ask user to enter strings and append them to the list
                        string = input("Enter a string to add to the list (press '0' to stop): ")
                        if string == '0':
                            break
                        else:
                            my_list.append(string)
                    print("List: ", my_list)
                else:
                    print("Invalid input. Please enter either 'i' or 's'.")

                while True:# Ask user for list operations to perform
                    operation = input("Choose one option From list operations:\n1: append\n 2: pop\n 3: sort \n  4: index\n Your Choice: (press '0' to go Back): ")
                    if operation == '0':
                        Arrays()
                    elif operation == "1":
                        input_type=input("Enter i to append integer s to append string ")# Ask user for value to append and append it to the list
                        if input_type=="i":
                            value = input("Enter a value to append: ")
                            try:# Check if the num is an integer and convert it if necessary
                                value = int(value)
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                continue
                            my_list.append(value)
                            print("List after appending:", my_list)
                        elif input_type=="s":
                            value = input("Enter a value to append: ")
                            my_list.append(value)
                            print("List after appending:", my_list)
                        else:
                            print("invalid input")
                    elif operation == "2":
                        if len(my_list) > 0:# Pop the last element from the list
                            popped_value = my_list.pop()
                            print("Popped value:", popped_value)
                            print("List after popping:", my_list)
                        else:
                            print("List is empty. Cannot perform pop operation.")
                    elif operation == "3":
                        # Sort the list in ascending order
                        my_list.sort()
                        print("List after sorting:", my_list)
                    elif operation == "4":
                        Type=input("Enter i for integer list or s for list of strings ")
                        if Type=="i":
                            value = input("Enter a value to find its index: ")# Ask user for value to find index of and find its index in the list
                            try:# Check if the num is an integer and convert it if necessary
                                value = int(value)
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                continue
                            if value in my_list:
                                index = my_list.index(value)
                                print("Index of", value, "in the list:", index)
                            else:
                                print(value, "not found in the list.")
                        elif Type=="s":
                            value = input("Enter a value to find its index: ")
                            if value in my_list:
                                index = my_list.index(value)
                                print("Index of", value, "in the list:", index)
                            else:
                                print(value, "not found in the list.")
                        else:
                            print("Invalid input")
                    else:
                        print("Invalid operation. Please enter the correct number for the operations")
                
            list_choose = input("Choose one option form list categories:\n 0: Back \n1: Definition, \n2: how to create,\n3: operations\n Your Choice:")
            if list_choose == "0":
                Arrays()
            elif list_choose == "1":
                print("List:\n Lists are a data structure in puthon used to store multiple items in a single variable.")
                My_list()
            elif list_choose == "2":
                print('How To create a list:\n Lists are created using square brackets:\n lets create a list:')
                inputType=input("enter i for integer or s for string: ")
                if inputType=="i":
                    my_list = list(input("Enter items separated by comma:").split(","))
                    my_list=[eval(i) for i in my_list]
                    print("list:", my_list)
                    My_list()
                elif inputType=="s":
                    my_list = list(input("Enter items separated by comma:").split(','))
                    print("list:", my_list)
                    My_list()
                else:
                    print("invalid Input")
                    My_list()
                    
                My_list()
            elif list_choose == "3":
                operations()
            else:
                print("Invalid input, sorry!!!")
                My_list()

        def my_dic():
            def operations():
                dict_type = input("Do you want to create a dictionary of integers, strings, or both? \n type i for integrs, s for strings or b for Both ")# Ask user for the type of dictionary to create

                my_dict = {}# Initialize an empty dictionary

                if dict_type.lower() == "i":# Check user input and create the dictionary accordingly
                    while True:# Ask user to enter key-value pairs and add them to the dictionary
                        key = input("Enter an integer key to add to the dictionary (press '#' to stop): ")
                        if key == '#':
                            break
                        else:
                            try:
                                key = int(key)
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                continue
                            value = input("Enter a value for the key: ")
                            try:# Check if the num is an integer and convert it if necessary
                                value= int(value)
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                continue
                            my_dict[int(key)] = value
                    print("Dictionary:",my_dict)
                elif dict_type.lower() == "s":
                    while True:# Ask user to enter key-value pairs and add them to the dictionary
                        key = input("Enter a string key to add to the dictionary (press '#' to stop): ")
                        if key == '#':
                            break
                        else:
                            value = input("Enter a value for the key: ")
                            my_dict[key] = value
                    print("Dictionary:",my_dict)
                elif dict_type.lower() == "b":# Ask user to enter key-value pairs and add them to the dictionary
                    while True:
                        key = input("Enter a key to add to the dictionary (press '#' to stop): ")
                        if key == '#':
                            break
                        else:
                            value = input("Enter a value for the key: ")
                            try:# Check if the key is an integer and convert it if necessary
                                key = int(key)
                            except ValueError:
                                pass
                            my_dict[key] = value
                    print("Dictionary:",my_dict)
                else:
                    print("Invalid input. Please enter either 'i', 's', or 'b'.")
                    my_dic()
                    
                while True:# Ask user for dictionary operations to perform
                    operation = input("Choose one option from Dictionary operations:\n 1: update\n 2: Remove \n 3:search \n Your Choice:\n(press '0' to go Back): ")
                    if operation == '0':
                        my_dic()
                    elif operation == "1":
                        key = input("Enter a key to add or update: ")# Ask user for key-value pair to add or update in the dictionary
                        value = input("Enter a value for the key: ")
                        try:# Check if the key is an integer and convert it if necessary
                            key = int(key)
                        except ValueError:
                            pass
                        my_dict[key] = value
                        print("Dictionary after updating:", my_dict)
                    elif operation == "2":
                        key = input("Enter a key to remove: ") # Ask user for key to remove from the dictionary
                        if key in my_dict:
                            popped_value = my_dict.pop(key)
                            print("Popped value:", popped_value)
                            print("Dictionary after popping:", my_dict)
                        else:
                            print(key, "not found in the dictionary.")
                    elif operation == "3":
                        input_type=input("Enter i for integer key or s for string  key ")# Ask user for value to append and append it to the list
                        if input_type=="i":
                            key = input("Enter a key to get the value of: ")# Ask user for key to get value of from the dictionary
                            try:# Check if the num is an integer and convert it if necessary
                                key = int(key)
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                continue
                            value = my_dict.get(int(key))
                            if value is not None:
                                print("Value of", key, "in the dictionary:", value)
                            else:
                                print(key, "not found in the dictionary.")
                        elif input_type=="s":
                            key = input("Enter a key to get the value of: ")# Ask user for key to get value of from the dictionary
                            value = my_dict.get(key)
                            if value is not None:
                                print("Value of", key, "in the dictionary:", value)
                            else:
                                print(key, "not found in the dictionary.")
                        else:
                            print("Invalid input, Enter either i or s")
                        
                    else:
                        print("Invalid operation. Please enter the correct operation.")


            dic_choose = int(input("Choose one option: \n 0:Back \n1: Definition, \n2: how to create,\n 3: operations \n Your Choice: "))    
            if dic_choose == 1:
                print("Dictionary:\nDictionaries are used to store data values in key:value pairs.\n A dictionary is a collection which is ordered*, changeable and do not allow duplicates." )
                my_dic()
            elif dic_choose == 2:
                print('How to create Dictionaries:\nDictionary items are presented in key:value pairs, and can be referred to by using the key name.\n Lets Create a Dictioary.')
                dict_type = input("Do you want to create a dictionary of integers, strings, or both? \n type i for integrs, s for strings or b for Both ")# Ask user for the type of dictionary to create

                my_dict = {}# Initialize an empty dictionary

                if dict_type.lower() == "i":# Check user input and create the dictionary accordingly
                    while True:# Ask user to enter key-value pairs and add them to the dictionary
                        key = input("Enter an integer key to add to the dictionary (press '#' to stop): ")
                        if key == '#':
                            break
                        else:
                            try:# Check if the num is an integer and convert it if necessary
                                key = int(key)
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                continue
                            value = input("Enter a value for the key: ")
                            try:# Check if the num is an integer and convert it if necessary
                                value = int(value)
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                continue
                            my_dict[int(key)] = value
                    print("Dictionary:",my_dict)
                    my_dic()
                elif dict_type.lower() == "s":
                    while True:# Ask user to enter key-value pairs and add them to the dictionary
                        key = input("Enter a string key to add to the dictionary (press '#' to stop): ")
                        if key == '#':
                            break
                        else:
                            value = input("Enter a value for the key: ")
                            my_dict[key] = value
                    print("Dictionary:",my_dict)
                    my_dic()
                elif dict_type.lower() == "b":# Ask user to enter key-value pairs and add them to the dictionary
                    while True:
                        key = input("Enter a key to add to the dictionary (press '#' to stop): ")
                        if key == '#':
                            break
                        else:
                            value = input("Enter a value for the key: ")
                            try:# Check if the key is an integer and convert it if necessary
                                key = int(key)
                            except ValueError:
                                pass
                            my_dict[key] = value
                    print("Dictionary:",my_dict)
                    my_dic()
                else:
                    print("Invalid input. Please enter either 'i', 's', or 'b'.")
                    my_dic()
            elif dic_choose == 3:
                operations()
                operations()
            elif dic_choose == 0:
                Arrays()
            else:
                data_structure()

        def my_tup():
            def operations():
                tuple_type = input("Do you want to create a tuple of integers or strings?\n type i for integers or s for strings ")# Ask user for the type of tuple to create

                my_tuple = ()# Initialize an empty tuple

                if tuple_type.lower() == "i":# Check user input and create the tuple accordingly
                    while True:# Ask user to enter integers and add them to the tuple
                        num = input("Enter an integer to add to the tuple (press '#' to stop): ")
                        if num == '#':
                            break
                        else:
                            my_tuple += (int(num),)
                    print("Tuple:",my_tuple)
                elif tuple_type.lower() == "s":
                    while True:# Ask user to enter strings and add them to the tuple
                        string = input("Enter a string to add to the tuple (press '#' to stop): ")
                        if string == '#':
                            break
                        else:
                            my_tuple += (string,)
                    print("Tuple:",my_tuple)
                else:
                    print("Invalid input. Please enter either 'i' or 's'.")

                while True:# Ask user for tuple operations to perform
                    operation = input("Choose one option:\n 1: count\n 2: Slicing(access)\n 3: update\n 4:index\n Your Choice: (press '0' to go Back): ")
                    if operation == '0':
                        my_tup()
                    elif operation == "1":
                        input_type=input("Enter i for tuple of integers or s for tuple of strings: ")
                        if input_type=="i":
                            element = int(input("Enter an element to count: "))# Ask user for element to count in the tuple
                            count = my_tuple.count(element)
                            print("Count of", element, "in the tuple:", count)
                            try:# Check if the index is an integer and convert it if necessary
                                element = int(element)
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                continue
                        elif input_type=="s":
                            element = input("Enter an element to count: ")# Ask user for element to count in the tuple
                            count = my_tuple.count(element)
                            print("Count of", element, "in the tuple:", count)
                        else:
                            print("Invalid input, Enter either i or s.")
                            
                    elif operation == "2":
                        start = input("Enter the start index for slicing: ")# Ask user for start and end indices for slicing the tuple
                        end = input("Enter the end index for slicing: ")
                        try:# Check if the indices are integers and convert them if necessary
                            start = int(start)
                            end = int(end)
                        except ValueError:
                            print("Invalid indices. Please enter integers.")
                            continue
                        sliced_tuple = my_tuple[start:end]
                        print("Sliced tuple:", sliced_tuple)
                    elif operation == "3":
                        index = input("Enter an index to update: ")# Ask user for index and value to update in the tuple
                        value = input("Enter a value for the index: ")
                        try:# Check if the index is an integer and convert it if necessary
                            index = int(index)
                        except ValueError:
                            print("Invalid index. Please enter an integer.")
                            continue
                        if index < 0 or index >= len(my_tuple):# Check if the index is within the range of the tuple
                            print("Index out of range.")
                            continue
                        my_list = list(my_tuple)# Convert the tuple to a list to update the value
                        my_list[index] = value
                        my_tuple = tuple(my_list)
                        print("Tuple after updating:", my_tuple)
                    elif operation == "4":
                        input_type=input("Enter i tuple of integers and s for strings: ")
                        if input_type=="i":
                            element = int(input("Enter an element to find the index of: "))# Ask user for element to find the index of in the tuple
                            try:
                                index = my_tuple.index(element)
                                print("Index of", element, "in the tuple:", index)
                            except ValueError:
                                print(element, "not found in the tuple.")
                        elif input_type=="s":
                            element = input("Enter an element to find the index of: ")# Ask user for element to find the index of in the tuple
                            try:
                                index = my_tuple.index(element)
                                print("Index of", element, "in the tuple:", index)
                            except ValueError:
                                print(element, "not found in the tuple.")
                        else:
                            print("Invalid input, Enter either i or s")
                    else:
                        print("Invalid operation. Please enter the correct operation.")

            tuple_choose = int(input("Choose one option: \n1: Definition, \n2: how to create,\n 3: operations \n 0:Back \n Your Choice:"))
            if tuple_choose == 1:
                print("Tuples:\nTuples are used to store multiple items in a single variable.")
                my_tup()
            elif tuple_choose == 2:
                print('How to create:\nTuples are written with round brackets:\n Lets create a tuple:')
                tuple_type = input("Do you want to create a tuple of integers or strings?\n type i for integers or s for strings ")# Ask user for the type of tuple to create

                my_tuple = ()# Initialize an empty tuple

                if tuple_type.lower() == "i":# Check user input and create the tuple accordingly
                    while True:# Ask user to enter integers and add them to the tuple
                        num = input("Enter an integer to add to the tuple (press '#' to stop): ")
                        if num == '#':
                            break
                        else:
                            my_tuple += (int(num),)
                    print("Tuple:",my_tuple)
                    my_tup()
                elif tuple_type.lower() == "s":
                    while True:# Ask user to enter strings and add them to the tuple
                        string = input("Enter a string to add to the tuple (press '#' to stop): ")
                        if string == '#':
                            break
                        else:
                            my_tuple += (string,)
                    print("Tuple:",my_tuple)
                    my_tup()
                else:
                    print("Invalid input. Please enter either 'i' or 's'.")
                    my_tup()

            elif tuple_choose == 3:
                operations()
            elif tuple_choose==0:
                Arrays()  
            else:
                print("Invalid input, enter the correct number")
                data_structure()

        def My_set():
            def operations():
                set_type = input("Do you want to create a set of integers or strings?\n type i for integers or s for stirngs ")# Ask user for the type of set to create

                my_set = set()# Initialize an empty set

                if set_type.lower() == "i":# Check user input and create the set accordingly
                    while True:# Ask user to enter integers and add them to the set
                        num = input("Enter an integer to add to the set (press '#' to stop): ")
                        if num == '#':
                            break
                        else:
                            try:# Check if the num is an integer and convert it if necessary
                                num = int(num)
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                continue
                            my_set.add(int(num))
                    print("Set: ",my_set)
                        
                elif set_type.lower() == "s":
                    while True:# Ask user to enter strings and add them to the set
                        string = input("Enter a string to add to the set (press '#' to stop): ")
                        if string == '#':
                            break
                        else:
                            my_set.add(string)
                    print("Set:", my_set)       
                else:
                    print("Invalid input. Please enter either 'i' or 's'.")

                while True:# Ask user for set operations to perform
                    operation = input("Choose one option:\n 1: add\n 2: remove\n 3: check through  in \n Your choice: (press '0' to go back): ")
                    if operation == '0':
                        My_set()
                    elif operation == "1":
                        input_type=input("Enter i to add integer or s to add string ")
                        if input_type=="i":
                            element = input("Enter an element to add: ")# Ask user for element to add to the set
                            try:
                                element= int(element)
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                continue
                            my_set.add(element)
                            print(element, "added to the set.")
                            print("set after Adding:",my_set)
                        elif input_type=="s":
                            element = input("Enter an element to add: ")# Ask user for element to add to the set
                            my_set.add(element)
                            print(element, "added to the set.")
                            print("set after Adding:",my_set)
                        else:
                            print("Invalid input, Enter either i or s.")
                            
                    elif operation == "2":
                        input_type=input("Enter i for set of integers or s for set of strings ")
                        if input_type=="i":
                            element = input("Enter an element to remove: ")# Ask user for element to remove from the set
                            try:
                                element= int(element)
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                continue
                            if element in my_set:
                                my_set.remove(element)
                                print(element, "removed from the set.")
                                print("set after removing: ", my_set)
                            else:
                                print(element, "not found in the set.")
                        elif input_type=="s":
                            element = input("Enter an element to remove: ")# Ask user for element to remove from the set
                            if element in my_set:
                                my_set.remove(element)
                                print(element, "removed from the set.")
                                print("set after removing: ", my_set)
                            else:
                                print(element, "not found in the set.")
                        else:
                            print("Invalid input, Enter Either i or s.")
                    elif operation == "3":
                        input_type=input("Enter i for set of integers or s for set of strings ")
                        if input_type=="i":
                            element = input("Enter an element to check: ")# Ask user for element to check in the set
                            try:
                                element= int(element)
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                continue
                            if element in my_set:
                                print(element, "is in the set.")
                            else:
                                print(element, "is not in the set.")
                        elif input_type=="s":
                            element = input("Enter an element to check: ")# Ask user for element to check in the set
                            if element in my_set:
                                print(element, "is in the set.")
                            else:
                                print(element, "is not in the set.")
                        else:
                            print("Invalid input, Enter either i or s.")   
                    else:
                        print("Invalid operation. Please enter the correct operation number.")

            set_choose = input("Choose one option: \n 0: Back \n1: Definition, \n2: how to create,\n 3: operations \n Your Choice:")
            if set_choose == "1":
                print("Sets:\nSets are used to store multiple items in a single variable.")
                My_set()
            elif set_choose == "2":
                print('How to Create sets:\nSets are written with curly brackets:\n Lets create a set:')
                set_type = input("Do you want to create a set of integers or strings?\n type i for integers or s for stirngs ")# Ask user for the type of set to create

                my_set = set()# Initialize an empty set

                if set_type.lower() == "i":# Check user input and create the set accordingly
                    while True:# Ask user to enter integers and add them to the set
                        num = input("Enter an integer to add to the set (press '#' to stop): ")
                        if num == '#':
                            break
                        else:
                            try:# Check if the num is an integer and convert it if necessary
                                num = int(num)
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                                continue
                            my_set.add(int(num))
                    print("Set:", my_set)
                    My_set()     
                elif set_type.lower() == "s":
                    while True:# Ask user to enter strings and add them to the set
                        string = input("Enter a string to add to the set (press '#' to stop): ")
                        if string == '#':
                            break
                        else:
                            my_set.add(string)
                    print("Set:", my_set)
                    My_set()
                    
                else:
                    print("Invalid input. Please enter either 'i' or 's'.")
                    My_set()

            elif set_choose =="3":
                operations()
                operations()
            elif set_choose == "0":
                My_set()
            else:
                data_structure()

        if a_choose == "1":
            My_list()
        elif a_choose == "2":
            my_dic()
        elif a_choose == "3":
            my_tup()
        elif a_choose == "4":
            My_set()
        elif a_choose== "0":
            data_structure()
        else:
            print("Invalid Input sorry!!")
            Arrays()
            
#++++++++++++++++++++++++++++++++++++++++++++++End of Arrays++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def Stack():
            def operations():
                # Define a class for a stack data structure
                class MyStack:
                    # Initialize the stack with a given size
                    def __init__(self, size):
                        self.size = size
                        self.stack = []  # The stack is initially empty
                        print("stack: ", self.stack)

                    # Method to add an item to the stack
                    def push(self, item):
                        # Check if the stack is full before adding the item
                        if len(self.stack) < self.size:
                            self.stack.append(item)  # Add the item to the stack
                        else:
                            print("Stack is full. Cannot push item.")  # Print a message if the stack is full
                        print("stack: ", self.stack)

                    # Method to remove an item from the stack
                    def pop(self):
                        # Check if the stack is empty before removing an item
                        if not self.is_empty():
                            item = self.stack.pop()  # Remove the last item added to the stack
                            print(f"Item Popped from the stack: {item}")
                            return item  # Return the removed item
                        else:
                            print(
                                "Stack is empty. Cannot perform pop operation.")  # Print a message if the stack is empty

                    # Method to get the last item added to the stack without removing it
                    def peek(self):
                        # Check if the stack is empty before getting an item
                        if not self.is_empty():
                            top_item = self.stack[-1]  # Get the last item added to the stack
                            print(f"Top item in stack: {top_item}")
                            return top_item  # Return the last item added
                        else:
                            print(
                                "Stack is empty. Cannot perform peek operation.")  # Print a message if the stack is empty

                    # Method to check if the stack is empty
                    def is_empty(self):
                        return len(self.stack) == 0  # Return True if the stack is empty, False otherwise

                    # Method to check if the stack is full
                    def is_full(self):
                        return len(self.stack) == self.size  # Return True if the stack is full, False otherwise

                def operations():
                    try:
                        stack_size = int(input("Enter the size of the stack: "))
                    except ValueError:
                        print("Invalid input. Size of stack must be an integer.")
                        operations()
                    
                    stack_type = input("Enter 'i' for stack of integers or 's' for stack of strings: ")
                    if stack_type not in ['i', 's']:
                        print("Invalid input. Only 'i' and 's' are allowed.")
                        operations()
                    
                    stack = MyStack(stack_size)
                    for i in range(1, stack_size+1):
                        item = input(f"Enter item {i}: ")
                        try:
                            if stack_type == 'i':
                                stack.push(int(item))
                            else:
                                stack.push(item)
                        except ValueError:
                            print("Invalid input. please enter  integers.")
                                
                    
                    print("Stack operations:")
                    while True:
                        print("\n1. Push")
                        print("2. Pop")
                        print("3. Peek")
                        print("4. Is Empty?")
                        print("5. Is Full?")
                        print("0. Back")
                        
                        choice = input("Enter your choice (0-5): ")
                        
                        if choice == '1':
                            item = input("Enter item to push: ")
                            try:
                                if stack_type == 'i':
                                    stack.push(int(item))
                                else:
                                    stack.push(item)
                            except ValueError:
                                print("Invalid input. please enter  integers.")
                        elif choice == '2':
                            stack.pop()
                        elif choice == '3':
                            stack.peek()
                        elif choice == '4':
                            if stack.is_empty():
                                print("Stack is empty.")
                            else:
                                print("Stack is not empty.")
                        elif choice == '5':
                            if stack.is_full():
                                print("Stack is full.")
                            else:
                                print("Stack is not full.")
                        elif choice == '0':
                            Stack()
                        else:
                            print("Invalid choice. Please choose a number from 0 to 5.")

                operations()

            stack_choose = input("Choose one option:\n 1: Definations\n 2: Applications \n 3: How To Create and Operations\n 0: MainMenu \n Your Choice\n: ")

            if stack_choose == "1":
                print("Stack:\nStack is a linear data structore that follows the last-in-first-out(LIFO) principle, which"
                        + " the last element added is the first one to be removed.")
                Stack()
                
            elif stack_choose == "2":
                print(
                        """
                Applications of stack:
                    1: computer run time memory invironments.
                    2: store local data.
                    3: Internet web browsers store the addresses of recently visited sites on a stack.
                    4: Undo mechanism that cancels recent edition.
                    5: Paste mechanism.
                    6: The “back” button on a web browser.
                    """
                    )
                Stack()
            elif stack_choose == "3":
                print("""
            How To create a Stack in Python:
1. Define a class called Stack.
2. In the __init__ method of the Stack class, initialize the size of the stack and an empty list to hold the values of the stack.
3. Define the push method that takes a value as an argument and appends it to the end of the list if the length of the list is less than the size of the stack.
4. Define the pop method that removes and returns the last element of the list if the list is not empty.
5. Define the peek method that returns the last element of the list without removing it if the list is not empty.
6. Define the is_empty method that returns True if the list is empty and False otherwise.
7. Define the is_full method that returns True if the length of the list is equal to the size of the stack and False otherwise.
8. Create an instance of the Stack class with a specified size.
9. Use the push method to add values to the stack.
10. Use other methods (pop, peek, is_empty, is_full) to manipulate and check the stack as needed.

""")
                operations()
               
            elif stack_choose == "0":
                data_structure()
                
#+++++++++++++++++++++++++++++++++++++++End of Stack Data Structure+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def Queu():
        queue_choose =input("Choose one option:\n 1: Definition\n 2: How to create\n3: Types\n 4: Operations\n 5: main menu\nYour Choice: ")
        
        if queue_choose == "1":
            print(
                """Queue: 
        A queue is a data structure used to implement First In-First-Out (FIFO) strategy.
        Conceptually, we add elements to the end of the queue and take away elements from its front."""
            )
            Queu()
        elif queue_choose == "2":
            print(
                """To create a queue data structure, follow these steps:

1. Define the size of the queue: Decide on the maximum number of elements that the queue can hold.
2. Create an array: Create an array of the defined size to hold the elements in the queue.
3. Define two pointers: Define two pointers, front and rear, to keep track of the first and last elements in the queue.
4. Initialize the pointers: Initialize both pointers to -1, indicating that the queue is empty.
5. Implement enqueue operation: To add an element to the queue, increment the rear pointer and insert the element at the rear position.
6. Implement dequeue operation: To remove an element from the queue, increment the front pointer and return the element at the front position.
7. Implement isFull operation: Check if the rear pointer is equal to the size of the array minus one. If it is, then the queue is full.
8. Implement isEmpty operation: Check if both front and rear pointers are equal to -1. If they are, then the queue is empty.
9. Implement peek operation: Return the element at the front position without removing it from the queue.
10. Use the queue: Use the implemented operations to add, remove, and access elements in the queue as required."""
            )
            Queu()
        elif queue_choose == "3":
            def Queue_types():
                print("queue has three types")
                queue_types = input("Select one option:\n 0: Back\n 1:circular queue \n 2: double_end queue(dqueue)\n3: priority\n Which One:")
                if queue_types == "0":
                    Queu()
                elif queue_types == "1":
                    def Circular_Queu():
                        circular_queue = input("Select one option:\n 0:Back \n 1:Definition \n 2: How to create and implementation \n Which One:")
                        if circular_queue == "0":
                            Queue_types()
                        elif circular_queue == "1":
                            print(
"""Circular queue:
    Circular queue is a type of linear queue where the last
    position is connected back to the first position.
    In simple linear queue, when the queue was being full and
    we deleted some items, we still received a message at the
    time of insertion that the queue is full.
    This issue has been resolved in circular queue."""
                            )
                            Circular_Queu()
                        elif circular_queue == "2":
                            print(
                                """how to create circular queue: 
        1. start
        2. Initialize the queue with a fixed size, front, rear, and count.
        3. Implement functions for enqueue, dequeue, is_empty, is_full, display, and get_size.
        4. To enqueue an element, check if the queue is full. If not, add the element to the rear and increment the rear and count.
        5. To dequeue an element, check if the queue is empty. If not, remove the element from the front, increment the front, and decrement the count.
        6. Implement the is_empty function to check if the queue is empty by checking the count.
        7. Implement the is_full function to check if the queue is full by comparing the count with the size of the queue.
        8. Implement the display function to print all the elements in the queue.
        9. end"""
                            )
                            print("Code And implementation of Circular Queue:")

                            # Define a class for a circular queue data structure
                            class CircularQueue:
                                # Initialize the queue with a given size
                                def __init__(self, size):
                                    self.size = size
                                    self.queue = [None] * size  # The queue is initially empty
                                    self.front = self.rear = -1  # The front and rear pointers are initially set to -1

                                # Method to check if the queue is empty
                                def is_empty(self):
                                    return self.front == -1

                                # Method to check if the queue is full
                                def is_full(self):
                                    return (self.rear + 1) % self.size == self.front

                                # Method to add an element to the queue
                                def enqueue(self, element):
                                    if self.is_full():
                                        print("Circular queue is full.")
                                    elif self.is_empty():
                                        self.front = self.rear = 0
                                        self.queue[self.rear] = element
                                    else:
                                        self.rear = (self.rear + 1) % self.size
                                        self.queue[self.rear] = element

                                # Method to remove an element from the queue
                                def dequeue(self):
                                    if self.is_empty():
                                        print("Circular queue is empty.")
                                    elif self.front == self.rear:
                                        self.queue[self.front] = None
                                        self.front = self.rear = -1
                                    else:
                                        self.queue[self.front] = None
                                        self.front = (self.front + 1) % self.size

                                # Method to display the elements in the queue
                                def display(self):
                                    if self.is_empty():
                                        print("Circular queue is empty.")
                                    else:
                                        output = "Circular Queue Content: "
                                        i = self.front
                                        while True:
                                            output += str(self.queue[i]) + " "
                                            if i == self.rear:
                                                break
                                            i = (i + 1) % self.size
                                        print(output)

                            # Function to create a new circular queue based on user input
                            def create_queue():
                                while True:
                                    choice = input("Enter 'i' for integer queue or 's' for string queue: ")
                                    if choice == "i":
                                        return CircularQueue(int(input("Enter the size of the queue: ")))
                                    elif choice == "s":
                                        return CircularQueue(int(input("Enter the size of the queue: ")))
                                    else:
                                        print("Invalid choice. Please try again.")

                            def main():
                                queue = create_queue()
                                option = None

                                while option != "4":
                                    print("\n----- Options -----")
                                    print("1. Enqueue")
                                    print("2. Dequeue")
                                    print("3. Display")
                                    print("0. Back")
                                    
                                    option = input("Enter your choice (1-4): ")

                                    if option == "1":
                                        element = input("Enter the element to enqueue: ")
                                        try:
                                            if isinstance(queue.queue[0], int):
                                                queue.enqueue(int(element))
                                            else:
                                                queue.enqueue(element)
                                        except ValueError:  # Handle value error when string is provided instead of int
                                            print("Invalid element. Expected integer.")

                                    elif option == "2":
                                        queue.dequeue()

                                    elif option == "3":
                                        queue.display()

                                    elif option == "0":
                                        Circular_Queu()

                                    else:
                                        print("Invalid choice. Please try again.")


                            if __name__ == "__main__":
                                main()
                            Queue_types()
                        else:
                            print("Invalid input, Enter from 0 to 2.")
                            Circular_Queu()
                    Circular_Queu()

                elif queue_types == "2":
                    def Double_End_Queue():
                        double_end_queue = input("Choose one option:\n 0:Back\n 1:Definition \n 2: How to create and implementation \n Your Choice:")
                        if double_end_queue == "0":
                            Queue_types()
                        elif double_end_queue == "1":
                            print(
                                """double endded queue:
        is a datastructure that allows insertion and removal of elements from both ends. it is similar to queue, but in a queue, we can only insert
        elements at the rear end and remove elements from the front end. this datastructure provides more flexibility than a queue and can be used
        for various applications such as implementing stacks, queues and lists.
                                    """
                            )
                            Double_End_Queue()

                        elif double_end_queue == "2":
                            print(
                                """how to create double endded queue: 
            start
        1. Initialize the deque with an empty list.
        2. Implement functions for checking if the deque is empty, getting its size,adding an element to the front,
        adding an element to the rear, removing an element from the front, removing an element from the rear, and displaying the elements.
        3. To add an element to the front, append it to the start of the deque list.
        4. To add an element to the rear, append it to the end of the deque list.
        5. To remove an element from the front, use the `pop(0)` function on the deque list.
        6. To remove an element from the rear, use the `pop()` function on the deque list.
        7. Implement the is_empty function to check if the deque is empty by checking the length of the deque list.
        8. Implement the get_size function to return the current number of elements in the deque.
        9. Implement the display function to print all the elements in the deque.
                                    end"""
                            )
                            print("Code and implementations of Double-ended-queue:")

                            # Function to create an empty deque
                            def create_deque():
                                return []

                            # Function to check if the deque is empty
                            def is_empty(deque):
                                return len(deque) == 0

                            # Function to get the size of the deque
                            def get_size(deque):
                                return len(deque)

                            # Function to add an item to the front of the deque
                            def add_front(deque, item, data_type):
                                try:
                                    if data_type == int:
                                        item = int(item)
                                    elif data_type == str:
                                        item = str(item)
                                    else:
                                        raise ValueError("Invalid data type.")
                                except ValueError:
                                    print("Invalid data type. Expected {}.".format(data_type.__name__))
                                    return

                                deque.insert(0, item)
                                print(f"Added element to the front: {item}")

                            # Function to add an item to the rear of the deque
                            def add_rear(deque, item, data_type):
                                try:
                                    if data_type == int:
                                        item = int(item)
                                    elif data_type == str:
                                        item = str(item)
                                    else:
                                        raise ValueError("Invalid data type.")
                                except ValueError:
                                    print("Invalid data type. Expected {}.".format(data_type.__name__))
                                    return

                                deque.append(item)
                                print(f"Added element to the rear: {item}")

                            # Function to remove an item from the front of the deque
                            def remove_front(deque):
                                if is_empty(deque):
                                    print("Deque is empty. Cannot remove element from the front.")
                                    return
                                removed_item = deque.pop(0)
                                print(f"Removed element from the front: {removed_item}")

                            # Function to remove an item from the rear of the deque
                            def remove_rear(deque):
                                if is_empty(deque):
                                    print("Deque is empty. Cannot remove element from the rear.")
                                    return
                                removed_item = deque.pop()
                                print(f"Removed element from the rear: {removed_item}")

                            # Function to display all items in the deque
                            def display(deque):
                                if is_empty(deque):
                                    print("Deque is empty.")
                                    return
                                print("Elements in the deque:")
                                for item in deque:
                                    print(item, end=" ")
                                print()

                            # Function to create a new deque based on user input
                            def Create_deque():
                                while True:
                                    choice = input("Enter 'i' for integer deque or 's' for string deque: ")
                                    if choice == "i":
                                        return [], int
                                    elif choice == "s":
                                        return [], str
                                    else:
                                        print("Invalid choice. Please try again.")
                            Create_deque()

                            deque, data_type = create_deque()

                            while True:
                                print("\n----- Options -----")
                                print("1. Add to Front")
                                print("2. Add to Rear")
                                print("3. Remove from Front")
                                print("4. Remove from Rear")
                                print("5. Display")
                                print("0. Back")

                                option = input("Enter your choice (1-6): ")

                                if option == "1":
                                    element = input("Enter the element to add to the front: ")
                                    add_front(deque, element, data_type)

                                elif option == "2":
                                    element = input("Enter the element to add to the rear: ")
                                    add_rear(deque, element, data_type)

                                elif option == "3":
                                    remove_front(deque)

                                elif option == "4":
                                    remove_rear(deque)

                                elif option == "5":
                                    display(deque)

                                elif option == "0":
                                    Double_End_Queue()
                                
                                else:
                                    print("Invalid choice. Please try again.")
                                    Queue_types()  
                        else:
                            print("invalid input, Enter from 0 to 2.")
                            Double_End_Queue()
                    Double_End_Queue()

                        
                elif queue_types == "3":
                    def Proiorty_Queue():
                        proiorty_queue = input("Select one option:\n0:Back\n 1:Definition \n 2: algorithm and Implementation \n Which One:")
                        if proiorty_queue == "0":
                            Queue_types()
                        elif proiorty_queue == "1":
                            print(
    """proiorty queue: 
            A more specialized data structure than a stack or queue.
            Items are ordered by key value so that the item with the
            lowest key is always at the first.
            Items are inserted in the proper position to maintain the
            order.
            Like ordinary queues, priority queues are used in various
            ways in certain computer systems."""
                            )
                            Proiorty_Queue()
                        elif proiorty_queue == "2":
                            print(
    """how to create proiorty queue: 
            start
            1. Initialize the priority queue as an empty list.
            2. Implement functions for checking if the priority queue is empty,
               adding an element with a priority, removing an element with the highest priority, and displaying the elements.
            3. When adding an element, create a tuple with the element value and its priority value, and append it to the priority queue list.
            4. When removing an element, find the item with the highest priority
               by using the `max` function with a key argument to compare priorities. Then, remove that item from the priority queue.
            5. Implement the is_empty function to check if the priority queue is empty by checking the length of the priority queue list.
            6. Implement the display function to print all the elements in the priority queue.
            end
            """
                            )
                            print("Code and implementation of Priorty queue")

                            # Function to check if the priority queue is empty
                            def is_empty(priority_queue):
                                return len(priority_queue) == 0

                            # Function to add an element to the priority queue with a given priority
                            def add_element(priority_queue, element, priority, item_type):
                                # Check if the priority is of the correct type
                                if item_type == 'i' and not isinstance(priority, int):
                                    raise ValueError(
                                        "Invalid priority. Integer expected for the priority queue of integers.")
                                elif item_type == 's' and not isinstance(priority, str):
                                    raise ValueError(
                                        "Invalid priority. String expected for the priority queue of strings.")
                                elif item_type == 'i' and isinstance(priority, str):
                                    try:
                                        # Try to convert the priority to an integer
                                        priority = int(priority)
                                    except ValueError:
                                        raise ValueError(
                                            "Invalid priority. Integer expected for the priority queue of integers.")

                                # Add the element to the priority queue
                                priority_queue.append((element, priority))
                                print(f"Added element: {element} with priority: {priority}")

                            # Function to remove an element from the priority queue
                            def remove_element(priority_queue):
                                if is_empty(priority_queue):
                                    print("Priority Queue is empty. Cannot remove element.")
                                    return

                                # Find the item with the highest priority
                                highest_priority_item = max(priority_queue, key=lambda item: item[1])
                                # Remove the highest priority item from the queue
                                priority_queue.remove(highest_priority_item)
                                removed_item = highest_priority_item[0]
                                print(f"Removed element: {removed_item}")

                            # Function to display all items in the priority queue
                            def display(priority_queue):
                                if is_empty(priority_queue):
                                    print("Priority Queue is empty.")
                                    return

                                print("Elements in the Priority Queue:")
                                for item in priority_queue:
                                    print(f"Element: {item[0]}, Priority: {item[1]}")

                            # Function to create a new priority queue based on user input
                            def create_priority_queue(item_type):
                                if item_type == 'i':
                                    return []
                                elif item_type == 's':
                                    return []
                                else:
                                    raise ValueError("Invalid item type. Please choose 'i' or 's'.")

                            # Get user input for the type of items in the queue
                            item_type = input(
                                "Enter 'i' for a priority queue of integers or 's' for a priority queue of strings: ")
                            if item_type not in ['i', 's']:
                                print("Invalid input. Only 'i' and 's' are allowed.")
                            else:
                                # Create a new priority queue based on user input
                                priority_queue = create_priority_queue(item_type)

                                while True:
                                    print("\nPriority Queue Operations:")
                                    print("1. Add Element")
                                    print("2. Remove Element")
                                    print("3. Display")
                                    print("0. Back")
                                    
                                    choice = input("Enter your choice (1-4): ")

                                    if choice == '1':
                                        element = input("Enter item to add: ")
                                        priority = input("Enter priority: ")
                                        try:
                                            add_element(priority_queue, element, priority, item_type)
                                        except ValueError as e:
                                            print(str(e))
                                    elif choice == '2':
                                        remove_element(priority_queue)
                                    elif choice == '3':
                                        display(priority_queue) 
                                    elif choice == '0':
                                        Proiorty_Queue()
                                    else:
                                        print("Invalid choice. Please enter a number from 0 to 3.")
                        else:
                            print("invalid input, Enter from 0 to 2.")
                            Proiorty_Queue()
                    Proiorty_Queue()
            Queue_types()

        elif queue_choose == "4":
            # Define a class for a queue data structure
            class Queue:
                # Initialize the queue
                def __init__(self):
                    self.queue = []  # The queue is initially empty
                    print("Created Queue:", self.queue)

                # Method to add an item to the queue
                def enqueue(self, item):
                    self.queue.append(item)
                    print("Queue: ", self.queue)

                # Method to remove an item from the queue
                def dequeue(self):
                    if not self.is_empty():
                        return self.queue.pop(0)
                    else:
                        raise IndexError("Queue is empty. Cannot perform dequeue operation.")

                # Method to get the front item of the queue
                def front(self):
                    if not self.is_empty():
                        return self.queue[0]
                    else:
                        raise IndexError("Queue is empty. Cannot perform front operation.")

                # Method to get the rear item of the queue
                def rear(self):
                    if not self.is_empty():
                        return self.queue[-1]
                    else:
                        raise IndexError("Queue is empty. Cannot perform rear operation.")

                # Method to display all items in the queue
                def display(self):
                    if not self.is_empty():
                        print("Queue: ")
                        for item in self.queue:
                            print(item, end=" ")
                    else:
                        print("Queue is empty.")

                # Method to check if the queue is empty
                def is_empty(self):
                    return len(self.queue) == 0

                # Method to get the size of the queue
                def size(self):
                    return len(self.queue)

                # Method to sort the items in the queue
                def sort(self):
                    self.queue.sort()
                    print("Sorted Queue: ", self.queue)

                # Method to search for an item in the queue
                def search(self, item, method, item_type):
                    if method == "1":  # Linear search
                        for i in range(len(self.queue)):
                            if self.queue[i] == item:
                                return i
                        return -1  # Item not found
                    elif method == "2":  # Binary search
                        low = 0
                        high = len(self.queue) - 1
                        while low <= high:
                            mid = (low + high) // 2
                            if self.queue[mid] == item:
                                return mid
                            elif item_type == 'i' and self.queue[mid] < item:
                                low = mid + 1
                            elif item_type == 's' and self.queue[mid] < str(item):
                                low = mid + 1
                            else:
                                high = mid - 1
                        return -1  # Item not found
                    else:
                        raise ValueError("Invalid search method. Please choose 1 for linear or 2 for binary.")

            def operations():
                try:
                    print("Creating and operations of Queue:")
                    queue_type = input("Enter 'i' for a queue of integers or 's' for a queue of strings: ")
                    if queue_type not in ['i', 's']:
                        print("Invalid input. Only 'i' and 's' are allowed.")
                        operations()

                    queue = Queue()
                    
                    queue_size = int(input("Enter the size of the queue: "))
                    print("Enter items to enqueue: ")
                    for i in range(queue_size):
                        item = input(f"Enter item {i+1}: ")
                        try:
                            if queue_type == 'i':
                                print(queue.enqueue(int(item)))
                            else:
                                queue.enqueue(item)
                        except ValueError:
                            print("Invalid input. Please enter integers.")
                            operations()
                            
                    print("Queue operations:")
                    while True:
                        print("\n1. Enqueue")
                        print("2. Dequeue")
                        print("3. Front")
                        print("4. Rear")
                        print("5. Display")
                        print("6. Sort")
                        print("7. Search")
                        print("0. Back")

                        choice = input("Enter your choice (0-7): ")

                        if choice == '1':
                            item = input("Enter item to enqueue: ")
                            try:
                                if queue_type == 'i':
                                    queue.enqueue(int(item))
                                else:
                                    queue.enqueue(item)
                            except ValueError:
                                print("Invalid input.Please enter integer.")
                                print("Queue: ", queue)
                        elif choice == '2':
                            try:
                                dequeued_item = queue.dequeue()
                                print(f"Dequeued item: {dequeued_item}")
                            except IndexError as e:
                                print(str(e))
                        elif choice == '3':
                            try:
                                front_item = queue.front()
                                print(f"Front item: {front_item}")
                            except IndexError as e:
                                print(str(e))
                        elif choice == '4':
                            try:
                                rear_item = queue.rear()
                                print(f"Rear item: {rear_item}")
                            except IndexError as e:
                                print(str(e))
                        elif choice == '5':
                            queue.display()
                        elif choice == '6':
                            queue.sort()
                        elif choice == '7':
                            search_item = input("Enter item to search: ")
                            search_method = input("Enter search method \n 1:linear  \n2:binary \n Your Choice ")
                            try:
                                if search_method not in ['1', '2']:
                                    raise ValueError("Invalid search method. Please choose '1' or '2'.")
                                if queue_type == 'i':
                                    search_item = int(search_item)
                                index = queue.search(search_item, search_method, queue_type)
                                if index != -1:
                                    print(f"Item {search_item} found at index {index}")
                                else:
                                    print(f"Item {search_item} not found")
                            except ValueError as e:
                                print(str(e))
                        elif choice == '0':
                            Queu()
                        else:
                            print("Invalid choice. Please enter a number from 0 to 7.")

                except ValueError:
                    print("Invalid input. Please enter integer values for the queue size.")
                    operations()
                except KeyboardInterrupt:
                    print("Program interrupted.")

            operations()
        elif queue_choose == "5":
            data_structure()
        else:
            print("invalid Input, Enter from 0 t0 5.")
            Queu()

#++++++++++++++++++++++++++++++++++++++++++++End of Queue++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def Linked_list():
        def Singly_linked_list():
            # operations of linked list ----------------------------------------
            def Operations():
                # Define a class Node
                class Node:
                    # Initialize the Node object
                    def __init__(self, data):
                        self.data = data  # Assign data
                        self.next = None  # Initialize next as null

                # Define a class LinkedList
                class LinkedList:
                    # Function to initialize the LinkedList object
                    def __init__(self):
                        self.head = None  # Initialize head as null

                    # Function to add new node at the end of the Linked List
                    def append(self, data):
                        new_node = Node(data)  # Create a new node
                        if not self.head:  # If the Linked List is empty, then make the new node as head
                            self.head = new_node
                        else:  # Else traverse till the last node and add the new_node there
                            current = self.head
                            while current.next:
                                current = current.next
                            current.next = new_node

                    # Function to add new node at the beginning of the Linked List
                    def insert(self, data):
                        new_node = Node(data)  # Create a new node
                        if not self.head:  # If the Linked List is empty, then make the new node as head
                            self.head = new_node
                        else:  # Else make the new_node as head and its next as old head
                            new_node.next = self.head
                            self.head = new_node

                    # Function to delete a node in a LinkedList
                    def delete(self, value):
                        if not self.head:  # If linked list is empty return
                            return
                        if self.head.data == value:  # If head needs to be removed
                            self.head = self.head.next  # Change head
                            return
                        current = self.head  # Else find the key to be deleted and remove it
                        while current.next:
                            if current.next.data == value:
                                current.next = current.next.next
                                return
                            current = current.next

                    # Function to print the linked list
                    def display(self):
                        current = self.head  # Start from head
                        while current:  # While end of linked list is not reached
                            print(current.data, end=" -> ")  # Print data
                            current = current.next  # Move to next node
                        print("None")  # Print None when end of linked list is reached

                    # Function to search a value in linked list
                    def search(self, value):
                        current = self.head  # Start from head
                        while current:  # While end of linked list is not reached
                            if current.data == value:  # If value is found return True
                                return True
                            current = current.next  # Move to next node
                        return False  # If value was not present in linked list return False

                    # Function to get length of linked list
                    def length(self):
                        count = 0  # Initialize count
                        current = self.head  # Start from head
                        while current:  # While end of linked list is not reached
                            count += 1  # Increment count
                            current = current.next  # Move to next node
                        return count  # Return count of nodes in linked list

                # create linked list based on user input
                data_type = input("Choose data type (int/ str): ")
                linked_list_obj = LinkedList()
                while True:
                    data = input(f"Enter {data_type} data to add or type '#' to exit: ")
                    if data == "#":
                        break
                    try:
                        if data_type == "int":
                            data = int(data)
                        linked_list_obj.append(data)
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")
                        continue
                    linked_list_obj.display()

                # perform operations on linked list
                while True:
                    operation_choice = input("Select an operation:\n 1:insert \n2:delete \n3:traverse \n4:search \n5::length \n0:Back /n Your Choice: ")
                    if operation_choice == "0":
                        break
                    elif operation_choice == "1":
                        data = input(f"Enter {data_type} data to insert: ")
                        try:
                            if data_type == "int":
                                data = int(data)
                            linked_list_obj.insert(data)
                            linked_list_obj.display()
                        except ValueError:
                            print("Invalid input. Please enter a valid integer.")
                    elif operation_choice == "2":
                        data = input(f"Enter {data_type} data to delete: ")
                        try:
                            if data_type == "int":
                                data = int(data)
                            linked_list_obj.delete(data)
                            linked_list_obj.display()
                        except ValueError:
                            print("Invalid input. Please enter a valid integer.")
                    elif operation_choice == "3":
                        linked_list_obj.display()
                    elif operation_choice == "4":
                        data = input(f"Enter {data_type} data to search: ")
                        try:
                            if data_type == "int":
                                data = int(data)
                            result = linked_list_obj.search(data)
                            if result:
                                print(f"{data} exists in the linked list.")
                            else:
                                print(f"{data} does not exist in the linked list.")
                        except ValueError:
                            print("Invalid input. Please enter a valid integer.")
                    elif operation_choice == "5":
                        length = linked_list_obj.length()
                        print(f"Length of the linked list is: {length}.")
                        
                    else:
                        print("Invalid choice. Please select a valid operation.")


            singly_linked_list_choose = input("Select one option:\n 1: Definitions\n 2: How to create and Operations\n 0: back \n Your Choice: ")
            if singly_linked_list_choose == "1":
                print(
                    "Singly_linked list:\n Each node points to the next node in the list, forming a unidirectional chain."
                )
                Singly_linked_list()
            if singly_linked_list_choose == "2":
                print(
                    """To create a singly linked list in python:
        1: Define the Node class: Create a class that represents a single node in the .linked list.
            Each node should have a value and a pointer to the next node.
            classNode:
                def__init__(self,value):
                self.value=value
                self.next=None

        2: Define the linked list class: create a class that represents a linked list. This class should
         have methods to perform operations on a linked list.

         classLinkedList:
             def__init__(self): 
             self.head=None
                                            """
                )
                print("Lets Create a singly Linked list:")
                Operations()
                Singly_linked_list()
            if singly_linked_list_choose == "0":
                Linked_list()
            else:
                print("Invalid Input")
                Singly_linked_list()
        # end of single -------------------------------------------------------------------------
        def Circular_Singly_linked_list():
            # Define a class Node
            class Node:
                # Initialize the Node object
                def __init__(self, data):
                    self.data = data  # Assign data
                    self.next = None  # Initialize next as null

            # Define a class CircularSinglyLinkedList
            class CircularSinglyLinkedList:
                # Function to initialize the CircularSinglyLinkedList object
                def __init__(self):
                    self.head = None  # Initialize head as null

                # Function to add new node at the beginning of the Circular Linked List
                def insert_at_beginning(self, data):
                    new_node = Node(data)  # Create a new node
                    if not self.head:  # If the Linked List is empty, then make the new node as head and point it to itself
                        new_node.next = new_node
                        self.head = new_node
                    else:  # Else traverse till the last node, add the new_node there and make it as head
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                        new_node.next = self.head
                        temp.next = new_node
                        self.head = new_node

                # Function to add new node at the end of the Circular Linked List
                def insert_at_end(self, data):
                    new_node = Node(data)  # Create a new node
                    if not self.head:  # If the Linked List is empty, then make the new node as head and point it to itself
                        new_node.next = new_node
                        self.head = new_node
                    else:  # Else traverse till the last node and add the new_node there and point it to head
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                        temp.next = new_node
                        new_node.next = self.head

                # Function to delete a node from beginning in a Circular LinkedList
                def delete_from_beginning(self):
                    if not self.head:  # If linked list is empty return
                        return
                    if self.head.next == self.head:  # If only one node is present, make head as null
                        self.head = None
                    else:  # Else traverse till last node and change its next to second node and make second node as head
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                        temp.next = self.head.next
                        self.head = self.head.next

                # Function to delete a node from end in a Circular LinkedList
                def delete_from_end(self):
                    if not self.head:  # If linked list is empty return
                        return
                    if self.head.next == self.head:  # If only one node is present, make head as null
                        self.head = None
                    else:  # Else traverse till second last node and change its next to head
                        temp = self.head
                        prev = None
                        while temp.next != self.head:
                            prev = temp
                            temp = temp.next
                        prev.next = self.head

                # Function to print the circular linked list
                def traverse(self):
                    if not self.head:  # If linked list is empty return
                        return
                    temp = self.head  # Start from head
                    while True:  # While end of linked list is not reached
                        print(temp.data, end="->")  # Print data
                        temp = temp.next
                        if temp == self.head:  # If end of linked list is reached, break
                            break
                    print(self.head.data)  # Print data of head at end

            # ExampleUsage
            circular_list = CircularSinglyLinkedList()
            circular_list.insert_at_beginning(9)
            circular_list.insert_at_beginning(5)
            circular_list.insert_at_beginning(2)

            def operations():
                cir_singly_operation_choose =input( "Choose one option:\n 1: Insertion\n 2: Deletion\n 3: Traversal\n 4 : MainMenu \n Your Choice: ")
                if cir_singly_operation_choose == "1":
                    print(circular_list.traverse())
                    if (input("Do you want to insert at the begining or end type(b/e): "
                        )
                        == "b"
                    ):
                        circular_list.insert_at_beginning(input("Enter the element: "))
                    else:
                        circular_list.insert_at_end(input("Enter the element: "))
                    print(circular_list.traverse())
                    Circular_Singly_linked_list()

                elif cir_singly_operation_choose == "2":
                    print(circular_list.traverse())
                    if (
                        input(
                            "Do you want to delete at the begining or end type(begining/end): "
                        )
                        == "b"
                    ):
                        circular_list.delete_from_beginning()
                    else:
                        circular_list.delete_from_end()
                    print(circular_list.traverse())
                    Circular_Singly_linked_list()

                elif cir_singly_operation_choose == "3":
                    print(circular_list.traverse())
                    Circular_Singly_linked_list()
                elif cir_singly_operation_choose =="4":
                    data_structure()
                else:
                    print("invalid input")
                    Circular_Singly_linked_list()

            circular_singly_linked_list_choose =input("Select one option:\n 1: Definitions\n 2: How to create And Operations\n 0 : back \n Your Choice: ")
            if circular_singly_linked_list_choose == "1":
                print("circular linked list:\n is a type of linked list where the last node of the list points back to the first node , forming a loop.")
                Circular_Singly_linked_list()
            elif circular_singly_linked_list_choose == "2":
                print(
                    """To create a singly linked list in python:
                    1: Define the Node class: Create a class that represents a single node in the .linked list.
                        Each node should have a value and a pointer to the next node.
                        classNode:
                            def__init__(self,value):
                            self.value=value
                            self.next=None

                    2: Define the linked list class: create a class that represents a linked list. This class should
                     have methods to perform operations on a linked list.

                     classLinkedList:
                         def__init__(self): 
                         self.head=None
                         self.tail=None
                                            """
                )
                print("Lets Do the operations:")
                operations()
                Circular_Singly_linked_list()
            
            elif circular_singly_linked_list_choose == "0":
                Linked_list()
            else:
                print("Invalid input")
                Linked_list()
                

        # end of circular linked list -------------------------------

        def Doubly_linked_list():
            class Node:
                def __init__(self, data):
                    self.data = data
                    self.next = None
                    self.prev = None

            class DoublyLinkedList:
                def __init__(self):
                    self.head = None

                # Insertion at the Beginning
                def insert_at_beginning(self, data):
                    new_node = Node(data)
                    if not self.head:
                        self.head = new_node
                    else:
                        new_node.next = self.head
                        self.head.prev = new_node
                        self.head = new_node

                # Insertion at the End
                def insert_at_end(self, data):
                    new_node = Node(data)
                    if not self.head:
                        self.head = new_node
                    else:
                        temp = self.head
                        while temp.next:
                            temp = temp.next
                        temp.next = new_node
                        new_node.prev = temp

                # Deletion from the Beginning
                def delete_from_beginning(self):
                    if not self.head:
                        return
                    if not self.head.next:
                        self.head = None
                    else:
                        self.head = self.head.next
                        self.head.prev = None

                # Deletion from the End
                def delete_from_end(self):
                    if not self.head:
                        return
                    if not self.head.next:
                        self.head = None
                    else:
                        temp = self.head
                        while temp.next.next:
                            temp = temp.next
                        temp.next = None

                # Traversal Forward
                def traverse_forward(self):
                    if not self.head:
                        print("Doubly linked list is empty.")
                        return
                    temp = self.head
                    while temp:
                        print(temp.data, end=" <-> ")
                        temp = temp.next
                    print("None")

                # Traversal Backward
                def traverse_backward(self):
                    if not self.head:
                        print("Doubly linked list is empty.")
                        return
                    temp = self.head
                    while temp.next:
                        temp = temp.next
                    while temp:
                        print(temp.data, end=" <-> ")
                        temp = temp.prev
                    print("None")

            # Example Usage
            doubly_list = DoublyLinkedList()
            doubly_list.insert_at_beginning(3)
            doubly_list.insert_at_beginning(12)
            doubly_list.insert_at_beginning(38)

            def operations():
                dou_operation_choose = input("Select one option:\n 1: Insertion\n 2: Deletion\n 3: Traversal\n 0 : back \n Your Choice: ")
                

                if dou_operation_choose == "1":
                    print(doubly_list.traverse_forward())
                    if (
                        input(
                            "Do you want to insert at the begining or end type(b/e): "
                        )
                        == "b"
                    ):
                        doubly_list.insert_at_beginning(input("Enter the element: "))
                    else:
                        doubly_list.insert_at_end(input("Enter the element: "))
                    print(doubly_list.traverse_forward())
                    Doubly_linked_list()

                elif dou_operation_choose == "2":
                    print(doubly_list.traverse_forward())
                    if (
                        input(
                            "Do you want to delete from the begining or end type(b/e): "
                        )
                        == "b"
                    ):
                        doubly_list.delete_from_beginning()
                    else:
                        doubly_list.delete_from_end()
                    print(doubly_list.traverse_forward())
                    Doubly_linked_list()
                elif dou_operation_choose == "3":
                    print(doubly_list.traverse_forward())
                    if (
                        input(
                            "Do you want to traverse from the forward or backward(f/b): "
                        )
                        == "f"
                    ):
                        doubly_list.traverse_forward()
                    else:
                        doubly_list.traverse_backward()
                    Doubly_linked_list()
                elif dou_operation_choose == "0":
                    Doubly_linked_list()
                else:
                    print("Invalid Input")

            doubly_linked_list_choose = input("Select one option:\n 1: Definitions\n 2: How to create and operations\n0: back \n  Your Choice: ")
            

            if doubly_linked_list_choose == "1":
                print("In double linked list:\n each node containse two pointers, one pointing to the next node"
                    + " (as in a singly linked list) and another pointing to the previous node ")
                Doubly_linked_list()
            elif doubly_linked_list_choose == "2":
                print(
                    """To create a doubly linked list in python:
                    1: Define the Node class: Create a class that represents a single node in the .linked list.
                        Each node should have a value and two pointers to the next and privious node.
                        classNode:
                            def__init__(self,value):
                            self.value=value
                            self.next=None
                            self.prev=None

                    2: Define the doubly linked list class: create a class that represents a linked list. This class should
                     have methods to perform operations on a linked list.

                        class DoublyLinkedList:
                            def__init__(self): 
                                self.head=None
                                self.tail=None
                                            """
                )
                print("lets Do the Operations")
                operations()
                Doubly_linked_list()
            elif doubly_linked_list_choose == "0":
                Doubly_linked_list()
            else:
                print("Invalid Input")
                Doubly_linked_list()

        # end of Doubly_linked_list ---------------------------------------------------------

        def Circular_Doubly_linked_list():
            class Node:
                def __init__(self, data):
                    self.data = data
                    self.next = None
                    self.prev = None

            class CircularDoublyLinkedList:
                def __init__(self):
                    self.head = None

                # Insertion at the Beginning
                def insert_at_beginning(self, data):
                    new_node = Node(data)
                    if not self.head:
                        new_node.next = new_node
                        new_node.prev = new_node
                        self.head = new_node
                    else:
                        new_node.next = self.head
                        new_node.prev = self.head.prev
                        self.head.prev.next = new_node
                        self.head.prev = new_node
                        self.head = new_node

                # Insertion at the End
                def insert_at_end(self, data):
                    new_node = Node(data)
                    if not self.head:
                        new_node.next = new_node
                        new_node.prev = new_node
                        self.head = new_node
                    else:
                        new_node.next = self.head
                        new_node.prev = self.head.prev
                        self.head.prev.next = new_node
                        self.head.prev = new_node

                # Deletion from the Beginning
                def delete_from_beginning(self):
                    if not self.head:
                        return
                    if self.head.next == self.head:
                        self.head = None
                    else:
                        self.head.prev.next = self.head.next
                        self.head.next.prev = self.head.prev
                        self.head = self.head.next

                # Deletion from the End
                def delete_from_end(self):
                    if not self.head:
                        return
                    if self.head.next == self.head:
                        self.head = None
                    else:
                        self.head.prev.prev.next = self.head
                        self.head.prev = self.head.prev.prev

                # Traversal Forward
                def traverse_forward(self):
                    if not self.head:
                        print("Circular doubly linked list is empty.")
                        return
                    temp = self.head
                    while True:
                        print(temp.data, end=" <-> ")
                        temp = temp.next
                        if temp == self.head:
                            break
                    print(self.head.data)  # Print the starting node again

                # Traversal Backward
                def traverse_backward(self):
                    if not self.head:
                        print("Circular doubly linked list is empty.")
                        return
                    temp = self.head.prev
                    while True:
                        print(temp.data, end=" <-> ")
                        temp = temp.prev
                        if temp == self.head.prev:
                            break
                    print(self.head.prev.data)  # Print the last node again

            # Example Usage
            circular_doubly_list = CircularDoublyLinkedList()
            circular_doubly_list.insert_at_beginning(3)
            circular_doubly_list.insert_at_beginning(8)
            circular_doubly_list.insert_at_beginning(54)
            circular_doubly_list.insert_at_beginning(89)

            def operations():
                cir_dou_operation_choose = input("Select one option:\n 1: Insertion\n 2: Deletion\n 3: Traversal\n 4 : MainMenu \n 0 : back \nYour Choice: ")
                

                if cir_dou_operation_choose == "1":
                    print(circular_doubly_list.traverse_forward())
                    if (
                        input(
                            "Do you want to insert at the begining or end type(b/e): "
                        )
                        == "b"
                    ):
                        circular_doubly_list.insert_at_beginning(
                            input("Enter the element: ")
                        )
                    else:
                        circular_doubly_list.insert_at_end(input("Enter the element: "))
                    print(circular_doubly_list.traverse_forward())
                    Circular_Doubly_linked_list()

                elif cir_dou_operation_choose == "2":
                    print(circular_doubly_list.traverse_forward())
                    if (
                        input(
                            "Do you want to delete from the begining or end type(b/e): "
                        )
                        == "b"
                    ):
                        circular_doubly_list.delete_from_beginning()
                    else:
                        circular_doubly_list.delete_from_end()
                    print(circular_doubly_list.traverse_forward())
                    Circular_Doubly_linked_list()

                elif cir_dou_operation_choose == "3":
                    print(circular_doubly_list.traverse_forward())
                    if (
                        input(
                            "Do you want to traverse from the forward or backward(f/b): "
                        )
                        == "f"
                    ):
                        circular_doubly_list.traverse_forward()
                    else:
                        circular_doubly_list.traverse_backward()
                    Circular_Doubly_linked_list()
                elif cir_dou_operation_choose == "0":
                    Circular_Doubly_linked_list()
                else:
                    print("Invalid input")
                    Circular_Doubly_linked_list()

            circular_Doubly_linked_list_choose = input("Select one option:\n 1: Defenations\n 2: How to create and Operations\n 0 : back \n  Choose: ")
            

            if circular_Doubly_linked_list_choose == "1":
                print(
                    " circuly doubly linked list:\n is a varition of doubly linked list in which the last node's 'next'"
                    + " pointer points back to the first node creating the circular structure."
                )
                Circular_Doubly_linked_list()

            elif circular_Doubly_linked_list_choose == "2":
                print(
                    """To create a circular doubly linked list in python:
                    1: Define the Node class: Create a class that represents a single node in the .linked list.
                        Each node should have a value and two pointers to the next and privious node.
                        classNode:
                            def__init__(self,value):
                            self.value=value
                            self.next=None
                            self.prev=None

                    2: Define the doubly linked list class: create a class that represents a linked list. This class should
                     have methods to perform operations on a linked list.

                        class CircularDoublyLinkedList:
                            def__init__(self): 
                                self.head=None
                                 
                                            """
                )
                print("Lets Do the operations:")
                operations()
                
                Circular_Doubly_linked_list()
            elif circular_Doubly_linked_list_choose == "0":
                Linked_list()
                
            else:
                print("Invalid Input")
                Circular_Doubly_linked_list()
                

        # ends of Circular_Doubly_linked_list --------------------------------------------------

        linked_list_choose = input("Select one option:\n 1: Defenations\n 2: How to create\n 3: Types\n 4: MainMenu\n Your Choice: ")
        

        if linked_list_choose == "1":
            print(
                "Lonked List:\nA linked list is a linear data structore in which elements are stored add the contiguous memory locations."
                + " Insted, each element(node) in a linked list contains a refference(linke) to the next node in the sequence."
            )
            Linked_list()
        elif linked_list_choose == "2":
            print(
                """To create a linked list in python:
                    1: Define the Node class: Create a class that represents a single node in the .linked list.
                        Each node should have a value and a pointer to the next node.
                        classNode:
                            def__init__(self,value):
                            self.value=value
                            self.next=None

                    2: Define the linked list class: create a class that represents a linked list. This class should
                     have methods to perform operations on a linked list.

                     classLinkedList:
                         def__init__(self): 
                         self.head=None
                                            """
            )
            Linked_list()

        elif linked_list_choose == "3":
            linked_list_type_choose = input("We have four types, select one option:\n 1: Singly linked list\n 2: circular Singly linked list\n 3: Doubly linked list\n 4: Circular  Doubly linked list\n 0: back \n Your Choice:")
            

            if linked_list_type_choose == "1":
                Singly_linked_list()
            elif linked_list_type_choose == "2":
                Circular_Singly_linked_list()
            elif linked_list_type_choose == "3":
                Doubly_linked_list()
            elif linked_list_type_choose == "4":
                Circular_Doubly_linked_list()
            elif linked_list_type_choose == "0":
                data_structure()
        elif linked_list_choose == "0":
            data_structure()
        elif linked_list_choose == "4":
            data_structure()
#+++++++++++++++++++++++++++++++++++++++++++++++++=End Of Linked List++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def TreeDs():
        tree_Choose = input(
            "Select one Option:\n   0:Main Menu\n   1:Definitions And Representation \n   2:Applications \n   3:How to Create And operations \n   4: Tree Types \n    Your Choice: ")

        if tree_Choose == "1":
            print(""""Tree:\n
Tree is a data structure that is used to store data in a hierarchy.
Tree is a non-linear data structure.
Each element of the tree is known as node.
The top element of the tree is known as the root.
""")

            # Define a class TreeNode
            class TreeNode:
                # Initialize the TreeNode object
                def __init__(self, value):
                    self.value = value  # Assign value
                    self.parent = None  # Initialize parent as null
                    self.children = []  # Initialize children as empty list

                # Function to add a child node
                def add_child(self, child):
                    child.parent = self  # Set parent of child node to current node
                    self.children.append(child)  # Add child node to children list

                # Function to remove a child node
                def remove_child(self, child):
                    child.parent = None  # Remove parent of child node
                    self.children.remove(child)  # Remove child node from children list

                # Function to check if the node is a leaf (has no children)
                def is_leaf(self):
                    return len(self.children) == 0

                # Function to check if the node is a root (has no parent)
                def is_root(self):
                    return self.parent is None

                # Function to get the parent of the node
                def get_parent(self):
                    return self.parent

                # Function to get the children of the node
                def get_children(self):
                    return self.children

                # Function to get the path from root to the node
                def get_path(self):
                    path = [str(self.value)]  # Start with current node value
                    current_node = self
                    while current_node.parent:  # Traverse up to root
                        path.append(str(current_node.parent.value))  # Add parent value to path
                        current_node = current_node.parent  # Move to parent
                    return ' -> '.join(path[::-1])  # Reverse and join path with ' -> '

                # Function to get all ancestors of the node (from parent up to root)
                def get_ancestors(self):
                    ancestors = []
                    current_node = self.parent  # Start with parent
                    while current_node:  # Traverse up to root
                        ancestors.append(current_node)  # Add current node to ancestors list
                        current_node = current_node.parent  # Move to parent
                    return ancestors

                # Function to get all descendants of the node (from children down to leaves)
                def get_descendants(self):
                    descendants = []
                    for child in self.children:  # Traverse all children and their descendants
                        descendants.append(child)  # Add child to descendants list
                        descendants.extend(child.get_descendants())  # Add descendants of child to descendants list
                    return descendants

                # Function to get all nodes in the subtree rooted at the node (including the node itself)
                def get_subtree(self):
                    return [self] + self.get_descendants()  # Return list containing the node and its descendants

                # Function to get all siblings of the node (other children of its parent)
                def get_siblings(self):
                    if self.is_root():  # If the node is root, it has no siblings
                        return []
                    siblings = []
                    for child in self.get_parent().children:  # Traverse all children of parent
                        if child != self:  # If child is not the current node, it's a sibling
                            siblings.append(child)
                    return siblings

                # Function to get degree of the node (number of its children)
                def get_node_degree(self):
                    return len(self.children)

                # Function to get degree of the tree rooted at the node (maximum number of children among all nodes in the subtree)
                def get_tree_degree(self):
                    max_degree = self.get_node_degree()  # Start with degree of current node
                    for child in self.children:
                        max_degree = max(max_degree,
                                         child.get_tree_degree())  # Update max_degree with degree of child if it's larger
                    return max_degree

                # Function to get depth of the node (number of edges on path from root to the node)
                def get_node_depth(self):
                    depth = 0
                    current_node = self
                    while current_node.parent:
                        depth += 1
                        current_node = current_node.parent
                    return depth

                    # Function to get height of the tree rooted at the node (number of edges on longest path from the node down to a leaf)

                def get_node_height(self):
                    if self.is_leaf():
                        return 0
                    max_height = 0
                    for child in self.children:
                        max_height = max(max_height, child.get_node_height())
                    return max_height + 1

            def build_tree():
                root_value = input("Enter the root value: ")
                root = TreeNode(root_value)
                nodes = {root_value: root}
                stack = [root]

                while stack:
                    current_node = stack.pop()
                    child_values = input(
                        f"Enter the child values for node {current_node.value} (space-separated), or enter 'stop' to stop: ").split()
                    if child_values[0].lower() == 'stop':
                        break
                    for child_value in child_values:
                        child_node = TreeNode(child_value)
                        current_node.add_child(child_node)
                        nodes[child_value] = child_node
                        stack.append(child_node)

                return root, nodes

            def main():
                try:
                    root, nodes = build_tree()

                    print("\nTree representation:")
                    print("Root:", root.value)
                    for value, node in nodes.items():
                        parent = node.get_parent() if not node.is_root() else None
                        children = [child.value for child in node.get_children()]
                        path = node.get_path()
                        ancestors = [ancestor.value for ancestor in node.get_ancestors()]
                        descendants = [descendant.value for descendant in node.get_descendants()]
                        subtree = [subtree_node.value for subtree_node in node.get_subtree()]
                        siblings = [sibling.value for sibling in node.get_siblings()]
                        degree = node.get_node_degree()
                        tree_degree = node.get_tree_degree()
                        depth = node.get_node_depth()
                        height = node.get_node_height()

                        print()
                        print("Value:", value)
                        print("Parent:", parent.value if parent else None)
                        print("Children:", children)
                        print("Path:", path)
                        print("Ancestors:", ancestors)
                        print("Descendants:", descendants)
                        print("Subtree:", subtree)
                        print("Siblings:", siblings)
                        print("Degree of node:", degree)
                        print("Degree of tree:", tree_degree)
                        print("Depth of node:", depth)
                        print("Height of node:", height)

                    TreeDs()
                except Exception as e:
                    print("An error occurred:", str(e))
                    TreeDs()

            if __name__ == '__main__':
                main()



        elif tree_Choose == "2":
            print(""""Applications of Tree:\n
File Systems: The file system of a computer is often represented as a tree. Each folder or directory is a node in the tree, and files are the leaves.
XML Parsing: Trees are used to parse and process XML documents. An XML document can be thought of as a tree, with elements as nodes and attributes as properties of the nodes.
Database Indexing: Many databases use trees to index their data. The B-tree and its variations are commonly used for this purpose.
Compiler Design: The syntax of programming languages is often defined using a tree structure called a parse tree. This is used by compilers to understand the structure of the code and generate machine code from it.
Artificial Intelligence: Decision trees are often used in artificial intelligence to make decisions based on a series of criteria.
    """)
            TreeDs()
        elif tree_Choose == "3":
            print("Creating And Operations of Tree")

            # Define a class TreeNode
            class TreeNode:
                # Initialize the TreeNode object
                def __init__(self, data):
                    self.data = data  # Assign data
                    self.left = None  # Initialize left child as null
                    self.right = None  # Initialize right child as null

            # Define a class Tree
            class Tree:
                # Function to initialize the Tree object
                def __init__(self, data_type):
                    self.root = None  # Initialize root as null
                    self.data_type = data_type  # Assign data type

                # Function to insert a node into the tree
                def insert(self, data):
                    if self.root is None:  # If tree is empty, create root node with given data
                        if self.data_type == int:
                            self.root = TreeNode(int(data))
                        else:
                            self.root = TreeNode(str(data))
                    else:  # Else call helper function to insert node at correct position in the tree
                        self._insert(self.root, data)
                    self.print_tree()  # Print the tree after insertion

                # Helper function to insert a node into the tree
                def _insert(self, current, data):
                    if self.data_type == int:  # If data type is integer
                        if int(data) < current.data:  # If given data is less than current node's data, insert in left subtree
                            if current.left is None:  # If left child of current node is empty, create new node there
                                current.left = TreeNode(int(data))
                            else:  # Else call helper function recursively for left child of current node
                                self._insert(current.left, data)
                        else:  # If given data is greater than or equal to current node's data, insert in right subtree
                            if current.right is None:  # If right child of current node is empty, create new node there
                                current.right = TreeNode(int(data))
                            else:  # Else call helper function recursively for right child of current node
                                self._insert(current.right, data)
                    else:  # If data type is string (similar logic as above)
                        if str(data) < current.data:
                            if current.left is None:
                                current.left = TreeNode(str(data))
                            else:
                                self._insert(current.left, data)
                        else:
                            if current.right is None:
                                current.right = TreeNode(str(data))
                            else:
                                self._insert(current.right, data)

                # Function to delete a node from the tree
                def delete(self, data):
                    if self.root is None:  # If tree is empty, print error message and return
                        print("Tree is empty. Cannot delete node.")
                        return
                    self.root = self._delete(self.root,
                                             data)  # Call helper function to delete node from the tree and update root
                    self.print_tree()  # Print the tree after deletion

                # Helper function to delete a node from the tree
                def _delete(self, current, data):
                    if current is None:  # If tree/subtree is empty, return null
                        return current

                    if self.data_type == int:  # If data type is integer
                        if int(data) < current.data:  # If given data is less than current node's data, delete from left subtree and update left child of current node
                            current.left = self._delete(current.left, data)
                        elif int(
                                data) > current.data:  # If given data is greater than current node's data, delete from right subtree and update right child of current node
                            current.right = self._delete(current.right, data)
                        else:  # If given data is equal to current node's data (node to be deleted found)
                            if current.left is None:  # If left child of current node is empty, replace it with its right child (could be null or a subtree)
                                return current.right
                            elif current.right is None:  # If right child of current node is empty (and left child isn't), replace it with its left child (a subtree)
                                return current.left
                            else:  # If both children of current node are non-empty (current node has two children)
                                min_val_right_subtree = self._minimum_value(
                                    current.right)  # Find minimum value in right subtree (successor in inorder traversal)
                                current.data = min_val_right_subtree  # Replace value of current node with minimum value found above (this doesn't affect binary search tree property)
                                current.right = self._delete(current.right,
                                                             min_val_right_subtree)  # Delete the duplicate value from right subtree (this doesn't affect binary search tree property)

                    else:  # If data type is string (similar logic as above)
                        if str(data) < current.data:
                            current.left = self._delete(current.left, data)
                        elif str(data) > current.data:
                            current.right = self._delete(current.right, data)
                        else:
                            if current.left is None:
                                return current.right
                            elif current.right is None:
                                return current.left
                            else:
                                min_val_right_subtree = self._minimum_value(current.right)
                                current.data = min_val_right_subtree
                                current.right = self._delete(current.right, min_val_right_subtree)

                    return current  # Return updated tree/subtree

                # Helper function to find the node with minimum value in a given tree/subtree
                def _minimum_value(self, node):
                    current = node  # Start with given node
                    while current.left:  # Traverse left subtree till leftmost leaf (minimum value in a binary search tree)
                        current = current.left
                    return current.data  # Return minimum value

                # Function to search for a node with given data in the tree
                def search(self, data):
                    if self.root is None:  # If tree is empty, print error message and return None
                        print("Tree is empty. Cannot search for node.")
                        return None
                    if self.data_type == int:  # If data type is integer, call helper function to search for integer data in the tree
                        result = self._search(self.root, int(data))
                    else:  # If data type is string, call helper function to search for string data in the tree
                        result = self._search(self.root, str(data))
                    if result:  # If node found, print success message
                        print("Node found.")
                    else:  # If node not found, print error message
                        print("Node not found.")
                    return result  # Return found node (or None if not found)

                # Helper function to search for a node with given data in a given tree/subtree
                def _search(self, current, data):
                    if current is None or current.data == data:  # If tree/subtree is empty or node with given data found, return current node
                        return current

                    if self.data_type == int:  # If data type is integer
                        if int(data) < current.data:  # If given data is less than current node's data, search in left subtree
                            return self._search(current.left, data)
                        else:  # If given data is greater than or equal to current node's data, search in right subtree
                            return self._search(current.right, data)
                    else:  # If data type is string (similar logic as above)
                        if str(data) < current.data:
                            return self._search(current.left, data)
                        else:
                            return self._search(current.right, data)

                # Function to perform preorder traversal of the tree (visit root, traverse left subtree, traverse right subtree)
                def preorder_traversal(self):
                    if self.root is None:  # If tree is empty, print error message
                        print("Tree is empty.")
                    else:
                        print("Preorder Traversal:")  # Print traversal type message
                        self._preorder_traversal(
                            self.root)  # Call helper function to perform preorder traversal of the tree

                # Helper function to perform preorder traversal of a given tree/subtree
                def _preorder_traversal(self, current):
                    if current is not None:  # If tree/subtree is not empty
                        print(current.data, end=" ")  # Visit root (print its data)
                        self._preorder_traversal(current.left)  # Traverse left subtree
                        self._preorder_traversal(current.right)  # Traverse right subtree

                # Function to perform inorder traversal of the tree (traverse left subtree, visit root, traverse right subtree)
                def inorder_traversal(self):
                    if self.root is None:  # If tree is empty, print error message
                        print("Tree is empty.")
                    else:
                        print("Inorder Traversal:")  # Print traversal type message
                        self._inorder_traversal(
                            self.root)  # Call helper function to perform inorder traversal of the tree

                # Helper function to perform inorder traversal of a given tree/subtree
                def _inorder_traversal(self, current):
                    if current is not None:  # If tree/subtree is not empty
                        self._inorder_traversal(current.left)  # Traverse left subtree
                        print(current.data, end=" ")  # Visit root (print its data)
                        self._inorder_traversal(current.right)  # Traverse right subtree

                # Function to perform postorder traversal of the tree (traverse left subtree, traverse right subtree, visit root)
                def postorder_traversal(self):
                    if self.root is None:  # If tree is empty, print error message
                        print("Tree is empty.")
                    else:
                        print("Postorder Traversal:")  # Print traversal type message
                        self._postorder_traversal(
                            self.root)  # Call helper function to perform postorder traversal of the tree

                # Helper function to perform postorder traversal of a given tree/subtree
                def _postorder_traversal(self, current):
                    if current is not None:  # If tree/subtree is not empty
                        self._postorder_traversal(current.left)  # Traverse left subtree
                        self._postorder_traversal(current.right)  # Traverse right subtree
                        print(current.data, end=" ")  # Visit root (print its data)

                # Function to print the tree in inorder traversal order
                def print_tree(self):
                    print("Tree:", end=" ")  # Print tree label
                    if self.root is None:  # If tree is empty, print error message
                        print("Empty")
                    else:
                        self._print_tree(self.root)  # Call helper function to print the tree in inorder traversal order
                    print()  # Print newline

                # Helper function to print a given tree/subtree in inorder traversal order
                def _print_tree(self, current):
                    if current is not None:  # If tree/subtree is not empty
                        self._print_tree(current.left)  # Traverse left subtree
                        print(current.data, end=" ")  # Visit root (print its data)
                        self._print_tree(current.right)  # Traverse right subtree

            def create_tree():
                data_type = input("Enter data type of tree (int/str): ")

                if data_type == "int":
                    tree = Tree(int)
                elif data_type == "str":
                    tree = Tree(str)
                else:
                    print("Invalid data type. Exiting program.")
                    return None

                while True:
                    node = input("Enter node value (blank to stop adding nodes): ")
                    if node == "":
                        break

                    try:
                        tree.insert(node)
                    except ValueError:
                        print("Invalid input. Node value doesn't match the specified data type.")

                return tree

            def perform_operations(tree):
                while True:
                    print("\nChoose an operation:")
                    print("1. Insert a node")
                    print("2. Delete a node")
                    print("3. Search a node")
                    print("4. Preorder Traversal")
                    print("5. Inorder Traversal")
                    print("6. Postorder Traversal")
                    print("0. Back")

                    choice = input("Enter your choice: ")

                    if choice == "0":
                        TreeDs()

                    if choice == "1":
                        node = input("Enter the node value to insert: ")
                        try:
                            tree.insert(node)
                            print("Node inserted successfully.")
                        except ValueError:
                            print("Invalid input. Node value doesn't match the specified data type.")


                    elif choice == "2":
                        node = input("Enter the node value to delete: ")
                        try:
                            tree.delete(node)
                            print("Node deleted successfully.")
                        except ValueError:
                            print("Invalid input. Node value doesn't match the specified data type.")

                    elif choice == "3":
                        node = input("Enter the node value to search: ")
                        try:
                            result = tree.search(node)
                        except ValueError:
                            print("Invalid input. Node value doesn't match the specified data type.")

                    elif choice == "4":
                        tree.preorder_traversal()

                    elif choice == "5":
                        tree.inorder_traversal()

                    elif choice == "6":
                        tree.postorder_traversal()

                    else:
                        print("Invalid choice. Please try again.")

            def main():
                tree = create_tree()
                if tree:
                    perform_operations(tree)

            if __name__ == "__main__":
                main()
                TreeDs()
        elif tree_Choose == "4":
            def Tree_Types():
                types_choose = input(
                    "Select One: \n   1:Binary Tree \n   2:Binary Search Tree \n   3: AVl tree \n   4:Segment Tree \n   5:B- Tree \n   6: B+ Tree  \n   0:Back \n    Your choice: ")
                if types_choose == "2":
                    def Binary_Search_Tree():
                        BST_Choose = input(
                            "Select One:\n   1:Definitions \n   2:implementation And Operations \n   0:Back \n    Your Choice:' ")
                        if BST_Choose == "1":
                            print("""Binary Search Tree:\n
Binary search tree is a data structure that quickly allows us to maintain a sorted list of numbers.
It is called a binary tree because each tree node has a maximum of two children.
It is called a search tree because it can be used to search for the presence of a number in O(log(n)) time.
The properties that separate a binary search tree from a regular binary tree is
All nodes of left subtree are less than the root node
All nodes of right subtree are more than the root node
Both subtrees of each node are also BSTs i.e. they have the above two properties

    """)
                            Binary_Search_Tree()
                        elif BST_Choose == "2":
                            print("Implenetations and operations:")

                            class Node:
                                def __init__(self, data):
                                    self.data = data
                                    self.left = None
                                    self.right = None

                            def create_binary_search_tree(data_type):#Create A Tree Kinds
                                if data_type == 'int':
                                    root_data = int(input("Enter root node (integer): "))#Checking input types
                                    root = Node(root_data)
                                elif data_type == 'str':
                                    root_data = input("Enter root node (string): ")
                                    root = Node(root_data)
                                else:
                                    print("Invalid data type! Please choose 'int' or 'str'.")
                                    Binary_Search_Tree()

                                print("Binary Tree Created.")

                                while True:
                                    choice = input("Do you want to add more nodes? (y/n): ")#Asking if they want to continue
                                    if choice.lower() == 'n':
                                        break

                                    node_data = input("Enter node data: ")
                                    insert_node(root, node_data)

                                return root

                            def insert_node(root, data):#Function to insert a node
                                if root is None:
                                    return Node(data)

                                if data < str(root.data):
                                    root.left = insert_node(root.left, data)
                                else:
                                    root.right = insert_node(root.right, data)

                                return root

                            def delete_node(root, data):#Function to Delete a node
                                if root is None:
                                    return root

                                if data < str(root.data):
                                    root.left = delete_node(root.left, data)
                                elif data > str(root.data):
                                    root.right = delete_node(root.right, data)
                                else:
                                    if root.left is None:
                                        return root.right
                                    elif root.right is None:
                                        return root.left

                                    root.data = get_min_value(root.right)
                                    root.right = delete_node(root.right, root.data)

                                return root

                            def get_min_value(root):#Get the amin value 
                                while root.left is not None:
                                    root = root.left

                                return root.data

                            def search_node(root, data):#Function to search anode
                                if root is None or root.data == data:
                                    return root

                                if data < str(root.data):
                                    return search_node(root.left, data)
                                else:
                                    return search_node(root.right, data)

                            def display_tree(root):#Function to dispaly a Tree
                                if root is None:
                                    return

                                display_tree(root.left)
                                print(root.data)
                                display_tree(root.right)

                            def main():
                                data_type = input("Enter type of tree data (int or str): ")

                                try:
                                    root = create_binary_search_tree(data_type)

                                    while True:
                                        print("Operations:")
                                        print("1. Insert")
                                        print("2. Delete")
                                        print("3. Search")
                                        print("4. Display")
                                        print("0. Back")
                                        choice = int(input("Enter your choice (1-5): "))

                                        if choice == 1:
                                            node_data = input("Enter node data: ")
                                            root = insert_node(root, node_data)
                                            print("Node inserted.")
                                        elif choice == 2:
                                            node_data = input("Enter node data to delete: ")
                                            root = delete_node(root, node_data)
                                            print("Node deleted.")
                                        elif choice == 3:
                                            node_data = input("Enter node data to search: ")
                                            result = search_node(root, node_data)
                                            if result:
                                                print(f"Node {result.data} found.")
                                            else:
                                                print("Node not found.")
                                        elif choice == 4:
                                            print("Binary Search Tree:")
                                            display_tree(root)
                                        elif choice == 0:
                                            Tree_Types()
                                        else:
                                            print("Invalid choice! Please enter a valid choice.")
                                except ValueError as e:
                                    print(f"Value Error: {str(e)}")
                                    Binary_Search_Tree()

                            if __name__ == "__main__":
                                main()
                        elif BST_Choose == "0":
                            Tree_Types()
                        else:
                            print("Invalid Input!!!")
                            Binary_Search_Tree()

                    Binary_Search_Tree()
                elif types_choose == "1":
                    def Binary_Tree():
                        Binary_Choose = input(
                            "Select One:\n   1:Definitions \n   2:implementation And Operations \n   3: Types \n   0:Back\n    Your Choice:' ")
                        if Binary_Choose == "1":
                            print("""Binary Tree:\n
                    A tree where each node can have maximum two children, left and right children.
                    The maximum possible number of nodes at each level (k) of the binary tree is: (2k )  
                    The maximum possible number of nodes at height (h) can be: (2h+1  - 1)  
                    The minimum possible number of nodes at height (h) can be: (h+1)
                    """)
                            Binary_Tree()
                        elif Binary_Choose == "2":
                            print("Implenetations and operations:")

                            class Node:
                                def __init__(self, data):
                                    self.data = data
                                    self.left = None
                                    self.right = None
                            # A class for Binary Tree
                            class BinaryTree:
                                def __init__(self):
                                    self.root = None

                                def insert(self, value):#Function to insert a node
                                    if self.root is None:
                                        self.root = Node(value)
                                    else:
                                        self._insert_recursive(self.root, value)

                                def _insert_recursive(self, node, value):#Function to insert a node recursevily
                                    if value < node.data: 
                                        if node.left is None:
                                            node.left = Node(value)
                                        else:
                                            self._insert_recursive(node.left, value)
                                    else:
                                        if node.right is None:
                                            node.right = Node(value)
                                        else:
                                            self._insert_recursive(node.right, value)

                                def delete(self, value):#Function to delete a node
                                    self.root = self._delete_recursive(self.root, value)

                                def _delete_recursive(self, node, value):#Function to delete a node recursevily
                                    if node is None:
                                        return node

                                    if value < node.data:
                                        node.left = self._delete_recursive(node.left, value)
                                    elif value > node.data:
                                        node.right = self._delete_recursive(node.right, value)
                                    else:
                                        if node.left is None:
                                            return node.right
                                        elif node.right is None:
                                            return node.left
                                        else:
                                            min_value = self._find_min_value(node.right)
                                            node.data = min_value
                                            node.right = self._delete_recursive(node.right, min_value)

                                    return node

                                def _find_min_value(self, node):#Function to find MinValue
                                    current = node
                                    while current.left is not None:
                                        current = current.left
                                    return current.data

                                def search(self, value):#Function to search a node
                                    return self._search_recursive(self.root, value)

                                def _search_recursive(self, node, value):#Function to isearch  a node Recursevily
                                    if node is None or node.data == value:
                                        return node
                                    if value < node.data:
                                        return self._search_recursive(node.left, value)
                                    return self._search_recursive(node.right, value)

                                def display(self):#Function to display tree nodes
                                    self._display_recursive(self.root)

                                def _display_recursive(self, node):#Function to Dispaly a tree recursevily
                                    if node is not None:
                                        self._display_recursive(node.left)
                                        print(node.data)
                                        self._display_recursive(node.right)

                            def create_binary_tree():##Function to Create a Binary Tree
                                data_type = input("Enter the type of tree data (int or str): ")

                                while data_type not in ["int", "str"]:
                                    print("Invalid data type! Please enter either 'int' or 'str'.")
                                    data_type = input("Enter the type of tree data (int or str): ")

                                root_data = input("Enter the root node data: ")
                                if data_type == "int":
                                    try:
                                        root_data = int(root_data)
                                    except ValueError:
                                        print("Invalid value! Expected an integer.")
                                        return None
                                else:
                                    root_data = str(root_data)

                                binary_tree = BinaryTree()
                                binary_tree.insert(root_data)

                                print("Binary tree creation started...")
                                print("Enter 'stop' to finish creating the tree.")

                                while True:
                                    choice = input(
                                        "Enter 'L' to add a node as the left child or 'R' to add a node as the right child: ")

                                    if choice.lower() == "stop":
                                        break

                                    if choice not in ["l", "r"]:
                                        print("Invalid choice! Please enter either 'L' or 'R'.")
                                        continue

                                    node_data = input(f"Enter the {choice.upper()} node data: ")

                                    if data_type == "int":
                                        try:
                                            node_data = int(node_data)
                                        except ValueError:
                                            print("Invalid value! Expected an integer.")
                                            continue
                                    else:
                                        node_data = str(node_data)

                                    if choice.lower() == "l":
                                        binary_tree._insert_recursive(binary_tree.root, node_data)
                                    else:
                                        binary_tree._insert_recursive(binary_tree.root, node_data)

                                return binary_tree

                            def perform_operations(binary_tree):
                                while True:
                                    print("\nOPERATIONS")
                                    print("1. Insert a node")
                                    print("2. Delete a node")
                                    print("3. Search for a node")
                                    print("4. Display the binary tree")
                                    print("0. Back")

                                    choice = input("Enter your choice (1-5): ")

                                    if choice == "1":
                                        node_data = input("Enter the node data to insert: ")
                                        if isinstance(binary_tree.root.data, int):
                                            try:
                                                node_data = int(node_data)
                                            except ValueError:
                                                print("Invalid value! Expected an integer.")
                                                continue
                                        binary_tree.insert(node_data)
                                        print("Successfully inserted the node.")

                                    elif choice == "2":
                                        node_data = input("Enter the node data to delete: ")
                                        if isinstance(binary_tree.root.data, int):
                                            try:
                                                node_data = int(node_data)
                                            except ValueError:
                                                print("Invalid value! Expected an integer.")
                                                continue
                                        binary_tree.delete(node_data)
                                        print("Successfully deleted the node.")

                                    elif choice == "3":
                                        node_data = input("Enter the node data to search: ")
                                        if isinstance(binary_tree.root.data, int):
                                            try:
                                                node_data = int(node_data)
                                            except ValueError:
                                                print("Invalid value! Expected an integer.")
                                                continue
                                        result = binary_tree.search(node_data)
                                        if result is not None:
                                            print("Node found.")
                                        else:
                                            print("Node not found.")

                                    elif choice == "4":
                                        print("Binary Tree:")
                                        binary_tree.display()

                                    elif choice == "0":
                                        Binary_Tree()

                                    else:
                                        print("Invalid choice! Please enter a valid option (1-5).")

                            def main():
                                binary_tree = create_binary_tree()
                                if binary_tree is not None:
                                    perform_operations(binary_tree)

                            if __name__ == "__main__":
                                main()

                        elif Binary_Choose == "3":
                            pass
                        elif Binary_Choose == "0":
                            Tree_Types()
                        else:
                            print("Invalid Input!!!")
                            Binary_Tree()

                    Binary_Tree()
                elif types_choose == "3":
                    def AVL_Tree():
                        AVL_Choose = input(
                            "Select One:\n   1:Definitions \n   2:implementation And Operations \n   0:Back \n    Your Choice:' ")
                        if AVL_Choose == "1":
                            print("""AVL Tree:\n
AVL tree is named after inventors Adelson-Velsky and Landis 
It’s a self balancing binary search tree(BST), 
where the difference between heights of left and  right subtrees for any  node cannot be more than one.
The balance factor is:
 height of left subtree – height of the right subtree
And the difference should be {1,0,-1} """)
                            AVL_Tree()
                        elif AVL_Choose == "2":
                            print("Implementations and operations:")

                            # Node class for AVL tree
                            class Node:
                                def __init__(self, key):
                                    self.key = key
                                    self.left = None
                                    self.right = None
                                    self.height = 1

                            # AVL Tree class
                            class AVLTree:
                                def __init__(self):
                                    self.root = None

                                # Get the height of a node
                                def _get_height(self, node):
                                    if node is None:
                                        return 0
                                    return node.height

                                # Get the balance factor of a node
                                def _get_balance(self, node):
                                    if node is None:
                                        return 0
                                    return self._get_height(node.left) - self._get_height(node.right)

                                # Update the height of a node
                                def _update_height(self, node):
                                    if node is None:
                                        return
                                    node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

                                # Perform left rotation
                                def _left_rotate(self, z):
                                    y = z.right
                                    T2 = y.left

                                    y.left = z
                                    z.right = T2

                                    self._update_height(z)
                                    self._update_height(y)

                                    return y

                                # Perform right rotation
                                def _right_rotate(self, z):
                                    y = z.left
                                    T3 = y.right

                                    y.right = z
                                    z.left = T3

                                    self._update_height(z)
                                    self._update_height(y)

                                    return y

                                # Insert a node
                                def insert(self, key):
                                    def _insert_node(node, key):
                                        if node is None:
                                            return Node(key)
                                        elif key < node.key:
                                            node.left = _insert_node(node.left, key)
                                        else:
                                            node.right = _insert_node(node.right, key)

                                        self._update_height(node)

                                        balance = self._get_balance(node)

                                        # Left Left Case
                                        if balance > 1 and key < node.left.key:
                                            return self._right_rotate(node)

                                        # Right Right Case
                                        if balance < -1 and key > node.right.key:
                                            return self._left_rotate(node)

                                        # Left Right Case
                                        if balance > 1 and key > node.left.key:
                                            node.left = self._left_rotate(node.left)
                                            return self._right_rotate(node)

                                        # Right Left Case
                                        if balance < -1 and key < node.right.key:
                                            node.right = self._right_rotate(node.right)
                                            return self._left_rotate(node)

                                        return node

                                    self.root = _insert_node(self.root, key)

                                # Delete a node
                                def delete(self, key):
                                    def _delete_node(node, key):
                                        if node is None:
                                            return node

                                        if key < node.key:
                                            node.left = _delete_node(node.left, key)
                                        elif key > node.key:
                                            node.right = _delete_node(node.right, key)
                                        else:
                                            if node.left is None:
                                                temp = node.right
                                                node = None
                                                return temp
                                            elif node.right is None:
                                                temp = node.left
                                                node = None
                                                return temp
                                            else:
                                                temp = self._get_min_value_node(node.right)
                                                node.key = temp.key
                                                node.right = _delete_node(node.right, temp.key)

                                        self._update_height(node)
                                        balance = self._get_balance(node)

                                        # Left Left Case
                                        if balance > 1 and self._get_balance(node.left) >= 0:
                                            return self._right_rotate(node)

                                        # Left Right Case
                                        if balance > 1 and self._get_balance(node.left) < 0:
                                            node.left = self._left_rotate(node.left)
                                            return self._right_rotate(node)

                                        # Right Right Case
                                        if balance < -1 and self._get_balance(node.right) <= 0:
                                            return self._left_rotate(node)

                                        # Right Left Case
                                        if balance < -1 and self._get_balance(node.right) > 0:
                                            node.right = self._right_rotate(node.right)
                                            return self._left_rotate(node)

                                        return node

                                    self.root = _delete_node(self.root, key)

                                # Get the node with minimum value
                                def _get_min_value_node(self, node):
                                    if node is None or node.left is None:
                                        return node
                                    return self._get_min_value_node(node.left)

                                # Search for a node
                                def search(self, key):
                                    def _search_node(node, key):
                                        if node is None or node.key == key:
                                            return node

                                        if key < node.key:
                                            return _search_node(node.left, key)
                                        else:
                                            return _search_node(node.right, key)

                                    return _search_node(self.root, key)

                                # Display the AVL tree (inorder traversal)
                                def display(self, node):
                                    if node is None:
                                        return

                                    self.display(node.left)
                                    print(node.key, end=" ")
                                    self.display(node.right)

                            # Create an AVL tree with at least five nodes
                            avl_tree = AVLTree()

                            avl_tree.insert(9)
                            avl_tree.insert(5)
                            avl_tree.insert(10)
                            avl_tree.insert(0)
                            avl_tree.insert(6)

                            # Main program logic
                            while True:
                                print("\nAVL Tree Operations:")
                                print("1. Insert a node")
                                print("2. Delete a node")
                                print("3. Search for a node")
                                print("4. Display the tree")
                                print("0. Back")

                                choice = input("Enter your choice (1-5): ")

                                if choice == "1":
                                    try:
                                        key = int(input("Enter the key to be inserted: "))
                                        avl_tree.insert(key)
                                        print("Node inserted successfully!")
                                    except ValueError:
                                        print("Invalid input! Please enter an integer.")

                                elif choice == "2":
                                    try:
                                        key = int(input("Enter the key to be deleted: "))
                                        avl_tree.delete(key)
                                        print("Node deleted successfully!")
                                    except ValueError:
                                        print("Invalid input! Please enter an integer.")

                                elif choice == "3":
                                    try:
                                        key = int(input("Enter the key to search: "))
                                        result = avl_tree.search(key)
                                        if result:
                                            print("Node found!")
                                        else:
                                            print("Node not found!")
                                    except ValueError:
                                        print("Invalid input! Please enter an integer.")

                                elif choice == "4":
                                    print("Current AVL Tree:")
                                    avl_tree.display(avl_tree.root)

                                elif choice == "0":
                                    AVL_Tree()

                                else:
                                    print("Invalid choice! Please enter a valid option (1-5).")

                        elif AVL_Choose == "0":
                            Tree_Types()
                        else:
                            print("Invalid Input!!!")
                            AVL_Tree()

                    AVL_Tree()
                elif types_choose == "4":
                    def Segment_Tree():
                        Segment_Choose = input(
                            "Select One:\n   1:Definitions \n   2:implementation And Operations \n   0:Back \n   Your Choice:' ")
                        if Segment_Choose == "1":
                            print("""Segment Tree:\n
Segment tree, also known as interval tree or range tree, is a data structure used for efficient querying of intervals or ranges in an array.
It represents an array as a binary tree, where each node represents a range of elements in the array. 
The leaves of the tree correspond to individual elements of the array, and each internal node represents the union of the ranges of its child nodes. 
The main advantage of a segment tree: is that it allows for efficient query operations such as finding the sum, minimum, maximum, 
or any other associative operation on a given range of elements in the array. 
It achieves this by recursively dividing the array into smaller segments and precomputing useful information at each node,
 which can be used to answer queries efficiently. 
Segment trees are widely used:  in various applications, including range sum queries, 
range minimum or maximum queries, finding the number of elements less than or equal to a given value, and many others.

                        """)
                            Segment_Tree()
                        elif Segment_Choose == "2":
                            print("Implenetations and operations:")

                            class SegmentTree:
                                def __init__(self, arr):
                                    self.N = len(arr)  # Length of the input array
                                    self.tree = [0] * (4 * self.N)  # Segment tree represented as an array

                                    # Build the segment tree
                                    self.construct_tree(arr, 0, self.N - 1, 0)

                                def construct_tree(self, arr, low, high, pos):
                                    if low == high:
                                        self.tree[pos] = arr[low]
                                        return

                                    mid = (low + high) // 2
                                    self.construct_tree(arr, low, mid, 2 * pos + 1)
                                    self.construct_tree(arr, mid + 1, high, 2 * pos + 2)
                                    self.tree[pos] = self.tree[2 * pos + 1] + self.tree[2 * pos + 2]

                                def range_sum_query(self, qlow, qhigh, low, high, pos):
                                    if qlow <= low and qhigh >= high:  # Total overlap
                                        return self.tree[pos]

                                    if qlow > high or qhigh < low:  # No overlap
                                        return 0

                                    mid = (low + high) // 2
                                    return (self.range_sum_query(qlow, qhigh, low, mid, 2 * pos + 1) +
                                            self.range_sum_query(qlow, qhigh, mid + 1, high, 2 * pos + 2))

                                def range_min_query(self, qlow, qhigh, low, high, pos):
                                    if qlow <= low and qhigh >= high:  # Total overlap
                                        return self.tree[pos]

                                    if qlow > high or qhigh < low:  # No overlap
                                        return float('inf')

                                    mid = (low + high) // 2
                                    return min(self.range_min_query(qlow, qhigh, low, mid, 2 * pos + 1),
                                               self.range_min_query(qlow, qhigh, mid + 1, high, 2 * pos + 2))

                                def range_max_query(self, qlow, qhigh, low, high, pos):
                                    if qlow <= low and qhigh >= high:  # Total overlap
                                        return self.tree[pos]

                                    if qlow > high or qhigh < low:  # No overlap
                                        return float('-inf')

                                    mid = (low + high) // 2
                                    return max(self.range_max_query(qlow, qhigh, low, mid, 2 * pos + 1),
                                               self.range_max_query(qlow, qhigh, mid + 1, high, 2 * pos + 2))

                                def update(self, index, new_val, low, high, pos):
                                    if index < low or index > high:  # Out of range
                                        return

                                    if low == high:
                                        self.tree[pos] += new_val
                                        return

                                    mid = (low + high) // 2
                                    self.update(index, new_val, low, mid, 2 * pos + 1)
                                    self.update(index, new_val, mid + 1, high, 2 * pos + 2)
                                    self.tree[pos] = self.tree[2 * pos + 1] + self.tree[2 * pos + 2]

                                def print_tree(self):
                                    self.print_tree_recursive(0, self.N - 1, 0)

                                def print_tree_recursive(self, low, high, pos):
                                    if low == high:
                                        print(f"{self.tree[pos]}", end="")
                                        return

                                    mid = (low + high) // 2
                                    self.print_tree_recursive(low, mid, 2 * pos + 1)
                                    print(f" + {self.tree[pos]} + ", end="")
                                    self.print_tree_recursive(mid + 1, high, 2 * pos + 2)

                            # Example usage
                            try:
                                arr = [1, 3, 5, 7, 9, 11]
                                seg_tree = SegmentTree(arr)

                                # Printing the segment tree in a tree format
                                seg_tree.print_tree()
                                print()

                                # Operations menu
                                while True:
                                    print("Operations:")
                                    print("1. Range Sum Query")
                                    print("2. Range Minimum Query")
                                    print("3. Range Maximum Query")
                                    print("4. Update")
                                    print("0. Back")
                                    choice = int(input("Enter your choice (1, 2, 3, 4, or 0): "))

                                    if choice == 1:
                                        qlow = int(input("Enter the low index: "))
                                        qhigh = int(input("Enter the high index: "))
                                        print(f"Sum: {seg_tree.range_sum_query(qlow, qhigh, 0, seg_tree.N - 1, 0)}")
                                    elif choice == 2:
                                        qlow = int(input("Enter the low index: "))
                                        qhigh = int(input("Enter the high index: "))
                                        print(
                                            f"Minimum: {seg_tree.range_min_query(qlow, qhigh, 0, seg_tree.N - 1, 0)}")
                                    elif choice == 3:
                                        qlow = int(input("Enter the low index: "))
                                        qhigh = int(input("Enter the high index: "))
                                        print(
                                            f"Maximum: {seg_tree.range_max_query(qlow, qhigh, 0, seg_tree.N - 1, 0)}")
                                    elif choice == 4:
                                        index = int(input("Enter the index to update: "))
                                        new_val = int(input("Enter the value to add: "))
                                        seg_tree.update(index, new_val, 0, seg_tree.N - 1, 0)
                                        print("Segment tree updated successfully!")
                                    elif choice == 0:
                                        Segment_Tree()
                                    else:
                                        print("Invalid choice!")
                            except ValueError:
                                print("Invalid input. Please enter valid integers.")

                        elif Segment_Choose == "0":
                            Tree_Types()
                        else:
                            print("Invalid Input!!!")
                            Segment_Tree()

                    Segment_Tree()
                elif types_choose == "5":
                    def B_N_Tree():
                        B_N_Choose = input(
                            "Select One:\n   1:Definitions \n   2:implementation And Operations \n   0:Back \n   Your Choice:' ")
                        if B_N_Choose == "1":
                            print("""B- Tree:\n
A B-tree is a self-balancing data structure that maintains sorted data for efficient search, insertion, and deletion operations.
 It provides fast access times and efficient storage utilization by keeping the tree balanced through defined rules. 
 The B-tree is commonly used in file systems and databases to index and organize large amounts of data.
                                            """)
                            B_N_Tree()
                        elif B_N_Choose == "2":
                            print("Implenetations and operations:")

                            class BTreeNode:
                                def __init__(self, leaf=False):
                                    self.leaf = leaf
                                    self.keys = []
                                    self.child = []

                            class BTree:
                                def __init__(self, t):
                                    self.root = BTreeNode(True)
                                    self.t = t

                                def insert(self, k):
                                    root = self.root
                                    if len(root.keys) == (2 * self.t) - 1:
                                        temp = BTreeNode()
                                        self.root = temp
                                        temp.child.insert(0, root)
                                        self.split_child(temp, 0)
                                        self.insert_non_full(temp, k)
                                    else:
                                        self.insert_non_full(root, k)

                                def insert_non_full(self, x, k):
                                    i = len(x.keys) - 1
                                    if x.leaf:
                                        x.keys.append((None, None))
                                        while i >= 0 and k < x.keys[i]:
                                            x.keys[i + 1] = x.keys[i]
                                            i -= 1
                                        x.keys[i + 1] = k
                                    else:
                                        while i >= 0 and k < x.keys[i]:
                                            i -= 1
                                        i += 1
                                        if len(x.child[i].keys) == (2 * self.t) - 1:
                                            self.split_child(x, i)
                                            if k > x.keys[i]:
                                                i += 1
                                        self.insert_non_full(x.child[i], k)

                                def split_child(self, x, i):
                                    t = self.t
                                    y = x.child[i]
                                    z = BTreeNode(y.leaf)
                                    x.child.insert(i + 1, z)
                                    x.keys.insert(i, y.keys[t - 1])
                                    z.keys = y.keys[t:(2 * t) - 1]
                                    y.keys = y.keys[0:t - 1]
                                    if not y.leaf:
                                        z.child = y.child[t:(2 * t)]
                                        y.child = y.child[0:t - 1]

                                def delete(self, x, k):
                                    t = self.t
                                    i = 0
                                    while i < len(x.keys) and k > x.keys[i]:
                                        i += 1
                                    if x.leaf:
                                        if i < len(x.keys) and x.keys[i] == k:
                                            x.keys.pop(i)
                                            return
                                        return
                                    if i < len(x.keys) and x.keys[i] == k:
                                        return self.delete_internal_node(x, k, i)
                                    elif len(x.child[i].keys) >= t:
                                        self.delete(x.child[i], k)
                                    else:
                                        if i != 0 and i + 2 < len(x.child):
                                            if len(x.child[i - 1].keys) >= t:
                                                self.delete_sibling(x, i, i - 1)
                                            elif len(x.child[i + 1].keys) >= t:
                                                self.delete_sibling(x, i, i + 1)
                                            else:
                                                self.delete_merge(x, i, i + 1)
                                                self.delete(x.child[i], k)
                                        elif i == 0:
                                            if len(x.child[i + 1].keys) >= t:
                                                self.delete_sibling(x, i, i + 1)
                                            else:
                                                self.delete_merge(x, i, i + 1)
                                                self.delete(x.child[i], k)
                                        elif i + 1 == len(x.child):
                                            if len(x.child[i - 1].keys) >= t:
                                                self.delete_sibling(x, i, i - 1)
                                            else:
                                                self.delete_merge(x, i, i - 1)
                                                self.delete(x.child[i], k)
                                        else:
                                            return

                                def delete_internal_node(self, x, k, i):
                                    t = self.t
                                    if x.leaf:
                                        if x.keys[i] == k:
                                            x.keys.pop(i)
                                            return
                                        return
                                    if len(x.child[i].keys) >= t:
                                        x.keys[i] = self.delete_predecessor(x.child[i])
                                        return
                                    elif len(x.child[i + 1].keys) >= t:
                                        x.keys[i] = self.delete_successor(x.child[i + 1])
                                        return
                                    else:
                                        self.delete_merge(x, i, i + 1)
                                        self.delete_internal_node(x.child[i], k, self.t - 1)

                                def delete_predecessor(self, x):
                                    if x.leaf:
                                        return x.keys.pop()
                                    n = len(x.keys) - 1
                                    if len(x.child[n].keys) >= self.t:
                                        self.delete_sibling(x, n + 1, n)
                                    else:
                                        self.delete_merge(x, n, n + 1)
                                    return self.delete_predecessor(x.child[n])

                                def delete_successor(self, x):
                                    if x.leaf:
                                        return x.keys.pop(0)
                                    if len(x.child[1].keys) >= self.t:
                                        self.delete_sibling(x, 0, 1)
                                    else:
                                        self.delete_merge(x, 0, 1)
                                    return self.delete_successor(x.child[0])

                                def delete_merge(self, x, i, j):
                                    cnode = x.child[i]
                                    if j > i:
                                        rsnode = x.child[j]
                                        cnode.keys.append(x.keys[i])
                                        for k in range(rsnode.num_keys):
                                            cnode.keys.append(rsnode.keys[k])
                                            if len(rsnode.child) > 0:
                                                cnode.child.append(rsnode.child[k])
                                        if len(rsnode.child) > 0:
                                            cnode.child.append(rsnode.child.pop())
                                        new = cnode
                                        x.keys.pop(i)
                                        x.child.pop(j)
                                    else:
                                        lsnode = x.child[j]
                                        lsnode.keys.append(x.keys[j])
                                        for i in range(cnode.num_keys):
                                            lsnode.keys.append(cnode.keys[i])
                                            if len(lsnode.child) > 0:
                                                lsnode.child.append(cnode.child[i])
                                        if len(lsnode.child) > 0:
                                            lsnode.child.append(cnode.child.pop())
                                        new = lsnode
                                        x.keys.pop(j)
                                        x.child.pop(i)

                                    if x == self.root and len(x.keys) == 0:
                                        self.root = new

                                def delete_sibling(self, x, i, j):
                                    cnode = x.child[i]
                                    if i < j:
                                        rsnode = x.child[j]
                                        cnode.keys.append(x.keys[i])
                                        x.keys[i] = rsnode.keys[0]
                                        if len(rsnode.child) > 0:
                                            cnode.child.append(rsnode.child[0])
                                            rsnode.child.pop(0)
                                        rsnode.keys.pop(0)
                                    else:
                                        lsnode = x.child[j]
                                        cnode.keys.insert(0, x.keys[i - 1])
                                        x.keys[i - 1] = lsnode.keys.pop()
                                        if len(lsnode.child) > 0:
                                            cnode.child.insert(0, lsnode.child.pop())

                                def search_key(self, k, x=None):
                                    if x is not None:
                                        i = 0
                                        while i < len(x.keys) and k > x.keys[i]:
                                            i += 1
                                        if i < len(x.keys) and k == x.keys[i]:
                                            return True
                                        elif x.leaf:
                                            return False
                                        else:
                                            return self.search_key(k, x.child[i])
                                    else:
                                        return self.search_key(k, self.root)

                                def print_tree(self, x=None, l=0):
                                    if x is not None:
                                        print(f"Level {l}", end=": ")
                                        for i in range(len(x.keys)):
                                            print(x.keys[i], end=" ")
                                        print()
                                        l += 1
                                        if len(x.child) > 0:
                                            for i in range(len(x.child)):
                                                self.print_tree(x.child[i], l)

                                def display(self):
                                    self.print_tree(self.root)

                            def main():
                                try:
                                    t = int(input("Enter the minimum degree of the B-Tree: "))
                                    b_tree = BTree(t)
                                    values = input("Enter initial values (comma-separated): ").split(",")
                                    for value in values:
                                        b_tree.insert(int(value))
                                    print()
                                    b_tree.display()
                                    while True:
                                        print("\nChoose an operation:")
                                        print("1. Insert")
                                        print("2. Delete")
                                        print("3. Search")
                                        print("4. Display")
                                        print("0. Back")

                                        choice = int(input("Enter your choice: "))
                                        if choice == 1:
                                            value = int(input("Enter the value to insert: "))
                                            b_tree.insert(value)
                                            print("Insertion completed.")
                                        elif choice == 2:
                                            value = int(input("Enter the value to delete: "))
                                            b_tree.delete(b_tree.root, value)
                                            print("Deletion completed.")
                                        elif choice == 3:
                                            value = int(input("Enter the value to search: "))
                                            if b_tree.search_key(value):
                                                print("The value is found in the B-Tree.")
                                            else:
                                                print("The value is not found in the B-Tree.")
                                        elif choice == 4:
                                            b_tree.display()
                                        elif choice == 0:
                                            B_N_Tree()
                                        else:
                                            print("Invalid choice. Please try again.")

                                except ValueError:
                                    print("Please enter valid input values.")

                            if __name__ == "__main__":
                                main()


                        elif B_N_Choose == "0":
                            Tree_Types()
                        else:
                            print("Invalid Input!!!")
                            B_N_Tree()

                    B_N_Tree()
                elif types_choose == "6":
                    def B_P_Tree():
                        B_P_Choose = input(
                            "Select One:\n   1:Definitions \n   2:implementation And Operations \n   0:Back \n   Your Choice:' ")
                        if B_P_Choose == "1":
                            print("""B+ Tree:\n
B+ tree is a type of tree data structure that is commonly used in database systems and file systems.
 It is a variant of the B-tree, but with some modifications that make it more suitable for storing large amounts of data on disk. 
In a B+ tree, each internal node has multiple keys and pointers to child nodes, similar to a B-tree. 
However, in a B+ tree, all the data is stored in the leaf nodes, which are linked together in a linked list. 
This means that all the internal nodes are used only for indexing and do not store any data themselves.
The keys in a B+ tree are sorted in ascending order, which allows for efficient searching and range queries. 
The tree is also balanced, meaning that all leaf nodes are at the same level, 
which ensures that the height of the tree remains relatively small even for large datasets.
Overall, the B+ tree is a powerful data structure for storing and accessing large amounts of data efficiently, 
making it an ideal choice for use in database systems and file systems.
                                                                """)
                            B_P_Tree()
                        elif B_P_Choose == "2":
                            print("Implenetations and operations:")

                            class BPlusTree:
                                def __init__(self, degree):
                                    self.root = None
                                    self.degree = degree

                                def insert(self, key, value):
                                    if self.root is None:
                                        self.root = Node(True)
                                    if len(self.root.keys) == (2 * self.degree) - 1:
                                        new_root = Node()
                                        new_root.children.append(self.root)
                                        new_root.split_child(0)
                                        self.root = new_root
                                    self.root.insert_non_full(key, value)

                                def delete(self, key):
                                    if not self.root:
                                        print("B+Tree is empty!")
                                        return
                                    self.root.delete(key)

                                def search(self, key):
                                    if not self.root:
                                        print("B+Tree is empty!")
                                        return None
                                    return self.root.search(key)

                                def display(self):
                                    if not self.root:
                                        print("B+Tree is empty!")
                                    else:
                                        self.root.display()

                            class Node:
                                def __init__(self, leaf=False):
                                    self.leaf = leaf
                                    self.keys = []
                                    self.values = []
                                    self.children = []

                                def insert_non_full(self, key, value):
                                    i = len(self.keys) - 1
                                    if self.leaf:
                                        while i >= 0 and self.keys[i] > key:
                                            i -= 1
                                        self.keys.insert(i + 1, key)
                                        self.values.insert(i + 1, value)
                                    else:
                                        while i >= 0 and self.keys[i] > key:
                                            i -= 1
                                        if len(self.children[i + 1].keys) == (2 * BPlusTree.degree) - 1:
                                            self.split_child(i + 1)
                                            if self.keys[i + 1] < key:
                                                i += 1
                                        self.children[i + 1].insert_non_full(key, value)

                                def split_child(self, index):
                                    y = self.children[index]
                                    new_node = Node(y.leaf)
                                    self.keys.insert(index, y.keys[BPlusTree.degree - 1])
                                    self.values.insert(index, y.values[BPlusTree.degree - 1])
                                    self.children.insert(index + 1, new_node)
                                    new_node.keys = y.keys[BPlusTree.degree:]
                                    new_node.values = y.values[BPlusTree.degree:]
                                    y.keys = y.keys[:BPlusTree.degree - 1]
                                    y.values = y.values[:BPlusTree.degree - 1]
                                    if not y.leaf:
                                        new_node.children = y.children[BPlusTree.degree:]
                                        y.children = y.children[:BPlusTree.degree]

                                def delete(self, key):
                                    i = 0
                                    while i < len(self.keys) and key > self.keys[i]:
                                        i += 1
                                    if self.leaf:
                                        if i < len(self.keys) and self.keys[i] == key:
                                            self.keys.pop(i)
                                            self.values.pop(i)
                                        else:
                                            print("Key not found!")
                                            return
                                    else:
                                        if i < len(self.keys) and self.keys[i] == key:
                                            self.delete_internal_node(i)
                                        else:
                                            if len(self.children[i].keys) < BPlusTree.degree:
                                                self.fill_internal_node(i)
                                            if i >= len(self.keys) or key > self.keys[i]:
                                                i += 1
                                            self.children[i].delete(key)

                                def delete_internal_node(self, index):
                                    key = self.keys[index]
                                    if self.children[index].leaf:
                                        if index == 0:
                                            self.merge_leaf_nodes(index, index + 1)
                                        else:
                                            self.merge_leaf_nodes(index - 1, index)
                                    else:
                                        if len(self.children[index].keys) >= BPlusTree.degree:
                                            predecessor = self.get_predecessor(index)
                                            self.keys[index] = predecessor
                                            self.children[index].delete(predecessor)
                                        else:
                                            if len(self.children[index + 1].keys) >= BPlusTree.degree:
                                                successor = self.get_successor(index)
                                                self.keys[index] = successor
                                                self.children[index + 1].delete(successor)
                                            else:
                                                self.merge_internal_nodes(index, index + 1)

                                def merge_leaf_nodes(self, left_index, right_index):
                                    left_node = self.children[left_index]
                                    right_node = self.children[right_index]
                                    left_node.keys.extend(right_node.keys)
                                    left_node.values.extend(right_node.values)
                                    if right_index < len(self.keys):
                                        self.keys.pop(right_index)
                                    self.children.pop(right_index)

                                def merge_internal_nodes(self, left_index, right_index):
                                    left_node = self.children[left_index]
                                    right_node = self.children[right_index]
                                    left_node.keys.append(self.keys[left_index])
                                    left_node.keys.extend(right_node.keys)
                                    left_node.children.extend(right_node.children)
                                    if right_index < len(self.keys):
                                        self.keys.pop(right_index)
                                    self.children.pop(right_index + 1)

                                def fill_internal_node(self, index):
                                    if index != 0 and len(self.children[index - 1].keys) >= BPlusTree.degree:
                                        self.borrow_from_left_sibling(index)
                                    elif index != len(self.keys) and len(
                                            self.children[index + 1].keys) >= BPlusTree.degree:
                                        self.borrow_from_right_sibling(index)
                                    else:
                                        if index != len(self.keys):
                                            self.merge_internal_nodes(index, index + 1)
                                        else:
                                            self.merge_internal_nodes(index - 1, index)

                                def borrow_from_left_sibling(self, index):
                                    child = self.children[index]
                                    sibling = self.children[index - 1]
                                    child.keys.insert(0, self.keys[index - 1])
                                    child.children.insert(0, sibling.children.pop())
                                    self.keys[index - 1] = sibling.keys.pop()

                                def borrow_from_right_sibling(self, index):
                                    child = self.children[index]
                                    sibling = self.children[index + 1]
                                    child.keys.append(self.keys[index])
                                    child.children.append(sibling.children.pop(0))
                                    self.keys[index] = sibling.keys.pop(0)

                                def get_predecessor(self, index):
                                    current = self.children[index]
                                    while not current.leaf:
                                        current = current.children[-1]
                                    return current.keys[-1]

                                def get_successor(self, index):
                                    current = self.children[index + 1]
                                    while not current.leaf:
                                        current = current.children[0]
                                    return current.keys[0]

                                def search(self, key):
                                    i = 0
                                    while i < len(self.keys) and key > self.keys[i]:
                                        i += 1
                                    if i < len(self.keys) and self.keys[i] == key:
                                        return self.values[i]
                                    elif self.leaf:
                                        return None
                                    else:
                                        return self.children[i].search(key)

                                def display(self):
                                    queue = [self]
                                    while len(queue) > 0:
                                        current_level = []
                                        next_level = []
                                        for node in queue:
                                            current_level.append(f"{str(node.keys)} | ")
                                            if not node.leaf:
                                                next_level.extend(node.children)
                                        print("".join(current_level))
                                        queue = next_level

                            BPlusTree.degree = int(input("Enter the degree of the B+ tree: "))
                            bptree = BPlusTree(BPlusTree.degree)

                            while True:
                                print("\n1. Insert")
                                print("2. Delete")
                                print("3. Search")
                                print("4. Display")
                                print("0. Back")
                                choice = int(input("Enter your choice: "))

                                if choice == 1:
                                    try:
                                        key = int(input("Enter the key to insert: "))
                                        value = input("Enter the value to insert: ")
                                        bptree.insert(key, value)
                                        print("Key inserted successfully!")
                                    except ValueError:
                                        print("Invalid input!")

                                elif choice == 2:
                                    try:
                                        key = int(input("Enter the key to delete: "))
                                        bptree.delete(key)
                                        print("Key deleted successfully!")
                                    except ValueError:
                                        print("Invalid input!")

                                elif choice == 3:
                                    try:
                                        key = int(input("Enter the key to search: "))
                                        result = bptree.search(key)
                                        if result:
                                            print("Value:", result)
                                        else:
                                            print("Key not found!")
                                    except ValueError:
                                        print("Invalid input!")

                                elif choice == 4:
                                    print("B+Tree:")
                                    bptree.display()

                                elif choice == 0:
                                    B_P_Tree()

                                else:
                                    print("Invalid choice!")




                        elif B_P_Choose == "0":
                            Tree_Types()
                        else:
                            print("Invalid Input!!!")
                            B_P_Tree()

                    B_P_Tree()
                elif types_choose == "7":
                    pass
                elif types_choose == "8":
                    pass
                elif types_choose == "0":
                    TreeDs()
                else:
                    print("Invalid Input!!!")
                    Tree_Types()

            Tree_Types()

        elif tree_Choose == "0":
            data_structure()
        else:
            print("invalid Input!!!")
            TreeDs()
#+++++++++++++++++++++++++++++++++End Of TreeDs++++++++++++++++++++++++++++++
    import os
    def Graph():
        Graph_Choose = input(
            "Select One Option: \n   1.Definition of Graph  \n   2.terminology of Graph \n   3.implemention of Graph \n   4.kinds of Graph  \n   5.tervalsal of Graph  \n   0.Main Menu \n    Your Choice : ")
        if Graph_Choose == "0":
            clear = lambda: os.system('cls')
            clear()
            data_structure()
        elif Graph_Choose == "1":
            print("welcome to the definiton part\n")
            print("""definition: \n             Graph data structures are a powerful tool for representing and analyzing complex relationships between objects or entities.
        They are particularly useful in fields such as social network analysis, recommendation systems, and computer networks.
        In the field of sports data science, graph data structures can be used to analyze and understand the dynamics of team performance and player interactions on the field.""")
            print("_______________________________________________")
            Graph()
        elif Graph_Choose == "2":
            print("terminology of Graph")

            def terminology():
                Term_choose = input(
                    """Select One: \n   1.Overview \n   2.Definitions: Graph, Vertices, Edges   \n   3.Application  \n    4.Graph Classifications  \n   5.Kinds of Graphs: Weighted and Unweighted  \n   6.Kinds of Graphs: Directed and Undirected \n   0.back \n    Your Choice : """)
                if Term_choose == "1":
                    print("Overview")
                    print("""Definitions: Vertices, edges, paths, etc""")
                    print("""Representations: Adjacency list and adjacency matrix""")
                    print("_______________________________________________")
                    terminology()
                elif Term_choose == "2":
                    print("Definitions: Graph, Vertices, Edges")
                    print("""Define a graph G = (V, E) by defining a pair of sets:
        V = a set of vertices
        E = a set of edges

        Edges:
        Each edge is defined by a pair of vertices
        An edge connects the vertices that define it
        In some cases, the vertices can be the same

        Vertices:
        Vertices also called nodes
        Denote vertices with labels

        Representation:
        Represent vertices with circles, perhaps containing a label
        Represent edges with lines between circles

        Example:
        V = {A,B,C,D}
        E = {(A,B),(A,C),(A,D),(B,D),(C,D)}""")
                    print("_______________________________________________")
                    terminology()
                elif Term_choose == "3":
                    print("Applications")
                    print("""Many algorithms use a graph representation to represent data or the problem to be solved

        Examples:
        Cities with distances between
        Roads with distances between intersection points
        Course prerequisites
        Network
        Social networks
        Program call graph and variable dependency graph""")
                    print("_______________________________________________")
                    terminology()
                elif Term_choose == "4":
                    print("Graph Classifications")
                    print("""There are seveal common kinds of graphs
        Weighted or unweighted
        Directed or undirected
        Cyclic or acyclic

        Choose the kind required for problem and determined by data

        We examine each below""")
                    print("_______________________________________________")
                    terminology()
                elif Term_choose == "5":
                    print("Kinds of Graphs: Weighted and Unweighted")
                    print("""Graphs can be classified by whether or not their edges have weights

        Weighted graph: edges have a weight

        Weight typically shows cost of traversing
        Example: weights are distances between cities

        Unweighted graph: edges have no weight

        Edges simply show connections
        Example: course prereqs""")
                    print("_______________________________________________")
                    terminology()
                elif Term_choose == "6":
                    print("Kinds of Graphs: Directed and Undirected")
                    print("""Graphs can be classified by whether or their edges are have direction

        Undirected Graphs: each edge can be traversed in either direction

        Directed Graphs: each edge can be traversed only in a specified direction""")
                    print("_______________________________________________")
                    terminology()
                elif Term_choose == "0":
                    clear = lambda: os.system('cls')
                    clear()
                    Graph()
                else:
                    print("insert correct number")
                    terminology()

            terminology()
        elif Graph_Choose == "3":
            print("implemention of Graph")

            def implemention():
                Implement_choose = input(
                    "Select one: \n   1.Adjacency Matrix \n   2.Adjacency List  \n    0.back  \n    3. Your Choice:   ")
                if Implement_choose == "1":
                    print("Adjacency Matrix")

                    # Function to create an adjacency matrix
                    def create_adjacency_matrix(num_vertices):
                        try:
                            # Initialize an empty adjacency matrix
                            adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
                            for i in range(num_vertices):
                                print(f"Enter the connections for vertex {i + 1} (separated by spaces):")
                                # Get the connections for each vertex
                                connections = list(map(int, input().split()))
                                for j in connections:
                                    # Check if the connection is valid
                                    if j > num_vertices or j < 1:
                                        print("Invalid connection. Please try again.")
                                        return None
                                    # Add the connection to the adjacency matrix
                                    adjacency_matrix[i][j - 1] = 1

                            return adjacency_matrix
                        except Exception as e:
                            print(f"An error occurred: {str(e)}")

                    # Function to print an adjacency matrix
                    def print_adjacency_matrix(adjacency_matrix):
                        try:
                            num_vertices = len(adjacency_matrix)

                            print("Adjacency Matrix:")
                            print("   ", end="")
                            for i in range(num_vertices):
                                print(f"{i + 1} ", end="")
                            print()
                            for i in range(num_vertices):
                                print(f"{i + 1}: ", end="")
                                for j in range(num_vertices):
                                    print(f"{adjacency_matrix[i][j]} ", end="")
                                print()
                        except Exception as e:
                            print(f"An error occurred: {str(e)}")

                    if __name__ == "__main__":
                        try:
                            num_vertices = int(input("Enter the number of vertices: "))
                            adjacency_matrix = create_adjacency_matrix(num_vertices)

                            if adjacency_matrix is not None:
                                print_adjacency_matrix(adjacency_matrix)
                        except Exception as e:
                            print(f"An error occurred: {str(e)}")

                            implemention()
                elif Implement_choose == "2":
                    print("Adjacency List")

                    # Initialize an empty adjacency list
                    def init_adj_list():
                        return {}

                    # Function to add a vertex to the adjacency list
                    def add_vertex(adj_list, vertex):
                        if vertex not in adj_list:
                            adj_list[vertex] = []

                    # Function to add an edge to the adjacency list
                    def add_edge(adj_list, vertex1, vertex2):
                        if vertex1 in adj_list and vertex2 in adj_list:
                            adj_list[vertex1].append(vertex2)
                            adj_list[vertex2].append(vertex1)

                    # Function to print the adjacency list
                    def print_adjacency_list(adj_list):
                        for vertex in adj_list:
                            print(f"{vertex} -> {', '.join(str(v) for v in adj_list[vertex])}")

                    # Main function to interact with the user and perform operations on the adjacency list
                    def main():
                        try:
                            # Initialize an empty adjacency list
                            adj_list = init_adj_list()

                            # Ask the user for the number of vertices
                            num_vertices = int(input("Enter the number of vertices: "))

                            # Add each vertex to the adjacency list
                            for i in range(num_vertices):
                                value = input(f"Enter value for Vertex {i + 1}: ")
                                add_vertex(adj_list, value)

                            # Ask the user for the number of edges
                            num_edges = int(input("Enter the number of edges: "))

                            # Add each edge to the adjacency list
                            for i in range(num_edges):
                                edge = input(f"Enter vertices for Edge {i + 1} (separated by space): ")
                                v1, v2 = edge.split()
                                add_edge(adj_list, v1, v2)

                            # Print the adjacency list
                            print("\nAdjacency List:")
                            print_adjacency_list(adj_list)
                        except Exception as e:
                            print(f"An error occurred: {str(e)}")

                    if __name__ == "__main__":
                        main()

                    implemention()
                elif Implement_choose == "0":
                    import os
                    clear = lambda: os.system('cls')
                    clear()
                    Graph()
                else:
                    print("Invalid Input, choose the correct number")
                    implemention()

            implemention()
        elif Graph_Choose == "4":
            print("kinds of Graph")

            def kinds():
                Kinds_Choose = input(
                    "Select One:\n1:Undirected Graphs\n 2:Directed Graphs\n 3:Weighted Graphs\n 4:Unweighted Graphs\n 5:Complete Graphs\n 0:back\n Your Choice : ")
                if Kinds_Choose == "0":
                    import os
                    clear = lambda: os.system('cls')
                    clear()
                    Graph()
                if Kinds_Choose == "1":
                    print("Undirected Graphs")
                    print(
                        "A graph in which edges have no direction, i.e., the edges do not have arrows indicating the direction of traversal")

                    def U_Operations():
                        U_Operation_choose = input(
                            "Select One: \n   1.insert \n   2.delete \n   3.search \n   0:Back\n  Your Choice: ")
                        if U_Operation_choose == "1":
                            print("insertion in Undirected Graphs ")

                            class Graph:
                                def __init__(self):
                                    # Initialize an empty dictionary to store the graph
                                    self.graph = {}

                                def add_edge(self, u, v):
                                    try:
                                        # Add an edge to the graph
                                        if u not in self.graph:
                                            # If vertex u is not in the graph, add it with an empty adjacency list
                                            self.graph[u] = []
                                        if v not in self.graph:
                                            # If vertex v is not in the graph, add it with an empty adjacency list
                                            self.graph[v] = []

                                        # Add vertex v to the adjacency list of vertex u and vice versa
                                        self.graph[u].append(v)
                                        self.graph[v].append(u)
                                    except Exception as e:
                                        print(f"An error occurred while adding an edge: {e}")

                                def print_graph(self):
                                    try:
                                        # Print the adjacency list of each vertex
                                        for vertex in self.graph:
                                            print(f"Adjacency list of vertex {vertex}: ", end="")
                                            for neighbor in self.graph[vertex]:
                                                print(f"{neighbor} -> ", end="")
                                            print("None")
                                    except Exception as e:
                                        print(f"An error occurred while printing the graph: {e}")

                            try:
                                graph = Graph()
                                num_edges = int(input("Enter the number of edges: "))
                                for _ in range(num_edges):
                                    u, v = map(int, input("Enter an edge (u v): ").split())
                                    graph.add_edge(u, v)
                                graph.print_graph()
                            except Exception as e:
                                print(f"An error occurred: {e}")

                            U_Operations()
                        elif U_Operation_choose == "2":
                            print("deleltion in Undirected Graphs")

                            class Graph:
                                def __init__(self, vertices):
                                    # Initialize the number of vertices and the adjacency list
                                    self.V = vertices
                                    self.adj_list = [[] for _ in range(vertices)]

                                def add_edge(self, u, v):
                                    try:
                                        # Add an edge to the graph
                                        self.adj_list[u].append(v)
                                        self.adj_list[v].append(u)
                                    except Exception as e:
                                        print(f"An error occurred while adding an edge: {e}")

                                def delete_edge(self, u, v):
                                    try:
                                        # Delete an edge from the graph
                                        if v in self.adj_list[u]:
                                            self.adj_list[u].remove(v)
                                            self.adj_list[v].remove(u)
                                            print("Edge ({}, {}) has been deleted.".format(u, v))
                                        else:
                                            print("Edge ({}, {}) does not exist.".format(u, v))
                                    except Exception as e:
                                        print(f"An error occurred while deleting an edge: {e}")

                                def print_graph(self):
                                    try:
                                        # Print the adjacency list of each vertex
                                        for i in range(self.V):
                                            print("Adjacency list of vertex {}: ".format(i), end="")
                                            for j in self.adj_list[i]:
                                                print(j, end=" ")
                                            print()
                                    except Exception as e:
                                        print(f"An error occurred while printing the graph: {e}")

                            try:
                                V = int(input("Enter the number of vertices: "))
                                graph = Graph(V)
                                E = int(input("Enter the number of edges: "))
                                for _ in range(E):
                                    u, v = map(int, input("Enter edge (u,v): ").split())
                                    graph.add_edge(u, v)
                                print("\nInitial Graph:")
                                graph.print_graph()
                                u, v = map(int, input("\nEnter edge to delete (u,v): ").split())
                                graph.delete_edge(u, v)
                                print("\nUpdated Graph:")
                                graph.print_graph()
                            except Exception as e:
                                print(f"An error occurred: {e}")

                            U_Operations()
                        elif U_Operation_choose == "3":
                            print("searching in Undirected Graphs")

                            class Graph:
                                def __init__(self, vertices):
                                    # Initialize the number of vertices and the adjacency list
                                    self.V = vertices
                                    self.adj_list = [[] for _ in range(vertices)]

                                def add_edge(self, u, v):
                                    try:
                                        # Add an edge to the graph
                                        self.adj_list[u].append(v)
                                        self.adj_list[v].append(u)
                                    except Exception as e:
                                        print(f"An error occurred while adding an edge: {e}")

                                def search(self, start, target):
                                    try:
                                        # Search for a path from start to target
                                        visited = [False] * self.V
                                        queue = []
                                        path = []

                                        queue.append(start)
                                        visited[start] = True

                                        while queue:
                                            current_vertex = queue.pop(0)
                                            path.append(current_vertex)

                                            if current_vertex == target:
                                                return path

                                            for neighbor in self.adj_list[current_vertex]:
                                                if not visited[neighbor]:
                                                    queue.append(neighbor)
                                                    visited[neighbor] = True

                                        return None
                                    except Exception as e:
                                        print(f"An error occurred during the search: {e}")

                            try:
                                g = Graph(6)
                                g.add_edge(0, 1)
                                g.add_edge(0, 2)
                                g.add_edge(1, 3)
                                g.add_edge(2, 4)
                                g.add_edge(3, 5)
                                start_vertex = int(input("Enter the starting vertex: "))
                                target_vertex = int(input("Enter the target vertex: "))
                                result_path = g.search(start_vertex, target_vertex)

                                if result_path is None:
                                    print("No path found.")
                                else:
                                    print("Path:", result_path)
                            except Exception as e:
                                print(f"An error occurred: {e}")

                                U_Operations()
                        elif U_Operation_choose == "0":
                            import os
                            clear = lambda: os.system('cls')
                            clear()
                            kinds()
                        else:
                            print("Invalid Input!!")
                            U_Operations()

                    U_Operations()
                elif Kinds_Choose == "2":
                    print("Directed Graphs")
                    print("A directed graph, also called a digraph, is a graph in which the edges have a direction")

                    def D_Operations():
                        D_Operation_Choose = input(
                            "Select One: \n   1.insert \n   2.delete \n   3.search \n  0:Back  Your Choice: ")
                        if D_Operation_Choose == "0":
                            import os
                            clear = lambda: os.system('cls')
                            clear()
                            kinds()
                        if D_Operation_Choose == "1":
                            print("insertion in Directed Graphs")

                            class Graph:
                                def __init__(self):
                                    # Initialize an empty dictionary to store the graph
                                    self.graph = {}

                                def add_vertex(self, vertex):
                                    try:
                                        # Add a vertex to the graph
                                        if vertex not in self.graph:
                                            self.graph[vertex] = []
                                    except Exception as e:
                                        print(f"An error occurred while adding a vertex: {e}")

                                def add_edge(self, start_vertex, end_vertex):
                                    try:
                                        # Add an edge to the graph
                                        if start_vertex in self.graph:
                                            self.graph[start_vertex].append(end_vertex)
                                        else:
                                            print("Start vertex does not exist.")
                                    except Exception as e:
                                        print(f"An error occurred while adding an edge: {e}")

                                def display_graph(self):
                                    try:
                                        # Display the graph
                                        for vertex in self.graph:
                                            print(vertex, "->", " -> ".join(self.graph[vertex]))
                                    except Exception as e:
                                        print(f"An error occurred while displaying the graph: {e}")

                            try:
                                graph = Graph()
                                num_vertices = int(input("Enter the number of vertices: "))
                                for i in range(num_vertices):
                                    vertex = input("Enter a vertex: ")
                                    graph.add_vertex(vertex)
                                num_edges = int(input("Enter the number of edges: "))
                                for i in range(num_edges):
                                    start_vertex = input("Enter a start vertex: ")
                                    end_vertex = input("Enter an end vertex: ")
                                    graph.add_edge(start_vertex, end_vertex)
                                print("\nGraph:")
                                graph.display_graph()
                            except Exception as e:
                                print(f"An error occurred: {e}")

                            D_Operations()
                        elif D_Operation_Choose == "2":
                            print("deletion in Directed Graphs")

                            class Graph:
                                def __init__(self, vertices):
                                    # Initialize the number of vertices and the adjacency list
                                    self.V = vertices
                                    self.adj_list = [[] for _ in range(vertices)]

                                def add_edge(self, u, v):
                                    try:
                                        # Add an edge to the graph
                                        self.adj_list[u].append(v)
                                    except Exception as e:
                                        print(f"An error occurred while adding an edge: {e}")

                                def delete_edge(self, u, v):
                                    try:
                                        # Delete an edge from the graph
                                        if v in self.adj_list[u]:
                                            self.adj_list[u].remove(v)
                                            print("Edge deleted successfully.")
                                        else:
                                            print("Edge does not exist.")
                                    except Exception as e:
                                        print(f"An error occurred while deleting an edge: {e}")

                                def print_graph(self):
                                    try:
                                        # Print the adjacency list of each vertex
                                        for i in range(self.V):
                                            print("Adjacency list of vertex", i)
                                            print(" -> ".join(map(str, self.adj_list[i])))
                                    except Exception as e:
                                        print(f"An error occurred while printing the graph: {e}")

                            try:
                                V = int(input("Enter the number of vertices: "))
                                graph = Graph(V)
                                E = int(input("Enter the number of edges: "))
                                for _ in range(E):
                                    u, v = map(int, input("Enter edge (u v): ").split())
                                    graph.add_edge(u, v)
                                print("\nInitial Graph:")
                                graph.print_graph()
                                u, v = map(int, input("\nEnter edge to delete (u v): ").split())
                                graph.delete_edge(u, v)
                                print("\nUpdated Graph:")
                                graph.print_graph()
                            except Exception as e:
                                print(f"An error occurred: {e}")

                            D_Operations()
                        elif D_Operations() == "3":
                            print("searching in Directed Graphs")

                            class Graph:
                                def __init__(self):
                                    # Initialize an empty dictionary to store the graph
                                    self.graph = {}

                                def add_vertex(self, vertex):
                                    try:
                                        # Add a vertex to the graph
                                        if vertex not in self.graph:
                                            self.graph[vertex] = []
                                    except Exception as e:
                                        print(f"An error occurred while adding a vertex: {e}")

                                def add_edge(self, start_vertex, end_vertex):
                                    try:
                                        # Add an edge to the graph
                                        if start_vertex in self.graph:
                                            self.graph[start_vertex].append(end_vertex)
                                        else:
                                            print("Start vertex does not exist.")
                                    except Exception as e:
                                        print(f"An error occurred while adding an edge: {e}")

                                def display_graph(self):
                                    try:
                                        # Display the graph
                                        for vertex in self.graph:
                                            print(vertex, "->", " -> ".join(self.graph[vertex]))
                                    except Exception as e:
                                        print(f"An error occurred while displaying the graph: {e}")

                            try:
                                graph = Graph()
                                num_vertices = int(input("Enter the number of vertices: "))
                                for i in range(num_vertices):
                                    vertex = input("Enter a vertex: ")
                                    graph.add_vertex(vertex)
                                num_edges = int(input("Enter the number of edges: "))
                                for i in range(num_edges):
                                    start_vertex = input("Enter a start vertex: ")
                                    end_vertex = input("Enter an end vertex: ")
                                    graph.add_edge(start_vertex, end_vertex)
                                print("\nGraph:")
                                graph.display_graph()
                            except Exception as e:
                                print(f"An error occurred: {e}")

                    D_Operations()

                elif Kinds_Choose == "3":

                    print("Weighted Graphs")
                    print(
                        "Weighted graphs are the graph in Data Structure in which the edges are given some weight or value based on the type of graph we are representing")

                    def W_Operations():
                        W_Operation_Choose = input(
                            "Select One: \n   1.insert \n   2.delete \n   3.search\n   0:Back \n    Your Choice: ")
                        if W_Operation_Choose == "0":
                            import os
                            clear = lambda: os.system('cls')
                            clear()
                            kinds()
                        elif W_Operation_Choose == "1":
                            print("insertion")

                            class WeightedGraph:
                                def __init__(self):
                                    # Initialize an empty dictionary to store the graph
                                    self.graph = {}

                                def add_edge(self, u, v, weight):
                                    try:
                                        # Add a weighted edge to the graph
                                        if u not in self.graph:
                                            self.graph[u] = []
                                        self.graph[u].append((v, weight))
                                    except Exception as e:
                                        print(f"An error occurred while adding an edge: {e}")

                                def insert_operation(self):
                                    try:
                                        # Insert an operation into the graph
                                        u = input("Enter the source vertex: ")
                                        v = input("Enter the destination vertex: ")
                                        weight = float(input("Enter the weight of the edge: "))

                                        self.add_edge(u, v, weight)
                                        print("Edge inserted successfully!")
                                    except Exception as e:
                                        print(f"An error occurred during the insert operation: {e}")

                            try:
                                graph = WeightedGraph()
                                graph.insert_operation()
                            except Exception as e:
                                print(f"An error occurred: {e}")

                            W_Operations()
                        elif W_Operation_Choose == "2":
                            print("deletion")

                            class Graph:
                                def __init__(self, vertices):
                                    # Initialize the number of vertices and the adjacency matrix
                                    self.V = vertices
                                    self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

                                def add_edge(self, u, v, weight):
                                    try:
                                        # Add a weighted edge to the graph
                                        self.graph[u][v] = weight
                                    except Exception as e:
                                        print(f"An error occurred while adding an edge: {e}")

                                def delete_edge(self, u, v):
                                    try:
                                        # Delete an edge from the graph
                                        if u < 0 or u >= self.V or v < 0 or v >= self.V:
                                            print("Invalid edge")
                                            return

                                        if self.graph[u][v] == 0:
                                            print("Edge does not exist")
                                            return

                                        self.graph[u][v] = 0
                                    except Exception as e:
                                        print(f"An error occurred while deleting an edge: {e}")

                                def print_graph(self):
                                    try:
                                        # Print the adjacency matrix of the graph
                                        for i in range(self.V):
                                            for j in range(self.V):
                                                if self.graph[i][j] != 0:
                                                    print(f"Edge from {i} to {j} with weight {self.graph[i][j]}")
                                    except Exception as e:
                                        print(f"An error occurred while printing the graph: {e}")

                            try:
                                V = int(input("Enter the number of vertices: "))
                                g = Graph(V)
                                E = int(input("Enter the number of edges: "))
                                for _ in range(E):
                                    u, v, weight = map(int, input("Enter edge (u v weight): ").split())
                                    g.add_edge(u, v, weight)
                                print("Initial Graph:")
                                g.print_graph()
                                u = int(input("Enter source vertex of the edge to delete: "))
                                v = int(input("Enter destination vertex of the edge to delete: "))
                                g.delete_edge(u, v)
                                print("\nUpdated Graph:")
                                g.print_graph()
                            except Exception as e:
                                print(f"An error occurred: {e}")

                            W_Operations()

                        elif W_Operation_Choose == "3":
                            print("searching")
                            import heapq

                            def dijkstra(graph, start):
                                try:
                                    # Initialize distances from the start node to all other nodes as infinity
                                    distances = {node: float('inf') for node in graph}
                                    distances[start] = 0
                                    priority_queue = [(0, start)]

                                    while priority_queue:
                                        current_distance, current_node = heapq.heappop(priority_queue)
                                        if current_distance > distances[current_node]:
                                            continue
                                        for neighbor, weight in graph[current_node].items():
                                            distance = current_distance + weight
                                            if distance < distances[neighbor]:
                                                distances[neighbor] = distance
                                                heapq.heappush(priority_queue, (distance, neighbor))

                                    return distances
                                except Exception as e:
                                    print(f"An error occurred during Dijkstra's algorithm: {e}")

                            try:
                                graph = {}
                                num_nodes = int(input("Enter the number of nodes in the graph: "))

                                for i in range(num_nodes):
                                    node_name = input(f"Enter name of node {i + 1}: ")
                                    num_neighbors = int(input(f"Enter number of neighbors for node {node_name}: "))

                                    neighbors = {}
                                    for j in range(num_neighbors):
                                        neighbor_name, weight = input(
                                            f"Enter name and weight of neighbor {j + 1} for node {node_name}: ").split()
                                        neighbors[neighbor_name] = int(weight)

                                    graph[node_name] = neighbors
                                source_node = input("Enter source node: ")
                                target_node = input("Enter target node: ")
                                distances_from_source = dijkstra(graph, source_node)
                                print(
                                    f"The shortest distance from {source_node} to {target_node} is: {distances_from_source[target_node]}")
                            except Exception as e:
                                print(f"An error occurred: {e}")

                            W_Operations()

                    W_Operations()
                elif Kinds_Choose == "4":
                    print("Unweighted Graphs")
                    print(
                        "An unweighted graph is a graph in which the edges do not have weights or costs associated with them.")

                    def UW_Operation():
                        UW_OPeration_choose = input(
                            "Select One: \n   1.insert \n   2.delete \n   3.search\n   0:Back \n    your Choice: ")
                        if UW_OPeration_choose == "0":
                            import os
                            clear = lambda: os.system('cls')
                            clear()
                            kinds()
                        if UW_OPeration_choose == "1":
                            print("insertion")

                            class Graph:
                                def __init__(self):
                                    # Initialize an empty dictionary to store the graph
                                    self.graph = {}

                                def add_edge(self, u, v):
                                    try:
                                        # Add an edge to the graph
                                        if u not in self.graph:
                                            self.graph[u] = []
                                        if v not in self.graph:
                                            self.graph[v] = []

                                        self.graph[u].append(v)
                                        self.graph[v].append(u)
                                    except Exception as e:
                                        print(f"An error occurred while adding an edge: {e}")

                                def print_graph(self):
                                    try:
                                        # Print the adjacency list of each vertex
                                        for vertex in self.graph:
                                            print(f"Adjacency list of vertex {vertex}: ", end="")
                                            for neighbor in self.graph[vertex]:
                                                print(f"{neighbor} -> ", end="")
                                            print("None")
                                    except Exception as e:
                                        print(f"An error occurred while printing the graph: {e}")

                            try:
                                graph = Graph()
                                while True:
                                    u = input("Enter the first vertex (or 'q' to quit): ")
                                    if u == 'q':
                                        break

                                    v = input("Enter the second vertex: ")
                                    graph.add_edge(u, v)
                                graph.print_graph()
                            except Exception as e:
                                print(f"An error occurred: {e}")

                            kinds()
                        if UW_OPeration_choose == "2":
                            print("deletion")

                            class Graph:
                                def __init__(self, vertices):
                                    # Initialize the number of vertices and the adjacency list
                                    self.V = vertices
                                    self.adj_list = [[] for _ in range(vertices)]

                                def add_edge(self, u, v):
                                    try:
                                        # Add an edge to the graph
                                        self.adj_list[u].append(v)
                                        self.adj_list[v].append(u)
                                    except Exception as e:
                                        print(f"An error occurred while adding an edge: {e}")

                                def remove_edge(self, u, v):
                                    try:
                                        # Remove an edge from the graph
                                        if v in self.adj_list[u]:
                                            self.adj_list[u].remove(v)
                                            self.adj_list[v].remove(u)
                                            print("Edge ({}, {}) has been removed.".format(u, v))
                                        else:
                                            print("Edge ({}, {}) does not exist.".format(u, v))
                                    except Exception as e:
                                        print(f"An error occurred while removing an edge: {e}")

                                def print_graph(self):
                                    try:
                                        # Print the adjacency list of each vertex
                                        for i in range(self.V):
                                            print("Adjacency list of vertex {}: ".format(i), end="")
                                            for j in self.adj_list[i]:
                                                print(j, end=" ")
                                            print()
                                    except Exception as e:
                                        print(f"An error occurred while printing the graph: {e}")

                            try:
                                V = int(input("Enter the number of vertices: "))
                                graph = Graph(V)
                                E = int(input("Enter the number of edges: "))
                                for _ in range(E):
                                    u, v = map(int, input("Enter edge (u,v): ").split())
                                    graph.add_edge(u, v)
                                print("\nInitial Graph:")
                                graph.print_graph()
                                u, v = map(int, input("\nEnter edge to remove (u,v): ").split())
                                graph.remove_edge(u, v)
                                print("\nUpdated Graph:")
                                graph.print_graph()
                            except Exception as e:
                                print(f"An error occurred: {e}")

                            kinds()
                        if UW_OPeration_choose == "3":
                            print("searching")

                            from collections import defaultdict

                            class Graph:
                                def __init__(self):
                                    # Initialize an empty dictionary to store the graph
                                    self.graph = defaultdict(list)

                                def add_edge(self, u, v):
                                    try:
                                        # Add an edge to the graph
                                        self.graph[u].append(v)
                                    except Exception as e:
                                        print(f"An error occurred while adding an edge: {e}")

                                def bfs(self, start_vertex):
                                    try:
                                        # Perform Breadth-First Search (BFS) on the graph
                                        visited = [False] * (max(self.graph) + 1)
                                        queue = []

                                        queue.append(start_vertex)
                                        visited[start_vertex] = True

                                        while queue:
                                            current_vertex = queue.pop(0)
                                            print(current_vertex, end=" ")

                                            for neighbor in self.graph[current_vertex]:
                                                if not visited[neighbor]:
                                                    queue.append(neighbor)
                                                    visited[neighbor] = True
                                    except Exception as e:
                                        print(f"An error occurred during BFS: {e}")

                            try:
                                graph = Graph()
                                num_vertices = int(input("Enter the number of vertices in the graph: "))

                                for i in range(num_vertices):
                                    vertex = int(input(f"Enter vertex {i + 1}: "))
                                    num_neighbors = int(input(f"Enter the number of neighbors for vertex {vertex}: "))

                                    for j in range(num_neighbors):
                                        neighbor = int(input(f"Enter neighbor {j + 1} of vertex {vertex}: "))
                                        graph.add_edge(vertex, neighbor)
                                start_vertex = int(input("Enter the starting vertex for search: "))

                                print("BFS traversal:")
                                graph.bfs(start_vertex)
                            except Exception as e:
                                print(f"An error occurred: {e}")

                            UW_Operation()

                    UW_Operation()
                if Kinds_Choose == "5":
                    print("Complete Graphs")
                    print(
                        "A complete graph is an undirected graph in which every pair of distinct vertices is connected by a unique edge.")

                    def C_Opearion():
                        C_OPeration_choose = input(
                            "Select One: \n   1.insert \n   2.delete \n   3.search\n   0:Back \n    Your Choice: ")
                        if C_OPeration_choose == "0":
                            import os
                            clear = lambda: os.system('cls')
                            clear()
                            kinds()
                        if C_OPeration_choose == "1":
                            print("insertion")

                            class graph:
                                def __init__(self, num_nodes):
                                    # Initialize the number of nodes and the adjacency matrix
                                    self.num_nodes = num_nodes
                                    self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]

                                def add_edge(self, u, v):
                                    # Add an edge to the graph
                                    if u >= self.num_nodes or v >= self.num_nodes:
                                        print("Invalid node index!")
                                        return

                                    self.adj_matrix[u][v] = 1
                                    self.adj_matrix[v][u] = 1

                                def display_graph(self):
                                    # Display the graph
                                    for row in self.adj_matrix:
                                        print(row)

                            try:
                                num_nodes = int(input("Enter the number of nodes: "))
                                graph = graph(num_nodes)
                                while True:
                                    u = int(input("Enter the first node index (0 to {}): ".format(num_nodes - 1)))
                                    v = int(input("Enter the second node index (0 to {}): ".format(num_nodes - 1)))

                                    graph.add_edge(u, v)

                                    choice = input("Do you want to add more edges? (y/n): ")
                                    if choice.lower() != 'y':
                                        break
                                print("\nFinal Graph:")
                                graph.display_graph()
                            except Exception as e:
                                print(f"An error occurred: {e}")

                            kinds()
                        if C_OPeration_choose == "2":
                            print("deletion")

                            class CompleteGraph:
                                def __init__(self, num_vertices):
                                    # Initialize the number of vertices and the adjacency matrix
                                    self.num_vertices = num_vertices
                                    self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

                                def add_edge(self, u, v):
                                    # Add an edge to the graph
                                    self.adj_matrix[u][v] = 1
                                    self.adj_matrix[v][u] = 1

                                def delete_edge(self, u, v):
                                    # Delete an edge from the graph
                                    if u >= self.num_vertices or v >= self.num_vertices:
                                        print("Invalid vertices!")
                                        return

                                    if self.adj_matrix[u][v] == 0:
                                        print("Edge does not exist!")
                                        return

                                    self.adj_matrix[u][v] = 0
                                    self.adj_matrix[v][u] = 0

                                def display_graph(self):
                                    # Display the graph
                                    for row in self.adj_matrix:
                                        print(row)

                            try:
                                n = int(input("Enter the number of vertices: "))
                                graph = CompleteGraph(n)
                                for i in range(n):
                                    for j in range(i + 1, n):
                                        graph.add_edge(i, j)
                                print("Initial Graph:")
                                graph.display_graph()
                                while True:
                                    u = int(input("Enter the first vertex of the edge to delete (-1 to exit): "))
                                    if u == -1:
                                        break
                                    v = int(input("Enter the second vertex of the edge to delete: "))
                                    graph.delete_edge(u, v)
                                    print("\nUpdated Graph:")
                                    graph.display_graph()
                            except Exception as e:
                                print(f"An error occurred: {e}")

                                kinds()
                        if C_OPeration_choose == "3":
                            print("searching")

                            class graph:
                                def __init__(self, vertices):
                                    # Initialize the number of vertices and the adjacency matrix
                                    self.V = vertices
                                    self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

                                def add_edge(self, u, v):
                                    # Add an edge to the graph
                                    self.graph[u][v] = 1
                                    self.graph[v][u] = 1

                                def search_graph(self, start_vertex):
                                    # Perform a breadth-first search (BFS) on the graph
                                    visited = [False] * self.V
                                    queue = []

                                    visited[start_vertex] = True
                                    queue.append(start_vertex)

                                    while queue:
                                        current_vertex = queue.pop(0)
                                        print(current_vertex, end=" ")

                                        for vertex in range(self.V):
                                            if self.graph[current_vertex][vertex] == 1 and not visited[vertex]:
                                                visited[vertex] = True
                                                queue.append(vertex)

                            try:
                                num_vertices = int(input("Enter the number of vertices: "))
                                g = graph(num_vertices)
                                while True:
                                    edge_input = input("Enter two vertices to add an edge (or 'q' to quit): ")
                                    if edge_input == 'q':
                                        break

                                    u, v = map(int, edge_input.split())
                                    g.add_edge(u, v)
                                start_vertex = int(input("Enter the starting vertex for the search operation: "))

                                print("BFS Traversal:")
                                g.search_graph(start_vertex)
                            except Exception as e:
                                print(f"An error occurred: {e}")

                            C_Opearion()

                    C_Opearion()
                else:
                    print("Invalid Input!!!")
                    kinds()

            kinds()
        if Graph_Choose == "5":
            print("tervalsal of Graph")

            def Travessal_Operation():
                Travessal_Operation_Choose = input("Select One: \n   1.BFS \n   2.DFS  \n   0:Back\n    Your Choice: ")
                if Travessal_Operation_Choose == "0":
                    Graph()
                if Travessal_Operation_Choose == "1":
                    print("Breadth First Search")
                    from collections import defaultdict

                    def bfs(graph, start):
                        # Initialize the visited set and the queue
                        visited = set()
                        queue = []

                        # Add the start node to the queue and the visited set
                        queue.append(start)
                        visited.add(start)

                        # While there are nodes in the queue
                        while queue:
                            # Pop a node from the front of the queue
                            node = queue.pop(0)

                            # Print the node
                            print(node, end=" ")

                            # For each neighbor of the node
                            for neighbor in graph[node]:
                                # If the neighbor has not been visited
                                if neighbor not in visited:
                                    # Add the neighbor to the queue and the visited set
                                    queue.append(neighbor)
                                    visited.add(neighbor)

                    try:
                        # Create a default dictionary for the graph
                        graph = defaultdict(list)

                        # Get the number of vertices and edges from the user
                        num_vertices = int(input("Enter the number of vertices: "))
                        num_edges = int(input("Enter the number of edges: "))

                        print("Enter the edges (u v) where u and v are connected vertices:")

                        # For each edge
                        for _ in range(num_edges):
                            # Get the vertices of the edge from the user
                            u, v = map(int, input().split())

                            # Add an edge to the graph
                            graph[u].append(v)
                            graph[v].append(u)

                        # Get the start vertex from the user
                        start_vertex = int(input("Enter the starting vertex: "))

                        print("BFS Traversal:")

                        # Perform a breadth-first search on the graph from the start vertex
                        bfs(graph, start_vertex)
                    except Exception as e:
                        print(f"An error occurred: {e}")

                    Travessal_Operation()
                if Travessal_Operation_Choose == "2":
                    print("Depth First Search")

                    class graph:
                        def __init__(self):
                            # Initialize the graph as an empty dictionary
                            self.graph = {}

                        def add_edge(self, u, v):
                            # Add an edge to the graph
                            if u not in self.graph:
                                self.graph[u] = []
                            self.graph[u].append(v)

                        def dfs(self, start_node):
                            # Perform a depth-first search (DFS) on the graph
                            visited = set()
                            stack = [start_node]

                            while stack:
                                node = stack.pop()

                                if node not in visited:
                                    print(node, end=" ")
                                    visited.add(node)

                                    if node in self.graph:
                                        neighbors = self.graph[node]
                                        stack.extend(neighbors[::-1])

                    try:
                        graph = graph()
                        print("Enter edges (u v), one per line. Enter 'done' when finished:")
                        while True:
                            edge_input = input()
                            if edge_input == "done":
                                break
                            u, v = map(int, edge_input.split())
                            graph.add_edge(u, v)
                        start_node = int(input("Enter the starting node for DFS: "))
                        print("Depth First Search (DFS) traversal:")
                        graph.dfs(start_node)
                    except Exception as e:
                        print(f"An error occurred: {e}")

                    Travessal_Operation()
                else:
                    print(" invalid input!!!, please select correct number :")
                    Travessal_Operation()

            Travessal_Operation()
        else:
            print("Invalid Input!!!")
            Graph()

    #++++++++++++++++++++++++End Of Graph++++++++++++++++++
    def hash_table():
        hash1 = input(
            "Select One:\n   1:Definition\n   2:How to create\n   3:Applications\n   4:Operations\n   5:Colision technique\n   0:Main menu\n Your Choice: ")

        if hash1 == "1":
            print(
                """Hash Table:\t hash table, also known as a hash map, is a data structure that provides efficient storage and retrieval of key-value pairs. 
                It uses a hash function to compute an index or hash value for each key, which determines the location or bucket 
                where the key-value pair will be stored in an underlying array""")
            print(input("0:back"))
            import os
            clear = lambda: os.system('cls')
            clear()
            hash_table()
        elif hash1 == "2":
            def creation():
                def insert_key_value(my_hash_table, key, value):
                    my_hash_table[key] = value

                def delete_key(my_hash_table, key):
                    if key in my_hash_table:
                        del my_hash_table[key]

                def search_key(my_hash_table, key):
                    if key in my_hash_table:
                        return my_hash_table[key]
                    return None

                def print_hash_table(my_hash_table):
                    for key, value in my_hash_table.items():
                        print(f"{key}: {value}")

                try:
                    # Prompt the user to enter the size of the hash table
                    size = int(input("Enter the size of the hash table: "))
                    if size <= 0:
                        raise ValueError("Size must be a positive integer.")

                    # Create an empty hash table
                    my_hash_table = {}

                    # Loop through each index in the hash table
                    for i in range(size):
                        try:
                            # Prompt the user to enter a key-value pair for each index
                            key = input(f"Enter key for index {i}: ")
                            value = input(f"Enter value for index {i}: ")
                            # Insert the key-value pair into the hash table
                            insert_key_value(my_hash_table, key, value)
                            print(f"Key-value pair inserted at index {i}.")
                        except Exception as e:
                            print(f"Error: {e}")

                    # Display a menu to perform operations on the hash table
                    while True:
                        print("1. Insert key-value pair")
                        print("2. Delete key")
                        print("3. Search key")
                        print("4. Print hash table")
                        print("0. Back")

                        # Prompt the user to enter their choice
                        choice = input("Enter your choice: ")

                        if choice == "1":
                            try:
                                # Prompt the user to enter a key-value pair to insert
                                key = input("Enter key: ")
                                value = input("Enter value: ")
                                # Insert the key-value pair into the hash table
                                insert_key_value(my_hash_table, key, value)
                                print("Key-value pair inserted successfully.")
                            except Exception as e:
                                print(f"Error: {e}")
                        elif choice == "2":
                            try:
                                # Prompt the user to enter a key to delete
                                key = input("Enter key to delete: ")
                                # Delete the key from the hash table
                                delete_key(my_hash_table, key)
                                print("Key deleted successfully.")
                            except Exception as e:
                                print(f"Error: {e}")
                        elif choice == "3":
                            try:
                                # Prompt the user to enter a key to search
                                key = input("Enter key to search: ")
                                # Search for the key in the hash table
                                result = search_key(my_hash_table, key)
                                if result is not None:
                                    print(f"Key found! Value: {result}")
                                else:
                                    print("Key not found.")
                            except Exception as e:
                                print(f"Error: {e}")
                        elif choice == "4":
                            # Print the hash table
                            print_hash_table(my_hash_table)
                        elif choice == "0":
                            break
                        else:
                            print("Invalid choice. Please try again.")

                except Exception as e:
                    print(f"Error: {e}")

            creation()
            import os
            clear = lambda: os.system('cls')
            clear()
            hash_table()


        elif hash1 == "3":
            print("""Hash tables have numerous applications due to their efficient key-value storage and retrieval capabilities. Some common applications of hash tables include:

    1. Databases: Hash tables are used extensively in database systems for indexing and searching. They provide fast access to data based on keys, allowing for quick retrieval and efficient query execution.
    2. Caches: Hash tables are utilized in caching systems to store frequently accessed data. By using keys to quickly locate values, hash tables enable rapid cache lookups and improve overall performance.
    3. Symbol tables: Hash tables are commonly employed in compilers and interpreters to store symbols and their associated attributes or values. This aids in efficient name resolution and helps manage variables, functions, and other language constructs.
    4. Hash-based algorithms: Various algorithms rely on hash tables. Examples include hash-based encryption techniques, such as password hashing, and hash-based data structures like Bloom filters that efficiently determine set membership.
    5. Networking: Hash tables are used in routers and network switches for fast packet routing and filtering. They enable quick lookups based on packet headers, allowing for efficient forwarding and traffic management.
    6. Caching and memoization: Hash tables can be used to cache results of computationally expensive operations or function calls. This helps in reducing redundant calculations and improving overall execution speed.
    7. Data deduplication: Hash tables are utilized in data deduplication systems to identify and remove duplicate data chunks. By storing hashes of chunks, duplicate content can be efficiently identified and eliminated, leading to storage space reduction.
    8. Language implementation: Hash tables are employed in the implementation of dynamic languages, such as Python or JavaScript, for efficient storage of objects, attributes, and method lookup tables.
    These are just a few examples of the wide range of applications where hash tables are utilized. Their combination of fast access and efficient storage make them a valuable data structure in many domains.""")
            print(input("0:back: "))
            import os
            clear = lambda: os.system('cls')
            clear()
            hash_table()
        elif hash1 == "4":
            def operation():
                op = input("Select One: \n   1: Insert\n   2: Remove\n   3: Search\n   0: Back\n    Your Choice: ")
                if op == "1":

                    # Function to initialize the hash table
                    def init_hash_table(size):
                        # Create a list of empty lists of given size
                        return [[] for _ in range(size)]

                    # Function to calculate the hash value of a key
                    def hash_function(key, size):
                        # Use Python's built-in hash function and take modulo size to ensure the hash value is within the table size
                        return hash(key) % size

                    # Function to insert a key-value pair into the hash table
                    def insert(my_table, key, value):
                        # Calculate the index for this key using the hash function
                        index = hash_function(key, len(my_table))
                        # Append the key-value pair to the appropriate bucket in the hash table
                        my_table[index].append((key, value))

                    # Function to retrieve a value from the hash table using a key
                    def get(my_table, key):
                        # Calculate the index for this key using the hash function
                        index = hash_function(key, len(my_table))
                        # Iterate over each item in the appropriate bucket
                        for item in my_table[index]:
                            # If this item's key matches the given key, return its value
                            if item[0] == key:
                                return item[1]
                        # If no matching key was found in this bucket, return None
                        return None

                    # Function to print the entire hash table
                    def print_hash_table(my_table):
                        print("Hash Table:")
                        for i, bucket in enumerate(my_table):
                            print(f"Bucket {i}: {bucket}")

                    # Main function to interact with the user and perform operations on the hash table
                    def main():
                        try:
                            # Ask the user for the size of the hash table and initialize it
                            size = int(input("Enter the size of the hash table: "))
                            my_table = init_hash_table(size)

                            while True:
                                print("--- Hash Table Menu ---")
                                print("1. Insert key-value pair")
                                print("2. Get value by key")
                                print("0. Back")

                                try:
                                    # Ask the user for their choice of operation
                                    choice = int(input("Enter your choice: "))
                                except ValueError:
                                    # If they enter a non-integer choice, print an error message and continue to next iteration of loop
                                    print("Invalid choice!")
                                    continue
                                if choice==0:
                                    operation()
                                elif choice == 1:
                                    # If they chose 1, ask for a key-value pair and insert it into the hash table
                                    key = input("Enter the key: ")
                                    value = input("Enter the value: ")
                                    insert(my_table, key, value)
                                    print("Key-value pair inserted successfully!")
                                elif choice == 2:
                                    # If they chose 2, ask for a key and retrieve its corresponding value from the hash table
                                    key = input("Enter the key to get value: ")
                                    value = get(my_table, key)
                                    if value is not None:
                                        print(f"Value for key '{key}': {value}")
                                    else:
                                        print("Key not found in the hash table.")
                                elif choice == 3:
                                    # If they chose 3, break out of loop (end program)
                                    break
                                else:
                                    # If they entered an invalid choice, print an error message and continue to next iteration of loop
                                    print("Invalid choice!")

                                # After each operation, print out current state of hash table
                                print_hash_table(my_table)
                                print()
                            print("Program terminated.")

                        except Exception as e:
                            # Catch any other exceptions that might occur and print an error message
                            print(f"An error occurred: {str(e)}")

                    if __name__ == "__main__":
                        main()

                        import os
                        clear = lambda: os.system('cls')
                        clear()
                    operation()
                elif op == "2":
                    # Function to initialize the hash table
                    def init_table(size):
                        # Create a list of empty lists of given size
                        return [[] for _ in range(size)]

                    # Function to calculate the hash value of a key
                    def hash_function(key, size):
                        # Use Python's built-in hash function and take modulo size to ensure the hash value is within the table size
                        return hash(key) % size

                    # Function to insert a key-value pair into the hash table
                    def insert(my_table, key, value):
                        # Calculate the index for this key using the hash function
                        index = hash_function(key, len(my_table))
                        # Append the key-value pair to the appropriate bucket in the hash table
                        my_table[index].append((key, value))

                    # Function to retrieve a value from the hash table using a key
                    def get(my_table, key):
                        # Calculate the index for this key using the hash function
                        index = hash_function(key, len(my_table))
                        # Iterate over each item in the appropriate bucket
                        for item in my_table[index]:
                            # If this item's key matches the given key, return its value
                            if item[0] == key:
                                return item[1]
                        # If no matching key was found in this bucket, return None
                        return None

                    # Function to delete a key-value pair from the hash table
                    def delete(my_table, key):
                        # Calculate the index for this key using the hash function
                        index = hash_function(key, len(my_table))
                        # Iterate over each item in the appropriate bucket
                        for i, item in enumerate(my_table[index]):
                            # If this item's key matches the given key, delete it from the bucket
                            if item[0] == key:
                                del my_table[index][i]
                                return

                    # Function to print the entire hash table
                    def print_table(my_table):
                        print("Hash Table:")
                        for i, bucket in enumerate(my_table):
                            print(f"Bucket {i}: {bucket}")

                    # Main function to interact with the user and perform operations on the hash table
                    def main():
                        try:
                            # Ask the user for the size of the hash table and initialize it
                            size = int(input("Enter the size of the hash table: "))
                            my_table = init_table(size)

                            while True:
                                print("--- Hash Table Menu ---")
                                print("1. Insert key-value pair")
                                print("2. Get value by key")
                                print("3. Delete key-value pair")
                                print("0. Back")

                                try:
                                    # Ask the user for their choice of operation
                                    choice = int(input("Enter your choice: "))
                                except ValueError:
                                    # If they enter a non-integer choice, print an error message and continue to next iteration of loop
                                    print("Invalid choice!")
                                    continue
                                if choice == 0:
                                    operation()
                                elif choice == 1:
                                    # If they chose 1, ask for a key-value pair and insert it into the hash table
                                    key = input("Enter the key: ")
                                    value = input("Enter the value: ")
                                    insert(my_table, key, value)
                                    print("Key-value pair inserted successfully!")
                                elif choice == 2:
                                    # If they chose 2, ask for a key and retrieve its corresponding value from the hash table
                                    key = input("Enter the key to get value: ")
                                    value = get(my_table, key)
                                    if value is not None:
                                        print(f"Value for key '{key}': {value}")
                                    else:
                                        print("Key not found in the hash table.")
                                elif choice == 3:
                                    # If they chose 3, ask for a key and delete it from the hash table
                                    key = input("Enter the key to delete: ")
                                    delete(my_table, key)
                                    print("Key-value pair deleted successfully!")
                                elif choice == 4:
                                    # If they chose 4, break out of loop (end program)
                                    break
                                else:
                                    # If they entered an invalid choice, print an error message and continue to next iteration of loop
                                    print("Invalid choice!")

                                # After each operation, print out current state of hash table
                                print_table(my_table)
                                print()

                            print("Program terminated.")

                        except Exception as e:
                            # Catch any other exceptions that might occur and print an error message
                            print(f"An error occurred: {str(e)}")

                    if __name__ == "__main__":
                        main()

                        import os
                        clear = lambda: os.system('cls')
                        clear()
                    operation()
                elif op == "3":
                    # Function to insert a key-value pair into the hash table
                    def insert_key_value(my_table, key, value):
                        # Insert the key-value pair into the hash table
                        my_table[key] = value

                    # Function to delete a key from the hash table
                    def delete_key(my_table, key):
                        # If the key exists in the hash table, delete it
                        if key in my_table:
                            del my_table[key]

                    # Function to search for a key in the hash table
                    def search_key(my_table, key):
                        # If the key exists in the hash table, return its corresponding value
                        if key in my_table:
                            return my_table[key]
                        # If the key does not exist in the hash table, return None
                        return None

                    # Function to print the entire hash table
                    def print_table(my_table):
                        # Iterate over each key-value pair in the hash table and print it
                        for key, value in my_table.items():
                            print(f"{key}: {value}")

                    # Initialize an empty hash table
                    my_table = {}

                    while True:
                        try:
                            print("1. Insert key-value pair")
                            print("2. Delete key")
                            print("3. Search key")
                            print("4. Print hash table")
                            print("5. Back")

                            # Ask the user for their choice of operation
                            choice = input("Enter your choice: ")

                            if choice == "1":
                                # If they chose 1, ask for a key-value pair and insert it into the hash table
                                key = input("Enter key: ")
                                value = input("Enter value: ")
                                insert_key_value(my_table, key, value)
                                print("Key-value pair inserted successfully.")
                            elif choice == "2":
                                # If they chose 2, ask for a key and delete it from the hash table
                                key = input("Enter key to delete: ")
                                delete_key(my_table, key)
                                print("Key deleted successfully.")
                            elif choice == "3":
                                # If they chose 3, ask for a key and search for it in the hash table
                                key = input("Enter key to search: ")
                                result = search_key(my_table, key)
                                if result is not None:
                                    print(f"Key found! Value: {result}")
                                else:
                                    print("Key not found.")
                            elif choice == "4":
                                # If they chose 4, print out current state of hash table
                                print_table(my_table)
                            elif choice == "0":
                                # If they chose 5, break out of loop (end program)
                                import os
                                clear = lambda: os.system('cls')
                                clear()
                                operation()
                            else:
                                # If they entered an invalid choice, print an error message and continue to next iteration of loop
                                print("Invalid choice!")

                        except Exception as e:
                            # Catch any other exceptions that might occur and print an error message
                            print(f"An error occurred: {str(e)}")

                        else:
                            print("Invalid choice. Please try again.")

                elif op == "0":
                    hash_table()

            operation()
        elif hash1 == "5":
            def implementation():
                implement = input(
                    " Select One:\n   1:separate chaining\n   2:Linear probing\n   3:Double Hashin\n   4:Quadratic Probing\n   0:Back\n   Your Choice: ")
                if implement == "1":
                    print(
                        """Separate chaining: is a collision resolution technique in hashing where each bucket of the hash table contains a linked list of elements that have the same hash code. 
                        When a collision occurs, the new element is added to the existing linked list in the corresponding bucket.""")

                    # Function to create a hash table
                    def create_table(capacity):
                        # Create a list of empty lists of given size
                        table = [[] for _ in range(capacity)]
                        return table

                    # Function to calculate the hash value of a key
                    def hash_function(key, capacity):
                        # Use Python's built-in hash function and take modulo size to ensure the hash value is within the table size
                        return hash(key) % capacity

                    # Function to insert a key-value pair into the hash table
                    def put(table, key, value, capacity):
                        # Calculate the index for this key using the hash function
                        index = hash_function(key, capacity)
                        # Check if key already exists in table
                        for pair in table[index]:
                            if pair[0] == key:
                                # If key exists, update its value
                                pair[1] = value
                                return
                        # If key does not exist, append new key-value pair to table
                        table[index].append((key, value))

                    # Function to retrieve a value from the hash table using a key
                    def get(table, key, capacity):
                        # Calculate the index for this key using the hash function
                        index = hash_function(key, capacity)
                        # Iterate over each item in the appropriate bucket
                        for pair in table[index]:
                            # If this item's key matches the given key, return its value
                            if pair[0] == key:
                                return pair[1]
                        # If no matching key was found in this bucket, return None
                        return None

                    # Main function to interact with the user and perform operations on the hash table
                    def main():
                        try:
                            # Define the capacity of the hash table and create it
                            capacity = 10
                            my_table = create_table(capacity)

                            while True:
                                print("1. Add element")
                                print("2. Get element")
                                print("0. Back")

                                try:
                                    # Ask the user for their choice of operation
                                    choice = int(input("Enter your choice: "))
                                    if choice not in [1, 2, 0]:
                                        raise ValueError("Invalid choice!")
                                except ValueError as e:
                                    print(e)
                                    continue

                                if choice == 1:
                                    try:
                                        # If they chose 1, ask for a key-value pair and insert it into the hash table
                                        key = input("Enter key: ")
                                        value = input("Enter value: ")
                                        put(my_table, key, value, capacity)
                                        print("Element added successfully.")
                                    except Exception as e:
                                        print(e)
                                elif choice == 2:
                                    try:
                                        # If they chose 2, ask for a key and retrieve its corresponding value from the hash table
                                        key = input("Enter key: ")
                                        result = get(my_table, key, capacity)
                                        if result is None:
                                            print("Element not found!")
                                        else:
                                            print(f"Value for '{key}' is '{result}'")
                                    except Exception as e:
                                        print(e)
                                elif choice == 0:
                                    import os
                                    clear = lambda: os.system('cls')
                                    clear()
                                    implementation()

                        except Exception as e:
                            print(f"An error occurred: {str(e)}")

                    if __name__ == "__main__":
                        main()

                elif implement == "2":
                    print(
                        """Linear probing: is another collision resolution technique used in hash tables. 
                        In this technique, if a collision occurs, the program looks for the next available empty slot in the table, starting from the slot immediately following the one where the collision occurred.""")

                    # Function to create a hash table
                    def create_table(capacity):
                        # Create a list of None values of given size
                        table = [None] * capacity
                        return table

                    # Function to calculate the hash value of a key
                    def hash_function(key, capacity):
                        # Use Python's built-in hash function and take modulo size to ensure the hash value is within the table size
                        return hash(key) % capacity

                    # Function to insert a key-value pair into the hash table
                    def put(table, key, value, capacity):
                        # Calculate the index for this key using the hash function
                        index = hash_function(key, capacity)
                        # If the slot is occupied by a different key, find the next available slot
                        while table[index] is not None and table[index][0] != key:
                            index = (index + 1) % capacity
                        # Insert the key-value pair into the appropriate slot
                        table[index] = (key, value)

                    # Function to retrieve a value from the hash table using a key
                    def get(table, key, capacity):
                        # Calculate the index for this key using the hash function
                        index = hash_function(key, capacity)
                        # If the slot is occupied by a different key, find the next matching slot
                        while table[index] is not None and table[index][0] != key:
                            index = (index + 1) % capacity
                        # If no matching key was found in this bucket, return None
                        if table[index] is None:
                            return None
                        else:
                            return table[index][1]

                    # Main function to interact with the user and perform operations on the hash table
                    def main():
                        try:
                            # Define the capacity of the hash table and create it
                            capacity = 10
                            my_table = create_table(capacity)

                            while True:
                                print("1. Add element")
                                print("2. Get element")
                                print("0. Back")

                                try:
                                    # Ask the user for their choice of operation
                                    choice = int(input("Enter your choice: "))
                                except ValueError:
                                    print("Invalid choice!")
                                    continue

                                if choice == 1:
                                    try:
                                        # If they chose 1, ask for a key-value pair and insert it into the hash table
                                        key = input("Enter key: ")
                                        value = input("Enter value: ")
                                        put(my_table, key, value, capacity)
                                        print("Element added successfully!")
                                    except Exception as e:
                                        print(e)
                                elif choice == 2:
                                    try:
                                        # If they chose 2, ask for a key and retrieve its corresponding value from the hash table
                                        key = input("Enter key: ")
                                        result = get(my_table, key, capacity)
                                        if result is None:
                                            print("Element not found!")
                                        else:
                                            print(f"Value for '{key}' is '{result}'")
                                    except Exception as e:
                                        print(e)
                                elif choice == 0:
                                    import os
                                    clear = lambda: os.system('cls')
                                    clear()
                                    implementation()

                        except Exception as e:
                            print(f"An error occurred: {str(e)}")

                    if __name__ == "__main__":
                        main()

                elif implement == "3":
                    print(
                        """Double hashing: is a technique for resolving collisions in hash tables by using a secondary hash function to determine the next index to probe when a collision occurs.""")

                    # Function to create a hash table
                    def create_table(capacity):
                        # Create a list of None values of given size
                        table = [None] * capacity
                        return table

                    # Function to calculate the primary hash value of a key
                    def hash_function(key, capacity):
                        # Use Python's built-in hash function and take modulo size to ensure the hash value is within the table size
                        return hash(key) % capacity

                    # Function to calculate the secondary hash value of a key
                    def hash_function2(key, capacity):
                        # Use a different hash function to calculate a secondary hash value for double hashing
                        return 7 - (hash(key) % 7)

                    # Function to insert a key-value pair into the hash table
                    def put(table, key, value, capacity):
                        # Calculate the primary index for this key using the primary hash function
                        index = hash_function(key, capacity)
                        # Calculate the step size for probing using the secondary hash function
                        step = hash_function2(key, capacity)
                        # If the slot is occupied by a different key, find the next available slot using double hashing
                        while table[index] is not None and table[index][0] != key:
                            index = (index + step) % capacity
                        # Insert the key-value pair into the appropriate slot
                        table[index] = (key, value)

                    # Function to retrieve a value from the hash table using a key
                    def get(table, key, capacity):
                        # Calculate the primary index for this key using the primary hash function
                        index = hash_function(key, capacity)
                        # Calculate the step size for probing using the secondary hash function
                        step = hash_function2(key, capacity)
                        # If the slot is occupied by a different key, find the next matching slot using double hashing
                        while table[index] is not None and table[index][0] != key:
                            index = (index + step) % capacity
                        # If no matching key was found in this bucket, return None
                        if table[index] is None:
                            return None
                        else:
                            return table[index][1]

                    # Main function to interact with the user and perform operations on the hash table
                    def main():
                        try:
                            # Define the capacity of the hash table and create it
                            capacity = 10
                            my_table = create_table(capacity)

                            while True:
                                print("1. Add element")
                                print("2. Get element")
                                print("0. Back")

                                try:
                                    # Ask the user for their choice of operation
                                    choice = int(input("Enter your choice: "))
                                except ValueError:
                                    print("Invalid choice!")
                                    continue

                                if choice == 1:
                                    try:
                                        # If they chose 1, ask for a key-value pair and insert it into the hash table
                                        key = input("Enter key: ")
                                        value = input("Enter value: ")
                                        put(my_table, key, value, capacity)
                                        print("Element added successfully!")
                                    except Exception as e:
                                        print(e)
                                elif choice == 2:
                                    try:
                                        # If they chose 2, ask for a key and retrieve its corresponding value from the hash table
                                        key = input("Enter key: ")
                                        result = get(my_table, key, capacity)
                                        if result is None:
                                            print("Element not found!")
                                        else:
                                            print(f"Value for '{key}' is '{result}'")
                                    except Exception as e:
                                        print(e)
                                elif choice == 0:
                                    import os
                                    clear = lambda: os.system('cls')
                                    clear()
                                    implementation()

                        except Exception as e:
                            print(f"An error occurred: {str(e)}")

                    if __name__ == "__main__":
                        main()


                elif implement == "4":
                    print(
                        """Quadratic probing: is a technique for resolving collisions in hash tables by using a quadratic function to determine the next index to probe when a collision occurs.""")

                    # Function to create a hash table
                    def create_table(capacity):
                        # Create a list of None values of given size
                        table = [None] * capacity
                        return table

                    # Function to calculate the hash value of a key
                    def hash_function(key, capacity):
                        # Use Python's built-in hash function and take modulo size to ensure the hash value is within the table size
                        return hash(key) % capacity

                    # Function to insert a key-value pair into the hash table
                    def put(table, key, value, capacity):
                        # Calculate the index for this key using the hash function
                        index = hash_function(key, capacity)
                        i = 1
                        # If the slot is occupied by a different key, find the next available slot using quadratic probing
                        while table[index] is not None and table[index][0] != key:
                            index = (index + i ** 2) % capacity
                            i += 1
                        # Insert the key-value pair into the appropriate slot
                        table[index] = (key, value)

                    # Function to retrieve a value from the hash table using a key
                    def get(table, key, capacity):
                        # Calculate the index for this key using the hash function
                        index = hash_function(key, capacity)
                        i = 1
                        # If the slot is occupied by a different key, find the next matching slot using quadratic probing
                        while table[index] is not None and table[index][0] != key:
                            index = (index + i ** 2) % capacity
                            i += 1
                        # If no matching key was found in this bucket, return None
                        if table[index] is None:
                            return None
                        else:
                            return table[index][1]

                    # Main function to interact with the user and perform operations on the hash table
                    def main():
                        try:
                            # Define the capacity of the hash table and create it
                            capacity = 10
                            my_table = create_table(capacity)

                            while True:
                                print("1. Add element")
                                print("2. Get element")
                                print("0. Back")

                                try:
                                    # Ask the user for their choice of operation
                                    choice = int(input("Enter your choice: "))
                                except ValueError:
                                    print("Invalid choice!")
                                    continue

                                if choice == 1:
                                    try:
                                        # If they chose 1, ask for a key-value pair and insert it into the hash table
                                        key = input("Enter key: ")
                                        value = input("Enter value: ")
                                        put(my_table, key, value, capacity)
                                        print("Element added successfully!")
                                    except Exception as e:
                                        print(e)
                                elif choice == 2:
                                    try:
                                        # If they chose 2, ask for a key and retrieve its corresponding value from the hash table
                                        key = input("Enter key: ")
                                        result = get(my_table, key, capacity)
                                        if result is None:
                                            print("Element not found!")
                                        else:
                                            print(f"Value for '{key}' is '{result}'")
                                    except Exception as e:
                                        print(e)
                                elif choice == 0:
                                    import os
                                    clear = lambda: os.system('cls')
                                    clear()
                                    implementation()

                        except Exception as e:
                            print(f"An error occurred: {str(e)}")

                    if __name__ == "__main__":
                        main()

                elif implement == "0":
                    hash_table()
                else:
                    print("invalid Input!!")
                    implementation()
            implementation()

        elif hash1 == "0":
            import os
            clear = lambda: os.system('cls')
            clear()
            data_structure()
        else:
            print("invalid input!!")
            hash_table()

    #++++++++++++++++++++++++++++++++++End Of Hash Table++++++++++++++++++++++++++++++++++++++++
    choose = input("Select one option:\n  0: algorithm\n  1: Arrays\n  2: Stack\n  3: Queue\n  4: Linked List\n  5:Tree\n  6:Graph \n  7:Hash Tables \n  8: Exit:\n   Your Choice: ")
    if choose == "1":
        Arrays()
    elif choose == "2":
        Stack()
    elif choose == "3":
        Queu()
    elif choose == "4":
        Linked_list()
    elif choose == "0":
        algorithm()
    elif choose =="5":
        TreeDs()
    elif choose =="6":
        Graph()
    elif choose=="7":
        hash_table()
    elif choose=="8":
        print("Good BYe")
        sys.exit()
    else:
        print("invalid input! Choose the correct number(0-8)")
        data_structure()

data_structure()
