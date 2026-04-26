def format_dd_mm_yyyy(iso_text: Optional[str]) -> str:
    if not iso_text:
        return ""
    try:
        if len(iso_text) == 10 and iso_text[4] == "-":
            return datetime.strptime(iso_text, "%Y-%m-%d").strftime("%d-%m-%Y")
        iso2 = parse_any_date_to_iso(iso_text)
        if iso2:
            return datetime.strptime(iso2, "%Y-%m-%d").strftime("%d-%m-%Y")
    except Exception:
        pass
    return iso_text
