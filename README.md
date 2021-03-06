# Essential Air Service
*Plotly map for the US DOT's Essential Air Service subsidy program*

Not many people know about [Essential Air Service](https://en.wikipedia.org/wiki/Essential_Air_Service) (EAS).

EAS is a US Department of Transportation (DOT) program that is designed to provide commercial air service to rural communities that could not otherwise sustain service. As of September 2020, there are a total of 219 subsidized routes: 75 in Alaska, 2 in Hawaii, 1 in Puerto Rico, and 141 in the continental United States. The program paid out about $335 million in funding in 2020. If you were to fly on a route serviced by SkyWest, American Eagle, Alaska Airlines, or another "major" airline, you would not know that you were on a subsidized route. Other, smaller routes are serviced with turboprop aircraft that may not offer a seamless connection to major airline service.

Updated reports can be found in pdf and spreadsheet format at [this DOT site](https://www.transportation.gov/office-policy/aviation-policy/essential-air-service-reports). A historical explanation from the DOT can be found [here](https://www.transportation.gov/policy/aviation-policy/small-community-rural-air-service/essential-air-service). An imgur album with the screenshots for continental US, Alaska, Hawaii, and Puerto Rico can be found [here](https://imgur.com/a/bg0ggJw).

**eas.py** was originally written to use the **combined.xlsx** spreadsheet that contained all info about EAS as of September, 2020. I tried to convert the spreadsheet to a csv (**eas.csv**) to be able to just pull the raw data from the csv without having to download the spreadsheet. Since converting to CSV causes some data loss, I have uploaded the spreadsheet to use as a backup.

**eas_map.html** is the completed HTML webpage file that Plotly renders. You should be able to download and open this file, and hover over the different routes to see the hub, EAS airport, and airline/air carrier that services that route.
