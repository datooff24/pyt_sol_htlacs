def expression_to_token(string_list):
    # First split the expression into a list
    token_list = string_list.split()

    # Now clean up the list
    # Step 1: separate parentheses from number
    new_token_list = []
    for item in token_list:
        if '(' or ')' in item:
            # Create a list that separates the parantheses from the numbers
            temporary_list = list(item)
            new_token_list.extend(temporary_list)
        else:
            new_token_list.extend(item)

    # Step 2: turn numbers into integers
    for index, item in enumerate(new_token_list):
        if item in "0123456789":
            new_token_list[index] = int(item)

    # Step 3: add "end" to the end of the list
    new_token_list.append("end")
    return new_token_list


# Test
y = expression_to_token("(3 + 7) * 9")
print(y)