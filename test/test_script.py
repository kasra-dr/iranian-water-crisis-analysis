import wbdata

indicators_to_test = [
    'SP.POP.TOTL',
    'AG.LND.AGRI.K2',
    'EG.USE.AGRI.ZS',
]

countries_to_test = ['IRN']

print("--- Testing Indicators One by One ---")
for indicator in indicators_to_test:
    try:
        # Try to fetch the data for just ONE indicator
        wbdata.get_dataframe({indicator: 'test'}, country=countries_to_test)
        print(f"Successfully fetched data for {indicator}")
    except Exception as e:
        print(f"Error fetching data for {indicator}: {e}")
print("--- All tests completed ---")