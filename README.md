 ZENITH
 




Zenith is a web-based productivity dashboard developed as the CS50 Final Project. The application combines multiple productivity tools, including a focus timer, a to-do list, a daily checklist, motivational quotes, dark mode, and a weather widget, into a single cohesive interface designed to encourage concentration in a calm and cozy environment. The backend of the application is built using Python and Flask, with SQLite used to persist todo list data, while the frontend is implemented using HTML, CSS, and JavaScript to handle interactivity and user experience. Client side features such as the checklist, motivational quotes, and theme preferences are stored using browser localStorage, while real time weather data is fetched via the OpenWeatherMap API and processed through Flask. This project demonstrates the practical application of CS50 concepts, including web development, database management, API integration, and frontend and backend interaction.

I chose this project because, as a student, I personally struggle to stay focused for long periods of time, and I wanted to build a simple website that I would actually use myself. My goal was to create a calm, distraction free space for studying without unnecessary features or the need to sign up for an account. For this reason, the design prioritizes simplicity, usability, and clarity, using choices such as a single page layout and localStorage for lightweight, user specific state. Through this project, I focused on clearly understanding and applying the core concepts taught in CS50 rather than relying on advanced frameworks, making the project both practical and meaningful to me. This project was developed independently in accordance with CS50’s academic honesty guidelines.
SHORT NOTES:
To enable the weather feature, users must obtain their own OpenWeatherMap API key and add it to the get_weather function inside app.py, as no API keys are included in this submission for security reasons.

API integration was implemented using Flask concepts taught in Week 9, applying them to an external weather service. Some features that I  used in this project such as API integration and localStorage usage, were implemented by extending concepts taught in CS50 using official documentation.