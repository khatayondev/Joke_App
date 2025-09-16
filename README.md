# PyJoke WebApp

Welcome to **PyJoke WebApp** – a simple, fun web application that delivers random programming jokes using the [pyjokes](https://pypi.org/project/pyjokes/) Python library. This project is built with Flask for the backend and vanilla HTML, CSS, and JavaScript for the frontend.

---

## Features

- **Random Programming Jokes:** Get a new joke every time you click the button.
- **Two UI Versions:**
  - `index.html`: Minimal, basic styling for quick prototyping or learning.
  - `index1.html`: Modern landing page with a hero section, responsive design, and enhanced user experience.

---

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/pyjoke-webapp.git
   cd pyjoke-webapp
   ```

2. **Install dependencies:**
   ```bash
   pip install flask pyjokes
   ```

### Running the App

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Open your browser:**
   - Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Usage

- By default, the app serves `index1.html`, the enhanced landing page.
- If you want a minimal version, change the Flask route to serve `index.html` instead:
  ```python
  return render_template('index.html')
  ```
- Both versions allow you to fetch jokes by clicking the "Get a Joke" button.

---

## File Structure

```
├── app.py                # Flask backend
├── templates/
│   ├── index.html        # Minimal UI version
│   └── index1.html       # Enhanced landing page version
├── README.md             # Project documentation
```

---

## Screenshots

### Minimal Version (`index.html`)
A simple, clean interface for quick access to jokes.

### Enhanced Version (`index1.html`)
A modern landing page with a hero section, stylish joke display, and responsive layout.

---

## Customization

- **Styling:** Modify `index1.html` for advanced UI or add your own CSS.
- **Backend:** Extend `app.py` to support more joke categories or APIs.

---

## Credits

- [pyjokes](https://pypi.org/project/pyjokes/) for joke generation.
- Inspired by programming humor and developer communities.

---

## License

This project is licensed under the MIT License.

---

Enjoy your daily dose of programming humor! 😄
