#!/usr/bin/env python3
"""Extrae portátiles disponibles en CeX España usando Algolia (misma fuente que es.webuy.com)."""

import json
import re
import urllib.request
from datetime import datetime

APP_ID = "LNNFEEWZVA"
API_KEY = "bf79f2b6699e60a18ae330a1248b452c"
INDEX = "prod_cex_es_price_asc"
ALGOLIA_URL = f"https://search.webuy.io/1/indexes/{INDEX}/query"
PRODUCT_URL = "https://es.webuy.com/product-detail?id="

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Accept-Language": "es-ES,es;q=0.9",
    "Origin": "https://es.webuy.com",
    "Referer": "https://es.webuy.com/",
    "X-Algolia-Application-Id": APP_ID,
    "X-Algolia-API-Key": API_KEY,
}

# Línea de producto "Portátiles" en CeX (productLineId=35)
LAPTOP_CATEGORIES = [
    "Portatiles - Apple",
    "Portatiles - Windows",
    "Portatiles - Otros OS",
    "Chromebooks",
]

MIN_PRICE = 600
MAX_PRICE = 1600
OUTPUT_FILE = "portatiles_cex_600_1600.txt"

GRADE_MAP = {"A": "En perfecto estado", "B": "Bueno", "C": "Aceptable"}


def fetch_algolia_settings():
    url = "https://wss2.cex.es.webuy.io/v3/appsettings/prelogin?platformId=18"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": HEADERS["User-Agent"],
            "Accept": "application/json",
            "Origin": "https://es.webuy.com",
            "Referer": "https://es.webuy.com/",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read())["response"]["data"]["preLoginSettings"]


def algolia_search(page=0, hits_per_page=250):
    cat_filter = " OR ".join(f'categoryFriendlyName:"{c}"' for c in LAPTOP_CATEGORIES)
    filters = (
        f"({cat_filter}) AND sellPrice >= {MIN_PRICE} AND sellPrice <= {MAX_PRICE} "
        f'AND availability:"Disponible online"'
    )
    payload = {
        "query": "",
        "page": page,
        "hitsPerPage": hits_per_page,
        "filters": filters,
    }
    req = urllib.request.Request(
        ALGOLIA_URL,
        data=json.dumps(payload).encode(),
        headers=HEADERS,
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read())


def parse_grade(hit):
    if hit.get("Grado"):
        return hit["Grado"]
    name = hit.get("boxName", "")
    match = re.search(r"/([ABC])\s*$", name)
    if match:
        return GRADE_MAP.get(match.group(1), match.group(1))
    return ""


def format_price(value):
    return f"{value:,.2f}€".replace(",", "X").replace(".", ",").replace("X", ".")


def map_hit(hit):
    box_id = hit.get("boxId") or hit.get("objectID")
    return {
        "boxId": box_id,
        "title": hit.get("boxName", "").strip(),
        "price": hit.get("sellPrice"),
        "category": hit.get("categoryFriendlyName") or hit.get("categoryName") or "",
        "grade": parse_grade(hit),
        "stockOnline": hit.get("ecomQuantity") or hit.get("inStockOnline") or 0,
        "stores": hit.get("collectionStores") or [],
        "url": f"{PRODUCT_URL}{box_id}",
    }


def fetch_all_laptops():
    hits = []
    page = 0
    while True:
        data = algolia_search(page=page)
        hits.extend(data.get("hits", []))
        page += 1
        if page >= data.get("nbPages", 1):
            break
    products = [map_hit(h) for h in hits]
    products.sort(key=lambda p: (p["price"] or 0, p["title"].lower()))
    seen = set()
    unique = []
    for product in products:
        if product["boxId"] not in seen:
            seen.add(product["boxId"])
            unique.append(product)
    return unique


def write_txt(products, path=OUTPUT_FILE):
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    lines = [
        "PORTÁTILES DISPONIBLES EN CEX ESPAÑA (es.webuy.com)",
        f"Rango de precio: {MIN_PRICE}€ - {MAX_PRICE}€",
        "Filtro: disponibles para compra online",
        f"Fecha de extracción: {now}",
        f"Total de productos: {len(products)}",
        "Fuente: Algolia (catálogo CeX) vía search.webuy.io",
        "=" * 80,
        "",
    ]
    for i, product in enumerate(products, 1):
        stores = ", ".join(product["stores"][:5])
        if len(product["stores"]) > 5:
            stores += f" (+{len(product['stores']) - 5} tiendas más)"
        lines.extend(
            [
                f"{i}. {product['title']}",
                f"   Precio: {format_price(product['price'])}",
                f"   Categoría: {product['category']}",
                f"   Estado: {product['grade'] or 'No especificado'}",
                f"   Stock online: {product['stockOnline']}",
                f"   ID: {product['boxId']}",
                f"   URL: {product['url']}",
            ]
        )
        if stores:
            lines.append(f"   Tiendas con stock: {stores}")
        lines.append("")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def main():
    settings = fetch_algolia_settings()
    print(f"Algolia index: {settings['algoliaIndexName']}")
    products = fetch_all_laptops()
    write_txt(products)
    print(f"Extraídos {len(products)} portátiles -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
