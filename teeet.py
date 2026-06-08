import json
import csv

def extract_openapi_to_csv(openapi_file, output_csv):
    with open(openapi_file, "r", encoding="utf-8") as f:
        spec = json.load(f)

    rows = []

    for path, methods in spec.get("paths", {}).items():
        for method in methods:
            rows.append({
                "method": method.upper(),
                "path": path
            })

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["method", "path"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved {len(rows)} endpoints to {output_csv}")


extract_openapi_to_csv("openapi.json", "api_endpoints.csv")
