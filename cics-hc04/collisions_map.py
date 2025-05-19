import plotly.graph_objects as go #Including for markers
import plotly.express as px # Including for map
import pandas as pd


# get user input and output file
def get_user_inputs():
    input_file_name = input("Enter the input file name: ")
    output_file_name = input("Enter the output file name: ")
    return input_file_name, output_file_name

# read data from user input file
def read_file_data(data):
    file_data = pd.read_csv(data)
    return file_data

# drop rows with missing data
def drop_missing_data(data):
    data = data.dropna(subset=["LATITUDE", "LONGITUDE"])
    return data

def main(): 
    input_file_name, output_file_name = get_user_inputs() # call input function
    
    data = read_file_data(input_file_name) # reade data
    data = drop_missing_data(data) # drop missing data
    
    # set map with Scattermap
    fig = px.scatter_map(data, lat="LATITUDE", lon="LONGITUDE", 
                            hover_name="TIME", 
                            zoom=10, height=600)
    # set map layout
    fig.update_layout(hovermode='closest',
                  map=dict(center=go.layout.map.Center(lat=40.7,lon=-74),
                           zoom=8))
    
    fig.show() # show map
    fig.write_html(output_file_name) # save map to file
    
if __name__ == "__main__":
    main() # call main function 
    
    
    

