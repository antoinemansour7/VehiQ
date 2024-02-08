# Matter-soen341projectW2024

## Table of Contents

- [Project Description](#project-description)
- [Primary Users and Use Cases](#primary-users-and-use-cases)
- [Team Member Roles](#team_member-roles)
- [Project Approach and Technology](#project-approach-and-technology)
  - [Backend Framework Evaluation](#backend-framework-evaluation)
  - [Frontend Framework Evaluation](#frontend-framework-evaluation)
- [Integration and Interoperability](#integration-and-interoperability)
- [Security Considerations](#security-considerations)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [User Stories](#user-stories)
- [Conclusion](#conclusion)

## Project Description

Our project, a cutting-edge Car Rental Platform, aims to revolutionize the way users rent cars for personal use. By leveraging the latest web technologies, we offer a seamless, intuitive, and comprehensive car rental experience. Users can effortlessly browse a wide selection of vehicles, read detailed reviews from previous customers, and choose the perfect car that suits their needs and preferences. Our secure and straightforward payment process ensures a hassle-free rental experience from start to finish.

## Primary Users and Use Cases

#### Customers

- **Browse Vehicles for Rent**: Access a catalog of vehicles, filtering by type, category, and price range.
- **Start a Reservation**: Specify rental details like location and dates to view available vehicles and add optional equipment.
- **View/Modify/Cancel Reservation**: Manage reservations with the flexibility to adjust or cancel as needed.
- **Find a Branch**: Locate the nearest rental branch using postal code or airport information.
- **Rating and Review**: Provide feedback on vehicles and the rental experience.

#### Customer Service Representatives (CSRs)

- **Check-in Process**: Assist customers with new or existing reservations, verify identification, review rental agreements, and process payments.
- **Check-out Process**: Inspect vehicles, ensure rental agreement compliance, process final billing, and confirm return completion in the system.

#### System Administrators

- **CRUD Operations on Vehicles**: Manage vehicle inventory.
- **CRUD Operations on User Accounts**: Handle user account management.
- **CRUD Operations on Reservations**: Oversee reservation records.

## Team Member Roles

#### Julia - UI/UX Designer

Julia enhances user experience, bringing her extensive experience with HTML, CSS, and JavaScript to the table. Her creativity and innovative approach drive the aesthetic and functional design of our user interface, all while making sure that the user requirements are met.

#### Cristina - Frontend Lead

Cristina ensures that the implemented UI is coherent in every view and that it is easy for the user to interact with the platform. Her experience with the chosen frontend framework, Vue.js and her meticulous approach to implementation makes her an asset to the team

#### Jackson- Frontend Integration Developer

Jackson's previous work involves creating an Animal Adoption Agency Website and Financial Counseling Website from scratch using HTML,CSS, JavaScript and PHP. He ensures that the website not only looks great but also provides a seamless experience for our users. From designing layouts to implementing interactive features with JavaScript, he's passionate about creating engaging web experiences. His familarity with backend development such as PHP will allow him to connect the front end of the car rental website with the backend systems responsible for managing and storing data related to car inventory, availability, and bookings.

#### Antoine - Backend Developer

Antoine's role involves developing server-side applications. He will focus on integrating Django, along side other backend technologies to create a solialongside the car rental platform. His goal is to maintain flawless application logic to ensure the system's efficiency and reliability. Furthermore, he will work closely with front-end developers to maintain the desired user experience by providing the necessary backend functionalities.

#### André - Backend Developer

André's role is to focus on the backend side of the car rental web application. His focus will be to create an efficient database to ensure a secure and enjoyable user experience by creating and utilizing efficient models and database queries.

#### Leiticia - Backend Developer

As a Backend Developer, I am focused on developing robust and scalable server-side applications. My work involves integrating Django with other backend technologies to create a solid foundation for our car rental platform.

## Project Approach and Technology

### Project Overview

We aim to create a user-friendly Car Rental Application that serves as an interface between customers and rental services, streamlining the rental process.

### Development Methodology

Our Agile methodology allows us to adapt to changes quickly, focusing on iterative development and customer feedback.

### Technology Stack

#### Backend Framework Evaluation

- **Django**: Chosen for its comprehensive features and rapid development capabilities, ideal for our secure and scalable web application
- **Node.js**: Offers great performance for I/O intensive operations, suitable for real-time features.
- **ASP.NET**: Known for its robustness in enterprise scenarios, it provides strong security and performance.

<ins><br>**Django**<br></ins>
**Description:** <br>
Django is a free open-source Python-based web framework that runs on a web server. It was developed to make the web developement process fast and easy.
Build by experienced developers, it takes care of much of the hassle of web developement, so you can focus on writting your app without needing to reinvent the wheel.
<br>**Rationale:** <br>
Django was chosen for its robust set of features that enable building secure, scalable, and maintainable web applications quickly. Its built-in admin panel, ORM (Object-Relational Mapping), and class-based views are particularly beneficial for our project's backend development needs.
<br>**Strengths:** <br>
Django includes a comprehensive standard library, an automatic admin interface, and a tight security model to help developers avoid common security mistakes such as SQL injection, cross-site request forgery, and clickjacking.
Its scalability and flexibility make it suitable for projects of any size.
<br>**Weaknesses:** <br>
Django's monolitic structure can be cumbersome for smaller projects or when a more microservices-oriented architecture is preffered. Its ORM may not be the most efficient for handling complex queries massive datasets.
<br>**Use Cases:** <br>

- **Rapid Development:** Django's "batteries-included" approach for rapid development of features without the need for extensive setup.
- **Data-Driven Applications:** With its powerful ORM, Django is well-suited for applications that require complex data processing and storage, such as car rental platform.

<ins><br>**Node.js**<br></ins>
**Description:** <br>
Node.js is an open-source, cross-platform JavaScript runtime environment that allows the execution of JavaScript code server-side, allowing for the development of backend applications using the same language familiar to many developers from frontend development. It is built on Google Chrome's V8 JavaScript Engine.
<br>**Rationale:** <br>
Node.js is known for building efficient, scalable applications because of its non-broken, event-driven architecture making it highly scalable and suitable for real-life applications.
Due to its simple integration with web technologies, this JavaScript-based framework was chosen and will be a great fit for our project. Additionally, It is also worth mentioning that all the developers in the project are well-familiarized with this language.
Qualitative Assessment:
<br>**Strengths:** <br>
Node.js possesses multiple strengths that make it a preferred choice for the development of web applications. First of all, Node.js can handle multiple operations in the background without blocking the main thread due to its asynchronous architecture. This model is a perfect match for web applications that require a lot of I/O operations, thus increasing the throughput of the system. Unlike other traditional processing models, I/O operations don't halt the execution of subsequent operations.
While using Node.js, developers can maintain unity within their frontend and backend scripting structures with of a single language, JavaScript. Such a unified environment reduces the workflow and learning curve of both front and back teams. Hence, The development process gains greater efficiency and organization.
<br>**Weakness:** <br>
Overall, Node.js is a powerful tool for web development, but it has some weaknesses that make it less suitable for certain projects. As explicitly said, Node.js operates on a single-threaded loop. This is great for I/O tasks, but not for CPU-intensive operations. The single-threaded nature can become a bottleneck when it has to deal with these operations. As the event loop is frequently busy operating I/O requests, other incoming requests get delayed, which reduces the overall performance of the system. Another weakness is the extensive nesting of callback functions, necessary for any asynchronous architecture.  
<br>**Use Cases:** <br>

- **Collaborative Tools**: Node.js provides extensive tools for collaborative applications such as document editing platforms which let multiple users collaborate and edit the same document in real-time. Node.js handles WebSockets which facilitates real-time event base communication.
- **IoT Applications**: The Node.js non-blocking I/O model is a perfect match for IoT Applications, those that handle concurrent connections from various devices at the same time. The ability to process a large amount of data aligns well with the lightweight data-intensive requirements of IoT models.

<ins><br>**ASP.NET**<br></ins>
**Description:**
ASP.NET is an open-source web framework used for building the most modern dynamic web applications and services with .Net by Microsoft. It accommodates different programming styles like Web Forms, MVC, and Web API.
ASP.NET enhances the .NET platform with components for building specific types of apps. It offers a new comprehensive framework that processes web requests in languages like C# and F#.

**Rationale:**
ASP.NET offers developers a seamless integration with other Microsoft technologies, like Visual Studio, SQL Server, and Azure. ASP.NET is known for providing a rich set of features and libraries for building web applications and also includes support for model-view-controller architecture. Caching, web APIs, authentication, and authorization are examples of more technologies that ASP.NET offers.
**Strengths:**
**Weakness:**
The main weaknesses of using ASP.NET come from its environment. While being great for Microsoft technologies, using ASP.NET with a non-Windows environment can be relatively challenging. Furthermore, ASP.NET could present a difficulty in the learning curve for those who are not familiar with .Net languages such as C#, F#, and VB.NET.

**Use cases:** -**E-commerce website**: The scalability and integration with Microsoft Technologies make ASP.NET a common choice of web application framework for CRM systems, ERP software, and supply chain management systems. -**Enterprise Applications**: ASP.NET is well suited to accommodate E-commerce websites that require features like browsing, filtering, shopping carts, processing payments, and customer accounts.

#### Frontend Framework Evaluation

- **Vue.js**: Selected for its ease of learning and integration, Vue.js enables us to develop a dynamic UI efficiently.
- **React**: Offers a vast ecosystem and high performance, ideal for complex UIs.
- **Angular**: A full-fledged framework providing a wide range of features, suitable for enterprise-level applications.

<ins><br>**React**<br></ins>
**Description:** <br>
React is a front-end framework. It is an open-source JavaScript library developed and created by Meta Platforms formerly known as Facebook. It’s a component-based framework meaning developers can create reusable self-contained code that defines a specific UI component.
<br>**Rationale:** <br>
<br>**Qualitative Assessment:** <br>
<br>**Strengths:** <br>
As previously mentioned, React has a component architecture that makes it easier to manage large and complex applications due to its encapsulated nature. React has a virtual DOM which is a lighter version of the actual DOM in the memory. Thus, React has faster and more efficient DOM updates and Browser re-renders since it updates the virtual DOM and then optimizes when updating the real DOM. React is the most in-demand web framework as such it has a large and ever-growing community and provides an abundance of resources such as tutorials, forums, and online communities.
<br>**Weakness:** <br>
React is based on a flux architecture which can prove hard to learn for developers. New concepts such as Actions, Dispatchers, Views, and Stores are hard to understand for beginners. Indeed, the Flux architecture can introduce scalability challenges due to a growing set of dependencies between the aforementioned concepts. Also, React’s flux architecture forces developers to write many repetitive codes known as boilerplate code to set up the Flux pattern.  
<br>**Use Cases:** <br>

- React Native allows developers to build mobile applications using JavaScript and React, thus enabling code sharing between the web and mobile platforms.

- **Large-Scale Web Applications**: React’s modular architecture and vast tools like Redux and React Router a great assets for building large-scale web applications with multiple UI requirements.

<ins><br>**Vue.js**<br></ins>
**Description:** <br>
Vue.js is a JavaScript framework for building interactive web interfaces. It focuses on the view layer and provides a simple API. It’s very approachable since its syntax is a blend of HTML and JavaScript. Vue.js is known for its vast ecosystems of libraries and tools making it a popular framework for both small and big projects alike.
<br>**Rationale:** <br>
Vue.js was chosen due to its simple nature. When we considered our front-end developers' technological background, we found that Vue.js ’s ease of integration and incremental approach were the right fit for our team. Indeed, we are more familiar with HTML, CSS, and JavaScript thus Vue.js similar syntax is a great asset. Also, its component-based architecture and incremental philosophy enable us to modularize the code which helps us scale harmoniously.
Qualitative Assessment:
<br>**Strengths:** <br>
As previously mentioned, Vue.js has a simple syntax and HTML-based templates, making it friendly to developers already comfortable with HTML, CSS, and JavaScript. Vue.js, through its virtual DOM, efficiently updates the DOM when a data property is changed in a Vue component. Also, Vue.js provided reactive features such as computed properties and watchers which allow faster responses to changing data. Vue.js encourages component-based architecture. Thus, the encapsulated components promote easy communication between parent-child, code reuse, modularity, and maintainability.
<br>**Weakness:** <br>
Vue.js is a relatively newer framework, thus it faces challenges in enterprise adoption compared to its older peers such as React and Angular. Indeed, due to the lack of enterprise adoption, Vue.js doesn’t have the same level of studies and documentation. Also, its ecosystem of libraries and tools may not be as vast as React or Angular. Some developers may not find a library or a set of tools specific to their unique needs. Furthermore, Vue.js official tooling named Vue CLI is very limited. Indeed, it doesn’t offer as many features as React’s Create React App or Angular’s Angular CLI. For example, Vue CLI does not offer built-in support for server-side rendering while React has Next.js and Angular has a built-in option.
<br>**Use Cases:** <br>

- **In-app Widgets**: Vue.js is lightweight and flexible enough to be embedded into existing applications. It can easily be integrated into larger applications due to its modular and incremental nature.
- **Interactive User Interfaces**: Vue.js ‘s fast response rate due to its virtual DOM and responsive features suits applications with real-time data updates like dashboards.

<ins><br>**Angular**<br></ins>
**Description:** <br>
Angular is an open-source framework used to develop web applications created by Google. It is a TypeScript based framework, which is an extended version of JavaScript. Its main use is to build single-page web applications.
<br>**Rationale:** <br>
Angular provides a wide-ranging toolkit and may be too complex for our car rental web application. Furthermore, considering the front-end developers of our team, Angular is not the best option due to its unfamiliarity.
<br>**Strengths:** <br>
Angular provides a wide variety of tools, libraries, and third-party integrations, which can facilitate and accelerate the development of the web application. It has a reduced need for manipulating the DOM manually, due to its data binding feature, which simplifies the synchronization between the data model and the UI. Additionally, Angular is still being updated regularly by its large community of developers, meaning that there is a vast amount of ressources to provide support to the user.
<br>**Weaknesses:** <br>
If not optimized properly, Angular’s features may lead to performance overhead, which could affect the loading time and the responsiveness of the website, especially for smaller applications. It is also very complex and not ideal for simple and small web applications.
<br>**Use Cases:** <br>

- **Single-page applications**: Angular provides the necessities for building dynamic and interactive UX without page reloads.
- **Real-time applications**: Due to Angular’s data binding and reactive programming features, it can be used to build applications such as chat applications, dashboards, etc.

### Integration and Interoperability

Our car rental platform leverages the robust backend capabilities of Django with the dynamic and responsive frontend framework Vue.js, creating a seamless and efficient user experience. Django serves as the powerful backend, utilizing its ORM for database abstraction and its migration system for secure database changes, while Vue.js enhances the frontend with its component-based architecture and reactive data binding. This integration is facilitated through RESTful API endpoints created with Django, which Vue.js accesses using Axios for smooth data exchange. Together, Django and Vue.js enable a modular, scalable, and maintainable architecture, ensuring our platform is both user-friendly and technically sound.

### Security Considerations

For security considerations in our car rental platform, we prioritize safeguarding user data and interactions. By integrating Auth0, we implement robust authentication and authorization processes, utilizing JWT (JSON Web Tokens) for secure communication between our Django backend and Vue.js frontend. This setup ensures that sensitive operations and data access are strictly reserved for authenticated users. Furthermore, we enforce HTTPS protocols for encrypted data transmission and adhere to CORS policies in Django to manage cross-origin requests safely. These measures, alongside diligent input validation and regular security updates, form a comprehensive security strategy that upholds the integrity and confidentiality of user information and interactions across our platform.

## Getting Started

### Prerequisites

- Python (3.x is recommended)
- Node.js and npm
- Git

### Instalation

### Setting Up the Django Backend

### Setting Up the Vue.js Frontend

### Conclusion

The Matter-soen341projectW2024 project leverages Django and Vue.js to offer a seamless car rental experience. Our choice of technologies, based on detailed evaluations, positions us to meet our objectives effectively and provide a platform that is both user-friendly and robust.

## User Stories

1. As a user, I want to log into my account so that I can book a car for rental.
2. As a user, I want to filter my car search so that I can rent the one that interests me the most.
3. As a user, I want to be able to modify my reservation so that I can have flexibility.
4. As a user, I want to be able to modify my profile so that I can update my information relevant to the application.
5. As an administrator, I want to be able to add new cars from new companies that I sign contracts with so that the user sees that they are now available.
6. As a user, I want to make a reservation on a chosen car so that I can use it for my personal use.

---
