# Description: Allow users to visit /donations/Alice/ to see a list of just Alice's
# donations, to see a list of just Bob's donations at /donations/Bob/, etc.
# Comment: Execute in Python3.6
# Last Modified on 04/08/2018 by David Kan


import os
import base64
from flask import Flask, render_template, request, redirect, url_for, session
from model import Donation, Donor


app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/donations/<person>/')
def individual(person):
    """
    Gets a list of just Alice's, Bob's, or Charlie's donations and orders the value by descending
    :Donor.name: <peewee.CharField object at 0x0000020E3A26E278>
    :param person: Alice, Bob, Charlie
    :donations: <peewee.ModelSelect object at 0x0000020E3A53B128>
    :return:'<html>\n<head>\n<title>Mailroom</title>\n</head>\n<body>\n\t<h1>Donations</h1>\n
    \t<h2>Donations</h2>\n\t\n<ul>\n    \n <li><b>Bob</b>: 1941</li>\n    \n
    """
    donations = Donation.select().join(Donor).where(Donor.name == person).order_by(Donation.value.desc())
    return render_template('donations.jinja2', donations=donations)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
