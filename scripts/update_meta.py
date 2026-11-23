from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import httpx

OUTPUT_PATH = Path("JsonEndpointMetaProvider.json")


def fetch_live_meta() -> dict:
    """
    Replace or extend this function with your live PoE2 data source
    (e.g., poe.ninja / poe2scout API or your own scraper).
    For now, it preserves your existing 10-class data and updates the timestamp.
    """
    if OUTPUT_PATH.exists():
        data = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    else:
        data = {"source": "poe2_live_meta", "mod_stats": [], "mod_cooccurrence": []}

    data["source"] = f"poe2_live_meta_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M')}"
    return data


def main() -> None:
    payload = fetch_live_meta()
    OUTPUT_PATH.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        f"Updated {OUTPUT_PATH} | Mods: {len(payload.get('mod_stats', []))} "
        f"| Pairs: {len(payload.get('mod_cooccurrence', []))}"
    )


if __name__ == "__main__":
    main()
