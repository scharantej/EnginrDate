## Flask Application Design for a Dating App with Engineering Calculator Integration

### HTML Files

- **index.html:**
    - Landing page with user registration and login forms.
    - Displays a list of potential matches based on compatibility and technical skills.

- **profile.html:**
    - Personal profile page displaying user's information, including technical skills and project interests.
    - Allows users to update their profile and view compatibility with other users.

- **calculator.html:**
    - Engineering calculator interface integrated into the dating app.
    - Enables users to collaborate on technical projects and engage in intellectual discussions.

- **chat.html:**
    - Chat interface for users to communicate with potential matches.
    - Provides a platform for exchanging ideas, sharing knowledge, and fostering connections.

### Routes

- **@app.route('/register', methods=['GET', 'POST'])**:
    - Handles user registration.
    - Redirects to the login page upon successful registration.

- **@app.route('/login', methods=['GET', 'POST'])**:
    - Handles user login.
    - Redirects to the home page upon successful login.

- **@app.route('/home')**:
    - Displays the home page with potential matches.
    - Provides links to the profile, calculator, and chat pages.

- **@app.route('/profile')**:
    - Displays the user's profile.
    - Allows users to update their information and view compatibility with others.

- **@app.route('/calculator')**:
    - Renders the engineering calculator interface.
    - Handles calculations and displays results.

- **@app.route('/chat')**:
    - Renders the chat interface.
    - Handles message sending and receiving between users.