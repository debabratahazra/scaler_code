import pandas as pd
#rides is the loaded dataframe consisting of columns 'Start station', 'End station' and 'Duration'

start_station = ['Broad St', '66 St-Lincoln Center', '86th St', 'Times Sq - 42 St', '86th St', 'Bowery', '66 St-Lincoln Center', '66 St-Lincoln Center', '14 St / 8 Av', 'Times Sq - 42 St']
end_station = ['14 St / 8 Av', 'Bowery', 'Bowery', '66 St-Lincoln Center', '66 St-Lincoln Center', 'Broad St', 'Broad St', 'Broad St', '14 St / 8 Av', 'Times Sq - 42 St']
duration = [0.12, 1.94, 2.47, 1.53, 2.76, 1.93, 0.33, 0.94, 2.71, 1.39]

rides = pd.DataFrame({
    'Start station': start_station,
    'End station': end_station,
    'Duration': duration
})

# find joyrides
joyrides = (rides['Start station'] == rides['End station'])

# Median of all rides
print("The median duration overall was {:.2f} hrs".format(rides['Duration'].median()))

# Median of joyrides
print("The median duration for joyrides was {:.2f} hrs".format(rides[rides['Start station'] == rides['End station']]['Duration'].median()))
