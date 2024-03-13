import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# 3(a)
# Open the file
# ds - original file that we uploeaded
file_path = "ERA5_2mTemp_19900101-19900531_00h.nc"
ds = xr.open_dataset(file_path)

temp_jan1 = ds['t2m'].sel(time='1990-01-01')

#plot the temperature on 01/01/1990
plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree())
temp_jan1.plot(ax=ax, transform=ccrs.PlateCarree(), x='longitude', y='latitude', cbar_kwargs={'label': '2m Temperature (K)'})
ax.coastlines()
ax.set_global()
plt.title('Global Temperature Map on January 1, 1990')
plt.show()

# 3(b)
# Calculate daily mean global temperature
daily_mean_global_temp = ds['t2m'].mean(['longitude', 'latitude']).resample(time='1D').mean()

#Plot time series graph
plt.figure(figsize=(14, 6))
daily_mean_global_temp.plot()
plt.title('Daily Mean Global Temperature (January-May 1990)')
plt.xlabel('Date')
plt.ylabel('Temperature (K)')
plt.grid(True)
plt.show()

# 3(c)
# Calculate the mean temperature for each month (January-May) and plot the data on (five) global maps
# resample the dataset to monthly frequency and calculate average temp
monthly_mean_temp = ds['t2m'].resample(time='M').mean()

# dataset only has the temp of 5 months
# list with the month names for the plots
months = ['January', 'February', 'March', 'April', 'May']

# loop for the graphs
for i, month in enumerate(months):
    #the size of the plot
    plt.figure(figsize=(10, 5))
    # Set the projection to PlateCarree for a global map
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    monthly_mean_temp.sel(time=monthly_mean_temp['time.month'] == i + 1).mean(dim='time').plot()
    plt.title(f'Mean temperature for {month}')
    plt.show()
