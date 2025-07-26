"""Script to fetch World Bank data for Iran's water crisis analysis."""

import wbdata
import pandas as pd


countries = ["IRN"] # Iran ISO-3 code
date_range = ("2000", "2024")

# The World Bank measurments we want to fetch
# 'SP.POP.TOTL' is the total population
# 'AG.LND.AGRI.K2' is the agricultural land area (sq. km)
# 'AG.LND.ARBL.HA.PC' is the arable land area (hectares per person)
# 'NV.AGR.TOTL.ZS' is the agricultural, forestry, and fishing, value added (% of GDP)
# 'AG.LND.ARBL.HA.PC' is the arable land area (hectares per person)

indicators = {
    'SP.POP.TOTL': 'population',
    'AG.LND.AGRI.K2': 'agricultural_land_sqkm',
}

# Fetch the data
try:
    df = wbdata.get_dataframe(indicators, country=countries, date=date_range)
    print("\n✅ Raw data fetched successfully. Filtering by year...")

    # Process the DataFrame
    df = df.reset_index().rename(columns={'date': 'year'})
    df['year'] = pd.to_numeric(df['year'])

    # Filter the date range using pandas
    df_filtered = df[(df['year'] >= int(date_range[0])) & (df['year'] <= int(date_range[1]))].copy()
    df_filtered = df_filtered.sort_values('year').reset_index(drop=True)

    # 5. Save the final data
    output_path = './data/raw/world_bank_iran_data.csv'
    df_filtered.to_csv(output_path, index=False)
    
    print(f"\n✅ Final data for {date_range[0]}-{date_range[1]} saved to {output_path}")
    print("--- First 5 rows of the clean data: ---")
    print(df_filtered.head())
    
except Exception as e:
    print(f"❌ Error fetching data: {e}")