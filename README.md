# Matter-soen341projectW2024

## Project Description

Our project, a cutting-edge Car Rental Platform, aims to revolutionize the way users rent cars for personal use. By leveraging the latest web technologies, we offer a seamless, intuitive, and comprehensive car rental experience. Users can effortlessly browse a wide selection of vehicles, read detailed reviews from previous customers, and choose the perfect car that suits their needs and preferences. Our secure and straightforward payment process ensures a hassle-free rental experience from start to finish.

### Primary Users and Main Use Cases

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

Julia enhances user experience, bringing her extensive experience with HTML, CSS, and JavaScript to the table. Her creativity and innovative approach drive the aesthetic and functional design of our user interface.

#### Cristina - Frontend Lead

Cristina ensures that the implemented UI is coherent in every view and that it is easy for the user to interact with the platform. Her experience with the chosen frontend framework, Vue.js and her meticulous approach to implementation makes her an asset in the team

#### Jackson- Frontend Integration Developer

Jackson's previous work involves creating a Animal Adoption Agency Website and Financial Counseling Website from scratch using HTML,CSS, JavaScript and PHP. He ensures that the website not only looks great but also provides a seamless experience for our users. From designing layouts to implementing interactive features with JavaScript, he's passionate about creating engaging web experiences. His familarity with backend development such as PHP will allow him connect the frontend of the car rental website with the backend systems responsible for managing and storing data related to car inventory, availability, and bookings.

#### Antoine

#### André

#### Leiticia - Backend Developer

As a Backend Developer, I am focused on developing robust and scalable server-side applications. My work involves integrating Django with other backend technologies to create a solid foundation for our car rental platform.

## Project Approach and Technology

### Project Overview

We aim to create a user-friendly Car Rental Application that serves as an interface between customers and rental services, streamlining the rental process.

### Development Methodology

Our Agile methodology allows us to adapt to changes quickly, focusing on iterative development and customer feedback.

### Technology Stack

#### Backend Framework Evaluation

- **Django**: Chosen for its comprehensive features and rapid development capabilities, ideal for our secure and scalable web application.
- **Node.js**: Offers great performance for I/O intensive operations, suitable for real-time features.
- **ASP.NET**: Known for its robustness in enterprise scenarios, it provides strong security and performance.

#### Frontend Framework Evaluation

- **Vue.js**: Selected for its ease of learning and integration, Vue.js enables us to develop a dynamic UI efficiently.
- **React**: Offers a vast ecosystem and high performance, ideal for complex UIs.
- **Angular**: A full-fledged framework providing a wide range of features, suitable for enterprise-level applications.

Description:
React is a front-end framework. It is an open-source JavaScript library developed and create by Meta Platforms formerly known as Facebook. It’s a component-based framework meaning developers can create reusable self-contained piece of code that defines a specific UI component.
Rationale:
Qualitative Assessment:
Strengths:
As previously mentioned, React has a component-architecture which makes it easier to manage large and complex applications due to its encapsulated nature. React ahs a virtual Dom which is a lighter version of the actual DOM in the memory. Thus, React has faster and more efficient DOM updates and Browser re-renders since it updates the virtual DOM then optimize when updating the real DOM. React is the most in-demand web framework as such it has a large and ever-growing community provides an abundance of resources such as tutorials, forums and online communities. 
Weakness:
React is based on a flux architecture which can prove hard to learn for developers. New concepts such as Actions, Dispatchers, Views, and Stores are hard to understand for beginners. Indeed, the Flux architecture can introduce scalability challenges due to growing set of dependencies between the aforementioned concepts. Also, React’s flux architecture forces developers to write many repetitive codes known as boilerplate code to set up the Flux pattern.  
Uses Cases:
-React Native allows developers to build mobile applications using JavaScript and React, thus enabling code sharing between the web and mobile platform.
-Large-Scale Web Applications: React’s modular architecture and vast tools like Redux and React Router is a great asset to build large-scale web applications with multiples UI requirements.


Description:
Vue.js is a JavaScript framework for building interactive web interfaces. It focuses on the view layer and provides a simple API. It’s very approachable since its syntax is a blend of HTML and JavaScript. Vue.js is known for its vast ecosystems of libraries and tools making it a popular framework for both small and big projects alike.
Rationale:
Vue.js was chosen due to its simple nature. When we considered our front-end developers technological background, we found that Vue.js ’s ease of integration and incremental approach was the right fit for our team. Indeed, we are more familiar with HTML, CSS, and JavaScript thus Vue.js similar syntax is a great asset. Also, its component-based architecture and incremental philosophy enables us to modularize the code which help us scale harmoniously.
Qualitative Assessment:
Strengths:
As we previously mentioned, Vue.js has a simple syntax and has HTML-based templates which makes it friendly to developers already comfortable with HTML, CSS and JavaScript. Vue.js, through its virtual DOM, efficiently updates the DOM when a data property is changed in a Vue component. Also, Vue.js provided reactive features such as computed properties and watchers which allows faster responses to changing data. Vue.js encourages component-based architecture. Thus, the encapsulated components promote easy communication between parent-child, code reuse, modularity and maintainability.
Weakness:
Vue.js is a relatively newer framework, thus it faces challenges in enterprise adoptions compare to its older peers such as React and Angular. Indeed, to the lack of enterprise adoption, Vue.js doesn’t have the same level of studies and documentation. Also, its ecosystem of libraries and tools may not be as vast as React or Angular. Some developers may not find a library or the set of tools specific to their unique needs. Furthermore, Vue.js official tooling named Vue CLI is very limited. Indeed, it doesn’t offer as many features as React’s Create React App nor Angular’s Angular CLI. For example, Vue CLI does not offer built-in support for server-side rendering while React has Next.js and Angular has a built-in option.
Uses Cases:
-In-app Widgets: Vue.js is lightweight and flexible enough to be embedded into existing applications. It can easily be integrated to larger application due to its modular and incremental nature.
-Interactive User Interfaces: Vue.js ‘s fast response rate due to its virtual DOM and responsive features is well suited for application with real-time data updates like dashboards. 



### Integration and Interoperability

Our application employs RESTful APIs for seamless communication between the frontend and backend, ensuring a fluid user experience.

### Security Considerations

We prioritize application and data security through encryption, secure API endpoints, and adherence to best practices.

### Conclusion

The Matter-soen341projectW2024 project leverages Django and Vue.js to offer a seamless car rental experience. Our choice of technologies, based on detailed evaluations, positions us to meet our objectives effectively and provide a platform that is both user-friendly and robust.

## User Stories

1. As a user, I want to log into my account so that i can book a car for rental.
2. As a user, I want to filter my car search so that i can rent the one that interests me the most.
3. As a user, I want to be able to modify my reservation so that i can have flexibility.
4. As a user, I want to be able to modify my profile so that i can update my information relevant to the application.
5. As an administrator, I want to be able to add new car from new companies that i sign contracts with so that the user sees that they are now available.
6. As a user, I want to make a reservation on a chosen car so that i can use it for my personal use.
---
