
"""
Name: Jose Alarcon Chacon
Email: jose.alarconchacon76@login.cuny.edu
Date: April 23, 2025
Program accept three inputs parameters, then create a dataframe with the values
"""


import pandas as pd # import pandas as pd

def make_addr_df(last_name, first_name, email): 
    # use split to create a list for each input parameter
    last_name_list = last_name.split()
    first_name_list = first_name.split()
    email_list = email.split()
    
    # create a dataframe with dictionaries, one column for each input parameter
    data_frame = pd.DataFrame({
        'Last': last_name_list,
        'First': first_name_list,
        'emails': email_list
    })
    return data_frame

# test program with the provided values
def main():
    hc_last = "Hunter Raab Kirschner Cantor"
    c_first = "Thomas Jennifer Anne Nancy"
    hc_email = "th1870@hunter.cuny.edu jr2001@hunter.cuny.edu ak2023@hunter.cuny.edu nc2024@hunter.cuny.edu"
    print(make_addr_df(hc_last, c_first, hc_email))
    
# call main function 
if __name__ == "__main__":
    main()