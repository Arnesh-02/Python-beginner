years = ["January 2023", "February 2024", "March 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
for i in range(len(years)):
    if "2023" not in years[i]:
        years[i]=years[i].replace(years[i].split( )[-1],"2023")
print(years)
