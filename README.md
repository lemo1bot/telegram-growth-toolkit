# 🚀 Telegram Growth Toolkit (All-In-One)

[![Twitter Follow](https://img.shields.io/twitter/follow/bank_of_eth?style=social)](https://x.com/bank_of_eth)

**Follow me for more tools: [https://x.com/bank_of_eth](https://x.com/bank_of_eth)**

---

## Overview
A powerful, safe, and open-source toolkit to grow your Telegram setup.
**Features:**
1.  **Scraper:** Extract members from any public group.
2.  **Adder:** Add those members to *your* group (Safe Mode included).
3.  **Mass DM:** Send messages to your scraped list.

## 🛠 Installation

1.  **Download the tool:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/telegram-toolkit.git
    cd telegram-toolkit
    ```

2.  **Install requirements:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup API Keys:**
    - Go to [my.telegram.org](https://my.telegram.org) and get your `API_ID` and `API_HASH`.
    - Rename `.env.example` to `.env` and paste your keys:
      ```ini
      API_ID=123456
      API_HASH=abcdef123456...
      PHONE=+1234567890
      ```

## 🚀 How to Use (Easy Guide)

### Step 1: Login
Run the manager to log in to your account.
```bash
python manager.py
```

### Step 2: The "All-In-One" Command
This is the magic command. It will scrape a group and add the members to your group automatically.
```bash
python main.py
```
- **Source Group:** Paste the link of the group you want to *steal* members from.
- **Target Group:** Paste the link of *your* group.
- **Sit back:** The tool will scrape the users and start adding them one by one.

---

### ⚠️ Safety Warning
- **Adding Speed:** The tool waits **60-120 seconds** between adds to prevent bans. **DO NOT SPEED THIS UP.**
- **Privacy:** If a user has "Privacy Settings" enabled, the tool will **[SKIP]** them automatically.
- **Flood Errors:** If you see `PeerFloodError`, stop the tool and wait 24 hours.

---

## 📢 Mass DM (Optional)
If you want to send messages instead of adding members:
1.  Edit `message.txt` with your text.
2.  Run:
    ```bash
    python mass_dm.py
    ```

---

**Made with ❤️ by Bank of Eth**
**🐦 Follow for updates: [https://x.com/bank_of_eth](https://x.com/bank_of_eth)**
