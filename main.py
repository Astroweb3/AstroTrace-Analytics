import pandas as pd
import matplotlib.pyplot as plt
from googlesearch import search
import datetime
file_path ='F:/0.2 rexAi/hacathon/Food_Production.csv'

food_data = pd.read_csv(file_path)

# Display the first few rows of the DataFrame to understand the structure
print(food_data.head(43))

# Explore basic statistics of the numerical columns
print(food_data.describe().T)

# Check for missing values
print(food_data.isnull().sum().sum())

#fill the emptycell
food_data.fillna(0, inplace=True)

#plot the factor and product
for index, row in food_data.iterrows():
    
    # Extract values row vice
    values_in_row = row.iloc[1:].astype(float).fillna(0)
    
    # Plot the values
    plt.plot(values_in_row, label=row.iloc[0])
    plt.xticks(rotation=90, ha='right')
    

plt.xlabel('Factors')
plt.ylabel('Impact')
plt.title('LCA [Life Cycle Assessment]')
plt.tight_layout()
plt.legend(bbox_to_anchor=(1.01, 1.04), loc='upper left')


# Calculate the total emissions for each product
food_data['Total Emissions'] = food_data.iloc[:, 1:8].sum(axis=1)

# Sort the DataFrame based on 'Total Emissions' in descending order
sorted_food_data = food_data.sort_values(by='Total Emissions', ascending=False)

# Display the DataFrame with the added 'Total Emissions' column
print(sorted_food_data[['Food product', 'Total Emissions']])


#----- Emmision PLot----


# Define the colormap
cmap = plt.cm.RdYlGn_r  # Red-Yellow-Green colormap
# Normalize the values to range from 0 to 1
norm = plt.Normalize(min(sorted_food_data['Total Emissions']), max(sorted_food_data['Total Emissions']))

#image size
plt.figure(figsize=(20, 16))

# Create the bar chart with colormap
bars = plt.bar(sorted_food_data['Food product'], sorted_food_data['Total Emissions'], color=cmap(norm(sorted_food_data['Total Emissions'])))
plt.xlabel('Factors')
plt.ylabel('Rating')
plt.title('Factors of Food Product')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()

# Create a side color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)

# Set an empty array to match the colormap
sm.set_array([]) 
cbar = plt.colorbar(sm, ax=plt.gca())#ax=plt.gca()determine the axis
cbar.set_label('Danger Level')

#display
plt.show()
links = []
#find solution for emmission
search_query = f'{sorted_food_data["Food product"]} emmissions solution'
num_results = 5
results = list(search(search_query, num_results=num_results))
for result in results:
    links.append(result)
    
df = pd.DataFrame(links,columns = [f'{sorted_food_data["Food product"].head(1)} Emmissions Solutions'])
df.to_csv('sol{}.csv'.format(datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')))