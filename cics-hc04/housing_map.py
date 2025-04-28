
import plotly.express as px
import pandas as pd

# get user input
def get_user_input():
    input_file_name = input("Enter the name of the CSV file (with .csv extension): ")
    num_of_bedrooms = int(input("Enter the number of bedrooms: "))
    output_file_name = input("Enter the name of the output HTML file (with .html extension): ")
    return input_file_name, num_of_bedrooms, output_file_name

# read the CSV file
def read_csv_file(file_name):
    return pd.read_csv(file_name)

# get units column from 0 - 6
def get_units_column(bedrooms):
    if bedrooms == 0:
        return 'Studio Units'
    elif bedrooms == 1:
        return '1-BR Units'
    elif bedrooms == 2:
        return '2-BR Units'
    elif bedrooms == 3:
        return '3-BR Units'
    elif bedrooms == 4:
        return '4-BR Units'
    elif bedrooms == 5:
        return '5-BR Units'
    else:
        return '6-BR+ Units'
    

def main():
    # get user input
    input_file_name, num_of_bedrooms, output_file_name = get_user_input()
    # read the CSV file
    data_file = read_csv_file(input_file_name)
    # drop confidential
    drop_data = data_file[data_file['Project Name'] != 'Confidential']
    # get the units column
    units = get_units_column(num_of_bedrooms)
    # filter rows with missing values
    filter_data = drop_data[drop_data[units].notnull()]
    
    # create a map
    fig = px.scatter_mapbox(filter_data, 
                            lat='Latitude', 
                            lon='Longitude', 
                            hover_name='Project Name',
                            size=units, size_max=15, zoom=10)
    fig.update_layout(mapbox_style="open-street-map", title=f"Housing: {units}")
    
    fig.show()
    # save the map to an HTML file
    fig.write_html(output_file_name)
    
if __name__ == "__main__":
    main()



