from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! from Edouard Atanesyan. I am adding my first code change'
#new
@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

# Favorite course page; subject and course_number are read from the URL in the template
@app.route('/favorite-course')
def favorite_course():
    return render_template('favorite-course.html')


# Contact form: GET shows the form, POST shows the thank-you message
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()

