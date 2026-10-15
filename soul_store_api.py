import requests
import csv
from pathlib import Path


# Step 1: API URL
url = "https://api.thesouledstore.com/api/v2/pre-order/products/listing"


# Step 2: Request payload
payload = {
    "artist": "",
    "category": "",
    "filters": {},
    "gender_type": 3,
    "is_exclusive": 0,
    "offset": 24,
    "page": 1,
    "tags": "men-footwear",
    "tiptitle": 1
}


# Step 3: Request headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


try:
    # Step 4: Call API
    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=30
    )

    print("Status Code:", response.status_code)

    response.raise_for_status()

    # Step 5: Convert response to JSON
    data = response.json()

    products = data.get("products", [])

    print("API connection successful!")
    print("Total products received:", len(products))

    # Step 6: Check products
    if products:

        print("\nFirst product:")
        print(products[0].get("title"))

        # Step 7: Create output folder
        output_dir = Path("output")
        output_dir.mkdir(parents=True, exist_ok=True)

        csv_file = output_dir / "soul_store_products.csv"

        # Step 8: Select columns
        columns = [
            "id",
            "title",
            "price",
            "category",
            "product_slug",
            "stock",
            "artist"
        ]

        # Step 9: Write CSV
        with csv_file.open(
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=columns
            )

            writer.writeheader()

            for product in products:

                row = {}

                for column in columns:
                    value = product.get(column)

                    if isinstance(value, list):
                        value = ", ".join(
                            str(item) for item in value
                        )

                    row[column] = value

                writer.writerow(row)

        print("\nCSV file created successfully!")
        print("Saved location:", csv_file.resolve())

    else:
        print("No products found in the API response.")


except requests.exceptions.RequestException as error:
    print("API request failed:", error)

except ValueError:
    print("The API response is not valid JSON.")