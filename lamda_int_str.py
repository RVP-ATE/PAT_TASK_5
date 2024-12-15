# Sample list containing both integers and strings
sample_list = [10, 'apple', 45, 'banana', 100, 'cherry', 25.5, 'grape']

# Using lambda function to check if each element is an integer or string
check_type = lambda x: "Integer" if isinstance(x, int) else "String" if isinstance(x, str) else "Other"

# Applying the lambda function to each element of the list
result = list(map(check_type, sample_list))

# Print results
for item, res in zip(sample_list, result):
    print(f"Element: {item} is a {res}")