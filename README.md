# Smart Outreach Tool: An AI-Powered Cold Email Generator

<div align = "justify">

In an increasingly competitive world, making meaningful professional connections has become more challenging than ever. Businesses and individuals need a way to cut through the noise and create outreach messages that are not only relevant but also impactful. Crafting the perfect cold email, one that speaks directly to the recipient’s needs while showcasing the sender’s value, demands time, creativity and precision. Yet, in the fast-paced environment of today, there’s a pressing need for automated, intelligent tools that can streamline this process without sacrificing personalization. This is where the fusion of AI, automation, and optimization plays a pivotal role, delivering solutions that not only save time but ensure every email makes a lasting impression.

## Content

- [Overview](#overview)

- [Setup](#setup)

- [Features](#features)

- [Procedure](#procedure)

- [Workflow](#workflow)

- [User Interface](#user-interface)

- [Conclusion](#conclusion)

## Overview

The Smart Outreach Tool is a modern web-based solution that streamlines the process of generating cold emails. It leverages the power of A/B testing, theme customization and cold email generation based on job descriptions. The tool ensures that users can personalize and optimize outreach efforts, improving connection rates and engagement with potential clients. With a user-friendly interface and adjustable dark and light modes, this tool is designed to provide a seamless experience for professional outreach.

## Setup

- **Visual Studio Code:** for development

- **ChatGroq:** for utilizing cloud LLM framework

- **ChromaDB:** for vectore store

- **Streamlit:** for user interface and deployment 

## Features

- **Automated Email Generation:** Generate customized cold emails based on job descriptions.

- **A/B Testing:** Create and compare two email versions to optimize outreach effectiveness.

- **Light and Dark Mode Support:** Toggle between themes to suit user preferences.

- **User-Friendly Interface:** Simple navigation with side options for quick access.

- **Customizable Settings:** Adjust tool settings, including theme and A/B test, to fine-tune your workflow.

## Procedure

**1) Input a Job Posting URL:**

The user enters the career page URL (job posting URL) into the input field on the tool’s interface.

**2) Data Extraction Using LLM (Large Language Model):**

The entered job posting URL is analyzed by the LLM (we used **Llama**), which scrapes and extracts essential details such as:

- Job title

- Required skills

- Job description and responsibilities

**3) Formatting the Extracted Data to JSON:**

The extracted job data is converted into a `JSON` structure to organize it efficiently. This JSON serves as the basis for generating the email content.

**4) Integrating Portfolio Links with Vector Store:**

- A vector store (in our case **Chromadb**) is used to match relevant portfolio links from the user’s profile or stored projects, ensuring the generated email highlights these links effectively.
  
- The portfolio links are retrieved from the vector store and injected into the email content.

**5) A/B Testing via LLM:**

If the user enables `A/B testing`, the LLM generates two variations of the email based on the JSON data:

- **Variation A:** A formal email style focusing on efficiency and professionalism.

- **Variation B:** A more friendly and conversational tone to foster engagement.

**6) Cold Email Generation:**

- The LLM combines the extracted job description, relevant portfolio links, and the selected tone (A/B test or default) to generate a cold email.

- The email content emphasizes the sender's expertise and relevance to the target job, increasing the chances of a positive response.

**7) Displaying the Generated Email:**

The generated email(s) are displayed on the interface in code blocks, making them easy to review, copy, or modify.

**8) Theme Selection:**

Users can switch between `light and dark modes` using the sidebar for a customized experience.

**9) Real-time Rendering:**

All processes are executed and rendered in real-time on the Streamlit interface, ensuring a seamless and dynamic user experience.

## Workflow

<div align = "center">
  <img src = "https://github.com/user-attachments/assets/88e5fee6-381d-4d30-a535-243b27ebba10" alt = "workflow" width = 50%>
</div>

## User Interface

**1. Main User Interface**

The user interface provides easy navigation and access to all core features, including email generation and theme switching.

<div align = "center">
  <img src = "https://github.com/user-attachments/assets/33c2ef30-ef23-4dcc-9149-d29dbb17c0b5" alt = "workflow" width = 50%>
</div>

**2. A/B Testing**

With A/B testing, users can generate two different versions of emails to analyze which version performs better.

<div align = "center">
  <img src = "https://github.com/user-attachments/assets/d1cc3a0f-2c3c-441d-8fcb-9dad4eb883e9" alt = "workflow" width = 50%>
</div>

**3. Theme Selection**

The tool’s theme selection offers two modes namely light and dark, based on user needs and comfort.

<div align = "center">
  <img src = "https://github.com/user-attachments/assets/73b36fd1-8205-448b-adb7-ca17ad549ff2" alt = "workflow" width = 50%>
</div>

## Conclusion

The Smart Outreach Tool simplifies the process of creating personalized cold emails, improving outreach efficiency for businesses. With A/B testing and theme switching, users can tailor their approach and increase engagement with potential clients. Its clean architecture and real-time rendering make it a reliable and effective solution for professional outreach efforts.

</div>

## Credits

Codebasics: Youtube channel

## License

This project is licensed under the MIT License.
