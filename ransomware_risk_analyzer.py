import csv
from collections import Counter, defaultdict
from pathlib import Path

RISK_FILE = Path(__file__).with_name("risk_register.csv")

def rating(score):
    if score >= 20:
        return "Critical"
    if score >= 12:
        return "High"
    if score >= 6:
        return "Medium"
    return "Low"

def main():
    risks = []
    with RISK_FILE.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            likelihood = int(row["likelihood"])
            impact = int(row["impact"])
            inherent = likelihood * impact
            residual = int(row["residual_score"])
            risks.append({
                "id": row["id"],
                "risk": row["risk"],
                "likelihood": likelihood,
                "impact": impact,
                "inherent": inherent,
                "rating": rating(inherent),
                "csf": row["csf_mapping"],
                "residual": residual,
                "residual_rating": rating(residual),
            })

    print("\\nRANSOMWARE RISK ASSESSMENT")
    print("=" * 72)
    print(f"Total risks: {len(risks)}")

    before = Counter(item["rating"] for item in risks)
    after = Counter(item["residual_rating"] for item in risks)
    print("\\nRatings before controls:")
    for level in ("Critical", "High", "Medium", "Low"):
        print(f"  {level}: {before.get(level, 0)}")

    print("\\nExpected ratings after controls:")
    for level in ("Critical", "High", "Medium", "Low"):
        print(f"  {level}: {after.get(level, 0)}")

    print("\\nTop five risks:")
    for item in sorted(risks, key=lambda x: x["inherent"], reverse=True)[:5]:
        print(f"  {item['id']} | {item['risk']} | "
              f"{item['likelihood']} x {item['impact']} = "
              f"{item['inherent']} ({item['rating']})")

    grouped = defaultdict(list)
    for item in risks:
        # Group by the first part of the NIST CSF category code.
        grouped[item["csf"].split(".")[0]].append(item)

    print("\\nAverage risk by CSF category prefix:")
    for function, items in sorted(grouped.items()):
        avg_before = sum(x["inherent"] for x in items) / len(items)
        avg_after = sum(x["residual"] for x in items) / len(items)
        print(f"  {function}: before={avg_before:.1f}, after={avg_after:.1f}, "
              f"risks={len(items)}")

    print("\\nLikelihood x Impact heat map (number of risks):")
    for likelihood in range(5, 0, -1):
        cells = [sum(1 for x in risks
                     if x["likelihood"] == likelihood and x["impact"] == impact)
                 for impact in range(1, 6)]
        print(f"  L={likelihood}: " + " ".join(str(value) for value in cells))
    print("         I=1 2 3 4 5")

    output = Path(__file__).with_name("risk_summary.csv")
    with output.open("w", newline="", encoding="utf-8") as file:
        fields = ["id", "risk", "likelihood", "impact", "inherent",
                  "rating", "csf", "residual", "residual_rating"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(risks)
    print(f"\\nDetailed results saved to: {output.name}")

if __name__ == "__main__":
    main()
