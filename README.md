# 🪙 Crypto Tracker — Django + JS + API Based Real-Time Dashboard

A beautifully designed **Crypto Price Tracker Dashboard** built using  
**Django + CoinGecko API + JavaScript**, showing **live USD prices**,  
24/7 updates, and a modern UI inspired by premium fintech dashboards.

---

# 🚀 Project Working Flow

## 1. Data Fetching (Backend)
The backend uses a **Django Management Command** to fetch real-time crypto data.

| Process | Description |
|:--------|:------------|
| API Call | Fetches latest prices from CoinGecko |
| Coins Tracked | Bitcoin, Ethereum, Dogecoin, Litecoin, XRP |
| Fields Stored | Price, Symbol, Market Cap, Last Update |
| Schedule | Can be automated using CRON / Windows Task Scheduler |

---

## 2. Database Storage
After fetching API data:

| Field | Purpose |
|:-------|:-------------------------------|
| `coin_id` | Unique crypto ID (e.g., bitcoin) |
| `symbol` | BTC, ETH, LTC, DOGE |
| `name` | Full crypto name |
| `current_price` | LIVE USD price |
| `formatted_price` | ₹XX,XXX.XX formatted price |
| `market_cap` | Current market cap |
| `last_updated` | Timestamp |

Clean, structured, and easy to read.

---

## 3. Dashboard (Frontend)
The crypto dashboard is **fully responsive** and loads data with JavaScript.

| Section | Description |
|:---------|:-----------------------|
| **Crypto Cards** | Each card shows live USD price |
| **Refresh Button** | Manually fetches API data |
| **Price Color** | Green = Up, Red = Down |
| **Smooth UI** | Modern colors, animations |

---

## 4. Live Price Cards
For every crypto, the card displays:

- Symbol → BTC  
- Name → Bitcoin  
- Price → **₹80,11,021.96**  
- Color based on price movement  
- Soft animations & glowing hover effect  

| Visual Element | Description |
|:---------------|:------------|
| **Green price** | Price increased since last update |
| **Red price** | Price decreased |
| **Card hover** | Smooth 3D floating effect |

---

## 5. API Response Flow
```
JavaScript → /api/coins/ → Django API View → Database → Response → UI Update
```

The system does **not** reload the full page — only the card updates.

---

# 🧩 Features Overview

| Feature | Description | Status |
|:---------|:----------------------------------------|:-------:|
| Real-Time Prices | Fetches USD prices live | ✔ |
| API Integration | CoinGecko Market API | ✔ |
| Django Models | Structured DB for coins | ✔ |
| Dynamic UI | JS-powered card rendering | ✔ |
| Color Price Indicator | Green/Red price change | ✔ |
| Cron/Task Support | Auto-update backend | ✔ |
| Responsive Design | Works on mobile & desktop | ✔ |
| INR Conversion | Optional toggle support | ❌ (Not enabled) |

---

# 🗂 Folder Structure

```
crypto-tracker/
│
├── tracker/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── management/
│       └── commands/
│           └── fetch_prices.py
│
├── templates/
│   └── coins.html
│
├── crypto_backend/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

---

# 🎨 UI Highlights
- Dark theme inspired by GitHub + Binance  
- Floating cards  
- Animated footer  
- Clean typography (Poppins)  
- Professional price formatting  
- Looks good on all devices  

---

# 🔧 How to Run the Project

### 1. Create virtual env
```sh
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies
```sh
pip install -r requirements.txt
```

### 3. Run Django server
```sh
python manage.py runserver
```

### 4. Fetch live prices
```sh
python manage.py fetch_prices
```

---

# ⭐ Future Improvements

| Improvement | Details |
|:-----------|:---------|
| Auto refresh | Update UI every 30 seconds |
| Graphs | Add price history charts |
| Add 50+ coins | Expand selection |
| User accounts | Track your portfolio |
| Alerts | Price drop/increase alerts |

---

# 👨🏻‍💻 Developer

**Designed & Developed by Anuj Patil**  
GitHub: **https://github.com/Andyhub99**

---




# 🌟 End

A simple, elegant, and powerful **Crypto Tracking Dashboard** made with love,  
perfect for learning Django, APIs, and real-time UI rendering.
