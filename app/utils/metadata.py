# DEFINE EACH TAG METADATA IN HERE
# DOCUMENTATION
tags = [
    {
        "name": "users",
        "description": "Operations with users."
        + "The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
    {
        "name": "products",
        "description": "Operations with _products_.",
    },
    {
        "name": "product_categories",
        "description": "Operations with _products categories_."
        + " **Many to one** with Product.",
    },
    {
        "name": "product_details",
        "description": "Operations with _products details_."
        + " **One to one** with Product.",
    },
    {
        "name": "product_insurance_types",
        "description": "Operations with _products insurance types_."
        + " **Many to one** with Product.",
    },
]
