# Brand Folder

Brand Folder is a platform to create news content posts that come on Instagram. With a focus on simplicity and efficiency, Brand Folder empowers users to minimise the efforts in content creation.

![Demo Video](<Brand Folder Demo.gif>)

## Solutions We Provide

### 1. Editor
Brand Folder offers a versatile editor capable of generating images in a matter of seconds. With intuitive controls and customizable options, users can tailor their visuals to suit their specific needs with ease.

### 2. Chrome Extension
Our Chrome Extension seamlessly integrates with your browser, allowing you to capture web content directly into the editor with just a single click. Say goodbye to manual content gathering and hello to streamlined workflow.

### 3. News
Stay informed without the hassle of scouring the web for news articles. Brand Folder fetches news content directly to the platform, keeping you up-to-date with the latest information relevant to your interests.

### 4. Customization
Tailor your profile and content according to your brand guidelines with Brand Folder's customization features. Whether it's branding elements, templates, or post layouts, you have the flexibility to create a cohesive brand identity effortlessly.

## Backend Repository
This repository contains all the API endpoints and functionalities that power Brand Folder.

- For the frontend counterpart, please refer to [Brand Folder - Frontend](https://github.com/VanshWadhwa/brandfactory-frontend)
- For the chrome extension counterpart, please refer to [Brand Folder - Chrome Extension](https://github.com/VanshWadhwa/brandfolder-chrome-extension)

## Creating a Post
When creating a post, users can customize various aspects using the following options:

- **Image Source**: Choose between uploading an image or providing a URL.
- **Crop Type**: Select the preferred cropping method for images.
- **Title Text Position**: Position the title text at the top, center, or bottom of the image.
- **Title Text Alignment**: Align the title text as justified, centered, or left-aligned.
- **Additional Features**: Add gradient, branding, or title text to the image.
- **Content Analysis**: Optionally analyze content for important keywords.


## User Accounts and Onboarding
Users can create accounts and undergo onboarding to create their own brand kits and templates. Additionally, users have the flexibility to switch between multiple templates for post creation, ensuring versatility and creativity.

## Tech Stack
- Django REST Framework (DRF) and Django for APIs
- Python Imaging Library (PIL) for image manipulation and generation
- Spacy for Natural Language Processing (NLP)
- NEWS API for news extraction

## API Endpoints
- `/admin/`: Django admin panel
- `/api/v1/users/`: User-related endpoints
- `/posts/`: Endpoints related to post creation and management
- `/news/`: Endpoints for accessing news content
- `/`: Root URL including additional endpoints provided by the router


Sure, here's the section on installing the backend:

## Backend Installation

To set up the backend for Brand Folder, follow these simple steps:

### 1. Installing Dependencies

First, navigate to the project directory and install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

This command will install all the necessary packages listed in the `requirements.txt` file.

### 2. Running the Server

Once the dependencies are installed, you can start the Django server by running the following command:

```bash
python manage.py runserver
```

This command will launch the development server, allowing you to access the backend API endpoints locally.

Now you're all set to start using Brand Folder's backend functionalities. Happy coding!

Feel free to explore the codebase and contribute to making Brand Folder even better!

[Frontend LINK]: # (Insert frontend repository link here)