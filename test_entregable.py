import pytest
from entregable import almacenarProductosBD

@pytest.mark.parametrize(
    "input_a, expected",
    [
        ([{
        "Titulo": "Samsung Galaxy A12 64 GB negro 4 GB RAM",
        "Precio": "$35.649",
        "Reviews": "50",
        "Fulfillment": "yes",
        "Url": "https://www.mercadolibre.com.ar/samsung-galaxy-a12-64-gb-negro-4-gb-ram/p/MLA17415926?pdp_filters=category:MLA1055#searchVariation=MLA17415926&position=1&search_layout=stack&type=product&tracking_id=ae1bfc4e-066e-4797-b874-1e4e6f11159c"
    },{
        "Titulo": "Samsung Galaxy S20 FE 128 GB cloud navy 6 GB RAM",
        "Precio": "$94.999",
        "Reviews": "2639",
        "Fulfillment": "yes",
        "Url": "https://www.mercadolibre.com.ar/samsung-galaxy-s20-fe-128-gb-cloud-navy-6-gb-ram/p/MLA16211370?pdp_filters=category:MLA1055#searchVariation=MLA16211370&position=2&search_layout=stack&type=product&tracking_id=6034e461-3c6a-49d7-9260-24a07c2911f5"
    }], 2),
    ([{
        "Titulo": "Samsung Galaxy A12 64 GB negro 4 GB RAM",
        "Precio": "$35.649",
        "Reviews": "50",
        "Fulfillment": "yes",
        "Url": "https://www.mercadolibre.com.ar/samsung-galaxy-a12-64-gb-negro-4-gb-ram/p/MLA17415926?pdp_filters=category:MLA1055#searchVariation=MLA17415926&position=1&search_layout=stack&type=product&tracking_id=ae1bfc4e-066e-4797-b874-1e4e6f11159c"
    }], 1)
    ]
)
def test_almacenarProductosBD(input_a, expected):
    assert almacenarProductosBD(input_a) ==expected