import pandas as pd
import os

dirname = os.path.dirname(__file__)
csv_path = os.path.join(dirname, '../sources.csv')
readme_path = os.path.join(dirname, '../README.md')

df = pd.read_csv(csv_path)

df['website'] = '[link](' + df['website'].astype(str) + ')'
df['license_page'] = '[link](' + df['license_page'].astype(str) + ')'

with open(readme_path, "w") as file1:
    file1.write("# Open Data Sources \n\n")
    file1.writelines(df.to_markdown(index=False))