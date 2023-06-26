# YouTube Channel Scraper

This project is a YouTube channel scraper that retrieves subscriber counts and niches for a list of YouTube channels. It utilizes the YouTube Data API, SocialBlade, and a niche generation function to gather the required data.

## Features

- Retrieves subscriber counts for YouTube channels using the YouTube Data API.
- Scrapes niche information for each channel using a ChatGPT or an external API/service.
- Supports asynchronous requests for efficient processing.
- Utilizes error handling to handle potential issues during scraping.
- Provides optimized code for improved performance and scalability.

## Prerequisites

Before running the script, make sure you have the following:

- YouTube Data API Key: Obtain an API key from the Google Cloud Console and replace `'YOUR_API_KEY'` in the code with your actual API key.
- Service Account JSON file: Generate a service account JSON file with access to the YouTube Data API and replace `'PATH_TO_YOUR_SERVICE_ACCOUNT_JSON_FILE'` in the code with the path to your JSON file.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/youtube-channel-scraper.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Prepare a list of YouTube channel URLs or channel IDs in a text file, with one channel per line.

2. Run the scraper script:

   ```shell
   python scraper.py --input <path_to_input_file> --output <path_to_output_file>
   ```

   Replace `<path_to_input_file>` with the path to your input file and `<path_to_output_file>` with the desired path for the output file.

3. The script will retrieve the subscriber counts and niches for each channel and save the results to the specified output file.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and adapt the code according to your needs.

## Disclaimer

Please note that web scraping should be performed responsibly and in compliance with the terms of service of the websites being scraped. Use this tool at your own risk and ensure that you are familiar with and adhere to the relevant website's terms of service.

## Credits

This project is inspired by the need to gather YouTube channel data efficiently. Special thanks to the developers and contributors of the used libraries and APIs.

---

Feel free to customize the README file based on your project's specific requirements and add any additional sections or instructions as needed.
