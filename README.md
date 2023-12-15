# Flask Blog and Contact Application

## Overview
This Flask application serves as a platform for displaying blog posts and handling contact form submissions via email. It fetches blog data from an external API and uses SMTP to send emails from the contact form.

## Features
- **Blog Display**: Fetches and displays blog posts from an external API.
- **Dynamic Post Pages**: Generates pages for individual blog posts based on their ID.
- **Contact Form**: Allows users to submit messages through a contact form.
- **Email Notifications**: Sends submitted messages to a specified email address using SMTP.
  
## Usage
- **Adding New Blog Entries**: Navigate to the entry form, where you can input details including location, opening and closing times, and ratings for coffee, wifi, and power outlets.
- **Viewing Blog Posts**: Visit the homepage to see all blog entries.
- Location URL, open/close times, and ratings have been added as required features in the blog entry form.
- Validation ensures that all fields are filled out correctly, including checking the validity of the URL.
  
## Routes
- `/`: Homepage displaying all blog entries.
- Additional routes as per your application's functionality.

## Contributing
Contributions and suggestions are welcome. Please follow the standard fork and pull request process for contributions.

## Acknowledgments
- Flask and Python community for continuous support.
