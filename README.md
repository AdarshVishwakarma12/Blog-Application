# Blog Application

Welcome to the Blog Application! This project is a modern, feature-packed platform built using Django, Python, and a powerful tech stack. Designed for creating and sharing content, it offers a seamless experience for both developers and users, with easy deployment via Docker and a clean, responsive design.

## Features
- Create, read, update, and delete (CRUD) blog posts.
- User authentication and authorization.
- Commenting system for posts.
- Responsive design using HTML and CSS.
- Dockerized setup for seamless deployment.
- SQL database for efficient data storage and management.

## Prerequisites
Ensure the following tools are installed on your local machine:
- Docker
- Docker Compose
- Git
- A modern web browser

## Getting Started
Follow these steps to run the project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/AdarshVishwakarma12/Blog-Application.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Blog-Application
   ```

3. Start the Docker service on your machine.

4. Build and run the Docker containers:
   ```bash
   docker-compose up -d --build
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:8001/blog
   ```

6. Bingo! The application is now running locally.

## Project Structure
The project follows a modular structure for scalability and ease of maintenance:
```
Blog-Application/
├── project_blog/          # Core blog application
│   ├── AppBlog
│   ├── project_blog
│   ├── db.sqlite3
│   ├── manage.py
├── .gitignore        
├── Dockerfile         # Docker configuration
├── LICENSE            # License file
├── README.md          # Project documentation
├── docker-compose.yml # Docker Compose setup
└── requirements.txt   # Python dependencies
```

## Contributions
Contributions are welcome! If you have ideas for additional features or improvements, feel free to:
- Fork the repository.
- Create a feature branch.
- Submit a pull request with your changes.

## License
This project is open-source and available under the [Apache License Version 2.0, January 2004](http://www.apache.org/licenses/).

## Contact
For queries or support, reach out to me on GitHub: [Adarsh Vishwakarma](https://github.com/AdarshVishwakarma12).

Happy learning and coding!