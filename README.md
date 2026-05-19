Telegram Bot "Astana Life" — An Interactive Guide to the Capital

Project Overview:
"Astana Life" is a user-friendly and responsive Telegram bot designed for both residents and visitors of Astana. The bot helps users quickly discover interesting locations to visit, the best places to eat, upcoming city events, and the main attractions of the capital.
 Key Features

    Categorized Directory: A well-structured menu divided into logical sections: Parks, Cafes/Restaurants, Sights, Shopping, Culture, and Entertainment.

    Interactive Place Cards: Instead of sending plain text, the bot provides users with visually appealing cards featuring high-quality images and formatted Markdown descriptions.

    One-Click Navigation: Every location includes an Inline button with a direct link to 2GIS, allowing users to instantly build a route from any point in the city.

    Events Calendar: Up-to-date information about upcoming exhibitions, theater plays, and sports matches.

    Smart Data Architecture: All location data is isolated inside a dedicated file (places_data.py). This allows the project to scale easily and support hundreds of new locations without altering the bot's core logic.

🛠 Tech Stack

    Programming Language: Python 3.12

    Telegram API Library: pyTelegramBotAPI (telebot)

    Architectural Pattern: Separation of concerns — keeping keyboard layouts and message handlers (logic) completely separate from the content (dictionaries).

 Project Structure

    main.py — The entry point of the application containing bot initialization and universal text message handlers.

    keyboards.py — A dedicated module for generating static Reply keyboards and dynamic Inline buttons.

    places_data.py — The content repository storing local file paths to media, Markdown-formatted descriptions, and geo-links.

    images/ — A directory containing optimized graphic assets for stable local image loading.

 Core Competencies Gained:

    Implementing and managing asynchronous-like long-polling connections with the Telegram Bot API.

    Designing clean code architecture to eliminate redundant and repetitive if-elif conditional blocks.

    Managing local file systems within a Python environment to ensure media content reliability.

    Designing intuitive user interfaces using Markdown styling and interactive inline components.
