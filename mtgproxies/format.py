"""String formatting utils."""
from __future__ import annotations


def format_print(card_name: str | dict, set_id: str = None, collector_number: str = None) -> str:
    # Si card_name es un diccionario
    if isinstance(card_name, dict):
        card_name_value = card_name.get("name", "UNKNOWN")  # Obtener el nombre de la carta
        set_id = card_name.get("set", set_id or "UNKNOWN")  # Obtener el set o asignar 'UNKNOWN'
        collector_number = card_name.get("collector_number", collector_number or "N/A")  # Obtener número de coleccionista
    else:
        # Si card_name es una cadena (no un diccionario), lo tratamos directamente
        card_name_value = card_name

    # Si set_id sigue siendo None, le asignamos un valor por defecto
    if set_id is None:
        set_id = "UNKNOWN"

    return f"'{card_name_value} ({set_id.upper()}) {collector_number}'"



color_names = {
    "W": "white",
    "U": "blue",
    "B": "black",
    "R": "red",
    "G": "green",
}


def format_colors(colors: list[str]) -> str:
    if len(colors) == 0:
        return "colorless"
    return listing([color_names[c] for c in colors], ", ", " and ")


def listing(items: list[str], sep: str, final_sep: str, max_items: int = None) -> str:
    if len(items) == 0:
        return ""
    if len(items) == 1:
        return items[0]
    if max_items is None or len(items) <= max_items:
        return sep.join(items[:-1]) + final_sep + items[-1]
    else:
        return sep.join(items[:max_items] + ["..."])


def format_token(card: dict) -> str:
    # Double faced cards
    if "colors" not in card:
        return format_token(card["card_faces"][0]) + " // " + format_token(card["card_faces"][1])

    s = ""

    # P/T
    if "power" in card:
        s += f"{card['power']}/{card['toughness']} "

    # Colors
    s += format_colors(card["colors"]) + " "

    # Type line
    s += card["type_line"]

    # Oracle text
    if card["oracle_text"] != "":
        s += f" with '{card['oracle_text']}'"

    return s
