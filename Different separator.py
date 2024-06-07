#If you want to use a different separator for names.
def likes(arr):
    if not arr:
        return "no one likes this"
    elif len(arr) == 1:
        return f"{arr[0]} likes this"
    elif len(arr) == 2:
        return f"{arr[0]} and {arr[1]} like this"
    elif len(arr) == 3:
        return f"{arr[0]}, {arr[1]} & {arr[2]} like this"
    else:
        return f"{arr[0]}, {arr[1]}, {arr[2]} & {len(arr) - 3} others like this"

array = ['Peter', 'John', 'Andrew', 'Jacob', 'Modecai']
print(likes(array))  # Output: "Peter, John, Andrew & 2 others like this"
