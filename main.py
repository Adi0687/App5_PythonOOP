from flask.views import MethodView
from wtforms import Form
from flask import Flask, render_template

# __name__ contains a string of the current python file,
# nothing but a variable
# We are instantiating the Flask Class
app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        return "I am the Bill form page"
        # return render_template('bill_form_page.html')


class ResultsPage(MethodView):
    pass


class BillForm(Form):
    pass


# Connects the app to the url
# .as_view is method of MethodView that is inherited by our own Homepage Class
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))

app.run(debug=True)
