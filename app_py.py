
# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dLY7eDhVm_rwv5o_LYDVY1ds0aspuoKb
"""

# First, we import the necessary modules from Flask.

from flask import Flask, render_template_string, request

# Create an instance of the Flask class. This object will be our WSGI application.
app = Flask(__name__)

# Define the Home page route (the landing page of the website).
@app.route("/")
def home():
    # This is our HTML content for the Home page.
    html = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="description" content="Empowering rural students in Kenya through digital literacy, mentorship, and technology.">
<meta name="keywords" content="Connecting Dreams Initiative, Kenya, digital literacy, student empowerment">
<meta name="author" content="Connecting Dreams Initiative">
      <title>Connecting Dreams Initiative</title>
       <meta name="google-site-verification" content="LBIuqR4BpR4-ddCXsmny00Hrrmg9jWSqd4gL_Bpbl_A" />
      <style>
        body { font-family: "Times New Roman", serif; margin: 0; padding: 0; background: #f0f8ff; }
        header { background: linear-gradient(to bottom, #add8e6, #00008b); color: white; padding: 20px; text-align: center; }
        nav { text-align: center; margin: 20px; }
        nav a { margin: 0 15px; text-decoration: none; color: #00008b; font-size: 18px; }
        section { margin: 20px; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        footer { text-align: center; padding: 10px; background: #00008b; color: white; }
      </style>
    </head>
    <body>
      <header>
        <h1>Connecting Dreams Initiative</h1>
        <p>Every Dream Can Thrive</p>
      </header>
      <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/projects">Projects</a> |
        <a href="/contact">Contact</a>
      </nav>
      <section>
        <h2>Welcome</h2>
        <p>Our mission is to empower rural students in Kenya through comprehensive digital literacy, mentorship, and technology-driven learning. Join us as we transform education and build brighter futures together.</p>
      </section>
      <footer>
        <p>&copy; 2025 Connecting Dreams Initiative</p>
      </footer>
    </body>
    </html>
    """
    return render_template_string(html)

# Define the About page route.
@app.route("/about")
def about():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>About - Connecting Dreams Initiative</title>
      <style>
        body { font-family: "Times New Roman", serif; margin: 0; padding: 0; background: #f0f8ff; }
        header { background: linear-gradient(to bottom, #add8e6, #00008b); color: white; padding: 20px; text-align: center; }
        nav { text-align: center; margin: 20px; }
        nav a { margin: 0 15px; text-decoration: none; color: #00008b; font-size: 18px; }
        section { margin: 20px; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        footer { text-align: center; padding: 10px; background: #00008b; color: white; }
      </style>
    </head>
    <body>
      <header>
        <h1>About Connecting Dreams Initiative</h1>
      </header>
      <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/projects">Projects</a> |
        <a href="/contact">Contact</a>
      </nav>
      <section>
        <h2>Our Journey</h2>
        <p>As the founder of the Connecting Dreams Initiative, I have led efforts to revolutionize rural education in Western Kenya through research, policy analysis, and holistic student support. Our program focuses on academic, emotional, and social mentorship for high school students, building community engagement and civic responsibility. We aim to expand our reach to multiple schools and integrate technology-enhanced learning to empower students across the region.</p>
      </section>
      <footer>
        <p>&copy; 2025 Connecting Dreams Initiative</p>
      </footer>
    </body>
    </html>
    """
    return render_template_string(html)

# Define the Projects page route.
@app.route("/projects")
def projects():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Projects - Connecting Dreams Initiative</title>
      <style>
        body { font-family: "Times New Roman", serif; margin: 0; padding: 0; background: #f0f8ff; }
        header { background: linear-gradient(to bottom, #add8e6, #00008b); color: white; padding: 20px; text-align: center; }
        nav { text-align: center; margin: 20px; }
        nav a { margin: 0 15px; text-decoration: none; color: #00008b; font-size: 18px; }
        section { margin: 20px; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        footer { text-align: center; padding: 10px; background: #00008b; color: white; }
      </style>
    </head>
    <body>
      <header>
        <h1>Our Projects</h1>
      </header>
      <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/projects">Projects</a> |
        <a href="/contact">Contact</a>
      </nav>
      <section>
        <h2>Bridging the Digital Divide</h2>
        <p>This project equips three rural high schools in Kenya with 20 desktop computers, three Starlink satellite internet units, and Google Cardboard VR headsets. Our comprehensive program delivers digital literacy training for students, teachers, and parents, and fosters peer-led learning to empower 500 students in grades 9 and 10. We aim to create a scalable and sustainable model for bridging the technology gap in education.</p>
      </section>
      <footer>
        <p>&copy; 2025 Connecting Dreams Initiative</p>
      </footer>
    </body>
    </html>
    """
    return render_template_string(html)

# Define the Contact page route.
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Here you would typically process the form data.
        return "Thank you for getting in touch! We will respond shortly."
    html = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Contact - Connecting Dreams Initiative</title>
      <style>
        body { font-family: "Times New Roman", serif; margin: 0; padding: 0; background: #f0f8ff; }
        header { background: linear-gradient(to bottom, #add8e6, #00008b); color: white; padding: 20px; text-align: center; }
        nav { text-align: center; margin: 20px; }
        nav a { margin: 0 15px; text-decoration: none; color: #00008b; font-size: 18px; }
        section { margin: 20px; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        footer { text-align: center; padding: 10px; background: #00008b; color: white; }
        form { max-width: 600px; margin: auto; }
        input, textarea { width: 100%; padding: 10px; margin: 5px 0; }
      </style>
    </head>
    <body>
      <header>
        <h1>Contact Us</h1>
      </header>
      <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/projects">Projects</a> |
        <a href="/contact">Contact</a>
      </nav>
      <section>
        <h2>Get in Touch</h2>
        <p>Please fill out the form below to contact us.</p>
        <form method="post" action="/contact">
          <input type="text" name="name" placeholder="Your Name" required>
          <input type="email" name="email" placeholder="Your Email" required>
          <textarea name="message" placeholder="Your Message" rows="5" required></textarea>
          <button type="submit">Submit</button>
        </form>
      </section>
      <footer>
        <p>&copy; 2025 Connecting Dreams Initiative</p>
      </footer>
    </body>
    </html>
    """
    return render_template_string(html)

# Run the application if this script is executed directly.
if __name__ == "__main__":
    app.run(debug=True)
