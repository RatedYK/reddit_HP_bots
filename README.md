# Reddit Harry Potter Bots Collection

Welcome to the Reddit Harry Potter Bots Collection! This repository contains a set of Python bots inspired by the magical world of Harry Potter, designed to interact with the popular website [Reddit](https://www.reddit.com/). These bots will bring a touch of wizardry to your Reddit experience. Explore the different bots and have fun engaging with the Harry Potter universe!

## Bots Overview

1. **Muggle Bot**: This bot posts submissions about the wizarding world, providing interesting insights and updates for muggles who want to stay informed.
2. **True Wizard Bot**: With a keen eye for specific keywords, the True Wizard Bot replies to submissions and comments that match its criteria. Additionally, it summons the third bot when it encounters the secret phrase "!enemies of the heir beware".
3. **The Heir to SS Bot**: Known for throwing insults related to muggles, The Heir to SS Bot utilizes "The Evil Insult Generator API" to craft witty and entertaining replies.
4. **Lord Voldemort Bot**: Beware, for the infamous Lord Voldemort himself will appear whenever his name is mentioned. This interactable bot allows users to post under his persona or choose not to.

## Setup

To run these bots on your own, follow the steps below:

1. Create your own Reddit account if you don't have one already by visiting the [Reddit website](https://www.reddit.com/).
2. Generate the required API credentials by following the instructions provided on the [Reddit API documentation](https://www.reddit.com/dev/api/) to obtain the necessary `client_id`, `client_secret`, `user_agent`, `username`, and `password`.
3. Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/your-username/reddit-harry-potter-bots.git
   ```
4. Navigate to the project directory:
   ```
   cd reddit-harry-potter-bots
   ```
5. Create a `.env` file in the project directory and provide the following information:
   ```
   CLIENT_ID=your-reddit-api-client-id
   CLIENT_SECRET=your-reddit-api-client-secret
   USER_AGENT=your-reddit-api-user-agent
   USERNAME=your-reddit-username
   PASSWORD=your-reddit-password
   ```
   Make sure to replace the placeholder values with your actual Reddit API credentials and account information.
6. Install the required Python dependencies. It's recommended to use a virtual environment:
   ```
   python3 -m venv env
   source env/bin/activate   # For Linux/MacOS
   env\Scripts\activate      # For Windows
   pip install -r requirements.txt
   ```
7. Run the desired bot script using Python. For example, to run the Muggle Bot:
   ```
   python muggle_bot.py
   ```

Make sure to run each bot script individually, as they serve different purposes and functions.

## Contributions

Contributions to this repository are welcome! If you have any improvements, bug fixes, or new ideas for the bots, feel free to submit a pull request. We encourage a collaborative and magical community, so don't hesitate to join in!

Please ensure that any contributions align with the theme of the project and maintain the professional yet tongue-in-cheek nature of the repository.

Happy botting and may your journey through the Reddit Harry Potter universe be filled with enchantment!