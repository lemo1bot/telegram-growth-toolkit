import asyncio
import os
import sys

# Import custom modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import scraper
import add_members

async def main():
    print("========================================")
    print("   TELEGRAM ALL-IN-ONE AUTOMATION")
    print("========================================")
    
    # Step 1: Subscribe/Scrape
    print("\n[STEP 1] SCRAPE MEMBERS")
    source_link = input("Enter Source Group Link (to scrape from): ").strip()
    
    if not source_link:
        print("Source link required.")
        return

    print(f"Scraping {source_link}...")
    scrape_result = await scraper.scrape_members(source_link, "members.csv")
    
    if scrape_result['status'] != 'success':
        print(f"Scraping Failed: {scrape_result.get('message')}")
        return
    
    print(f"Successfully scraped {scrape_result['count']} members to 'members.csv'.")

    # Step 2: Add Members
    print("\n[STEP 2] ADD MEMBERS")
    target_link = input("Enter Target Group Link (to add members TO): ").strip()
    
    if not target_link:
        print("Target link required.")
        return

    print("------------------------------------------------")
    print("WARNING: Adding members takes time (1-2 mins per person).")
    print("Do not close this window.")
    print("------------------------------------------------")
    confirm = input("Type 'YES' to start adding: ").strip()
    
    if confirm != "YES":
        print("Operation Cancelled.")
        return

    print(f"Adding members to {target_link}...")
    add_result = await add_members.add_members_to_group(target_link, "members.csv")

    if add_result['status'] == 'success':
        print(f"\nDONE! Successfully added {add_result['count']} members.")
    else:
        print(f"\nStopped with error: {add_result.get('message')}")

if __name__ == "__main__":
    asyncio.run(main())
