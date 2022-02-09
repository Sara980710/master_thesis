from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
import pandas as pd

api = SentinelAPI('ebaa.asaad', 'LBC*c%7exuH+UHX', 'https://apihub.copernicus.eu/apihub')

# search by polygon, time, and SciHub query keywords
footprint = geojson_to_wkt(read_geojson('map.geojson'))
products = api.query(footprint,
                     date=('20151219', date(2015, 12, 29)),
                     platformname='Sentinel-2')

# convert to Pandas DataFrame
products_df = api.to_dataframe(products)

print(f"Number of rows: {len(products_df.index)}")
print(f"Number of columns: {len(products_df.columns)}")

products_df_sorted = products_df.sort_values(['ingestiondate'], ascending=[False])
products_df_sorted = products_df_sorted[products_df_sorted['platformname'] == 'Sentinel-2']

products_df_sorted["ingestiondate"]

products_df_sorted = products_df_sorted.sort_values(['size'], ascending=[True])

products_df_sorted.head(1)["size"]

product_download = products_df_sorted.head(1)

# print("Downloading...")
# api.download_all(product_download.index)

print(f"Product ID: {product_download.index[0]}")
product_info = api.get_product_odata(product_download.index[0])
is_online = product_info['Online']
# or
is_online = api.is_online(product_download.index[0])

if is_online:
    print(f'Product {product_download.index[0]} is online. Starting download.')
    api.download(product_download.index[0])
else:
    print(f'Product {product_download.index[0]} is not online.')
    api.trigger_offline_retrieval(product_download.index[0])