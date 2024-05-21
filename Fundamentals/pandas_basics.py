data = {
        "Name": ["Arvind", "Diwash", "Diwas", "Sagar", "Utkarsh"],
        "Age": ["15", "16", "17", "16", "15"]
        }
import pandas
result = pandas.DataFrame(data)
resutl = pandas.melt(result)
print(result)
