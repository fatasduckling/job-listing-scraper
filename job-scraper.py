import requests
import csv
from datetime import datetime

# -----------------------------------------------
# CONFIG — edit these to customize your search
# -----------------------------------------------
KEYWORDS   = ["intern", "junior", "entry level"]   # filter job titles
CATEGORIES = ["software-dev", "data"]               # remotive.com categories
OUTPUT_CSV = "jobs.csv"
# -----------------------------------------------

BASE_URL = "https://remotive.com/api/remote-jobs"

def fetch_jobs(category):
    """Fetch jobs from Remotive API for a given category."""
    resp = requests.get(BASE_URL, params={"category": category})
    if resp.status_code != 200:
        print(f"  ⚠️  Failed to fetch category '{category}' (status {resp.status_code})")
        return []
    return resp.json().get("jobs", [])

def matches_keywords(title, keywords):
    """Return True if any keyword appears in the job title."""
    title_lower = title.lower()
    return any(kw.lower() in title_lower for kw in keywords)

def save_to_csv(jobs, filename):
    """Save job list to a CSV file."""
    if not jobs:
        print("No jobs to save.")
        return
    fields = ["title", "company_name", "candidate_required_location", "url", "publication_date"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for job in jobs:
            writer.writerow({k: job.get(k, "") for k in fields})
    print(f"\n✅ Saved {len(jobs)} jobs to '{filename}'")

def main():
    print(f"🔍 Searching for: {KEYWORDS}")
    print(f"📂 Categories: {CATEGORIES}\n")

    all_matches = []

    for category in CATEGORIES:
        print(f"Fetching '{category}' jobs...")
        jobs = fetch_jobs(category)
        print(f"  Found {len(jobs)} total — filtering by keywords...")

        matches = [j for j in jobs if matches_keywords(j.get("title", ""), KEYWORDS)]
        print(f"  ✅ {len(matches)} matched\n")
        all_matches.extend(matches)

    # Remove duplicates by job ID
    seen = set()
    unique = []
    for j in all_matches:
        if j["id"] not in seen:
            seen.add(j["id"])
            unique.append(j)

    # Print results to terminal
    print(f"{'='*60}")
    print(f"  🎯 {len(unique)} matching jobs found")
    print(f"{'='*60}")
    for j in unique:
        print(f"\n📌 {j['title']}")
        print(f"   🏢 {j['company_name']}")
        print(f"   📍 {j.get('candidate_required_location', 'Not specified')}")
        print(f"   📅 {j.get('publication_date', '')[:10]}")
        print(f"   🔗 {j['url']}")

    # Save to CSV
    save_to_csv(unique, OUTPUT_CSV)

if __name__ == "__main__":
    main()
