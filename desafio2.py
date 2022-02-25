def password(my_password):
    if type(my_password) == str:
        special_character = [
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            "()",
            "-",
            "+",
        ]

        is_special_character = 0
        count_uppercase = 0
        count_lowercase = 0
        count = 0

        for character in my_password:
            if character in special_character:
                is_special_character += 1
            if character.islower() is True:
                count_lowercase += 1
            if character.isupper() is True:
                count_uppercase += 1

        if is_special_character == 0:
            count += 1

        if any(map(str.isdigit, my_password)) is False:
            count += 1

        if count_lowercase == 0:
            count += 1
        if count_uppercase == 0:
            count += 1

        if len(my_password) <= 3:
            return ((6 - len(my_password)) - count) + count
        if count == 0:
            return 6 - len(my_password)
        return count
    else:
        return False
