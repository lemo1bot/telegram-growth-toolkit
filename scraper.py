from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import config
import csv
import asyncio
import os

async def scrape_members(group_link, output_file="members.csv"):
    client = TelegramClient(config.SESSION_PATH, config.API_ID, config.API_HASH)
    results = [] # Return value
    
    try:
        await client.connect()
        if not await client.is_user_authorized():
            return {"status": "error", "message": "Not authorized. Run manager.py first."}

        print(f"Joining/Accessing group: {group_link}")
        try:
            entity = await client.get_entity(group_link)
        except Exception as e:
            return {"status": "error", "message": f"Error accessing group: {e}"}

        print(f"Fetching members from {entity.title}...")
        
        all_participants = []
        limit = 1000 
        
        async for participant in client.iter_participants(entity, limit=limit):
            all_participants.append(participant)

        # Saving to CSV
        with open(output_file, "w", encoding="UTF-8", newline="") as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(["User ID", "Username", "First Name", "Last Name", "Access Hash"])
            
            for user in all_participants:
                writer.writerow([
                    user.id,
                    user.username or "",
                    user.first_name or "",
                    user.last_name or "",
                    user.access_hash
                ])
                
        return {"status": "success", "count": len(all_participants), "file": output_file}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        await client.disconnect()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python scraper.py <group_link>")
        sys.exit(1)
    
    target_group = sys.argv[1]
    asyncio.run(scrape_members(target_group))
