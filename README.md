# Smart Recycling Assistant

**Term Project Proposal and Implementation**

Smart Recycling Assistant is a simple web application that helps users find general information about sorting and disposing of common waste items. Users can search for an item, browse waste categories, read preparation and disposal instructions, save favorites, and review recent searches.

## 1. Project Overview

Recycling rules can be confusing, especially for people who are new to Korea. This project collects basic recycling guidance in one place so users can quickly look up common items and learn how to prepare them before disposal.

## 2. Main Features

- **Search Waste:** Search by item name, category, or keyword.
- **Recycling Information:** View preparation steps, disposal guidance, and useful tips.
- **Waste Categories:** Browse items by Plastic, Paper, Glass, Metal, Organic, General Waste, and Special Waste.
- **Favorite List:** Save frequently checked items during the current app session.
- **Search History:** Review recent searches during the current app session.
- **About Page:** Read the project purpose, technologies, and limitations.

## 3. Technologies

- Python 3.10 or newer
- Streamlit
- JSON for storing the sample waste-item information

## 4. Project Structure

```text
smart-recycling-assistant/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── data/
    └── waste_items.json
```

## 5. How to Run the Project

### Step 1: Install Python

Install Python 3.10 or newer from [https://www.python.org/downloads/](https://www.python.org/downloads/). During installation on Windows, select **Add Python to PATH**.

### Step 2: Download the project

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/smart-recycling-assistant.git
cd smart-recycling-assistant
```

Alternatively, download the repository ZIP from GitHub and extract it.

### Step 3: Install the required library

Open a terminal in the project folder and run:

```bash
python -m pip install -r requirements.txt
```

### Step 4: Start the application

```bash
python -m streamlit run app.py
```

A browser tab should open with the application. If it does not, copy the local URL printed in the terminal (usually `http://localhost:8501`) into a browser.

## 6. How to Use

1. Choose **Search Waste** from the sidebar.
2. Enter an item name or keyword, such as `plastic bottle`, `paper`, or `can`.
3. Open a result to see its category, preparation steps, disposal instructions, and tip.
4. Select **Add to favorites** to save an item.
5. Open **Waste Categories** to browse by material.
6. Open **Favorites** or **Search History** to review items you have used.

## 7. Data

The sample item information is stored in `data/waste_items.json`. Each item includes:
- `name`: item name
- `category`: waste category
- `keywords`: alternative search terms
- `recyclable`: whether recycling or a special collection may be available
- `preparation`: how to prepare the item
- `disposal`: general disposal guidance
- `tip`: an additional reminder

More items can be added by following the same JSON structure.

## 8. Testing Checklist

- [ ] The application starts with the Streamlit command.
- [ ] Searching for `plastic bottle` returns a matching item.
- [ ] Searching for an unknown word shows a no-results message.
- [ ] Category selection filters the displayed items.
- [ ] Add to favorites and remove from favorites work.
- [ ] Search history records recent search terms.
- [ ] Clear search history removes the displayed history.

## 9. Limitations and Future Work

The current version uses a small sample JSON database and general recycling guidance. Recycling rules vary by location, so users should confirm local instructions. Favorites and search history are stored in the Streamlit session and are not permanent across separate sessions.

A possible future improvement is AI-based waste image recognition. This is not included in the current basic version; it can be developed after the core functions are stable.

## 10. License

This project is released under the MIT License. See [LICENSE](LICENSE).

## 11. Author

- **Author:** Add your name here
- **Course:** Add your course name here
- **Project:** Smart Recycling Assistant
