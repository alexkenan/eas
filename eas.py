from time import sleep
import pandas as pd
import plotly.graph_objects as go


# get the df ready. This path may need to be edited if the combined.xlsx spreadsheet is not in the same directory
df = pd.read_csv("https://raw.githubusercontent.com/alexkenan/eas/main/eas.csv")

# Create an airline dictionary to assign the big 4 airlines as distinct colors
lower48 = {"American": '#fc787c', 'United': '#eeeb5d',
           'SkyWest': 'orange', 'Alaska Airlines': 'green'}

# make the points for the EAS community airports
fig = go.Figure(go.Scattermapbox(
    mode="markers",
    lon=df["Airport Long"],
    lat=df["Airport Lat"],
    marker={'size': 6, 'color': 'blue'},
    name="EAS airports",
    hovertext=df['EAS Community']))

# make the points for the hub airports
fig.add_trace(go.Scattermapbox(
    mode="markers",
    lon=df["Hub Long"],
    lat=df["Hub Lat"],
    marker={'size': 6, 'color': 'red'},
    name="Hubs",
    hovertext=df['Current Hubs Served']))

# create a list of carriers so that the legend shows other if the carrier is not in the list of main carriers
list_of_carriers = []
list_of_main_carriers = ["American", 'United', 'SkyWest', 'Alaska Airlines']

# for each row in the df, plot a line between the airport lat/lon and hub lat/lon
for row in range(len(df)):
    temp_df = df.iloc[row]
    x_coords = (temp_df['Airport Lat'], temp_df['Hub Lat'])
    y_coords = (temp_df['Airport Long'], temp_df['Hub Long'])
    carrier = temp_df['EAS Carrier']
    fig.add_trace(go.Scattermapbox(mode="lines", lon=y_coords, lat=x_coords, showlegend=False,
                                   line={'color': 'gray'},
                                   hovertext="{} to {} by {}".format(temp_df['EAS Community'],
                                                                     temp_df['Current Hubs Served'],
                                                                     carrier),
                                   name=""))
    
    # assign a linecolor to carriers. Use gray if the carrier is not a main carrier
    if carrier in lower48.keys():
        linecolor = lower48[carrier]
    else:
        linecolor = 'gray'

    # create the legend label to use Other if the carrier is not one of the main carriers
    if carrier not in list_of_main_carriers:
        carrier_legend = 'Other'
    else:
        carrier_legend = carrier

    # if the carrier has already been shown in the legend, don't show it again. This means that only one "American" will show
    # in the legend, for example, instead of 10
    if carrier_legend in list_of_carriers:
        show_legend = False
    else:
        show_legend = True
        list_of_carriers.append(carrier_legend)

    # add the trace (line) to the figure
    fig.add_trace(go.Scattermapbox(mode="lines", lon=y_coords, lat=x_coords, showlegend=show_legend,
                                   line={'color': linecolor},
                                   hovertext="{} to {} by {}".format(temp_df['EAS Community'],
                                                                     temp_df['Current Hubs Served'],
                                                                     carrier),
                                   name=carrier_legend))


# update the layout to center it, fix the zoom, pick the map type, and select the geo scope
fig.update_layout(
    margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
    mapbox={'center': {'lon': -100, 'lat': 40},
            'style': "carto-positron",
            'zoom': 3},
    geo_scope="usa")

# show the figure
fig.show()
sleep(20)
fig.write_html('eas_map.html')
