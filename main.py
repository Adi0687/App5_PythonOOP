from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat

# __name__ contains a string of the current python file,
# nothing but a variable
# We are instantiating the Flask Class
app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)


class ResultsPage(MethodView):
    def post(self):
        billform = BillForm(request.form)

        amount = float(billform.amount.data)
        period = billform.period.data

        name = billform.name.data
        days_in_1 = float(billform.days_in_1.data)

        name2 = billform.name2.data
        days_in_2 = float(billform.days_in_2.data)

        the_bill = flat.Bill(amount=amount, period=period)
        flatmate = flat.Flatmate(name=name, days_in_house=days_in_1)
        flatmate2 = flat.Flatmate(name=name2, days_in_house=days_in_2)

        pays = flatmate.pays(bill=the_bill, flatmate2=flatmate2)
        pays2 = flatmate2.pays(bill=the_bill, flatmate2=flatmate)

        # return f"{flatmate.name} pays {flatmate.pays(bill=the_bill,flatmate2=flatmate2)}"
        return render_template('results.html',
                               name1=flatmate.name, amount1=pays,
                               name2=flatmate2.name, amount2=pays2)


class BillForm(Form):
    amount = StringField(label="Bill Amount: ", default=1417)
    period = StringField(label="Bill Period: ", default='November 2021')

    name = StringField("Name: ", default='Aadil')
    days_in_1 = StringField("Days in House: ", default=23)

    name2 = StringField("Name: ", default="Shadia")
    days_in_2 = StringField("Days in House: ", default=35)

    button = SubmitField("Calculate")


# Connects the app to the url
# .as_view is method of MethodView that is inherited by our own Homepage Class
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
