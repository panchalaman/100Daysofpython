def format_name(f_name, l_name):
    """This function formats the given string of first and last name to title case."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))
