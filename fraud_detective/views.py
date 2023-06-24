import pickle
import numpy as np
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from . import db
from .models import Text

views = Blueprint('views', __name__)
#deserialising the saved model
model = pickle.load(open('fraud_detective/model.pkl', 'rb'))


#landing page route
@views.route('/landing')
@views.route('/')
def landing():
    return render_template("landing.html")

#home page route
@views.route('/home')
@login_required
def home():
    #logo_image = os.path.join(app.config['UPLOAD_FOLDER'], 'spy.jpg')
    return render_template("index.html")

#prediction route to return predictioi back to home
@views.route('/home', methods=['GET', 'POST'])
def preds():
    if request.method == 'POST':
        pred_text = request.form.get("pred_txt")
        source = request.form.get("txtdb")
        #conering our inputed text to list then string for the model to predict well
        prediction_model = model.predict(list(str(pred_text)))

        #checking if the prediction is 0
        if np.all(prediction_model== 0):
            prediction_key = "not-scam"
            final_pred = 'The message: {} is {}'.format(pred_text, prediction_key)
            return render_template("index.html", prediction=final_pred)
    
        elif np.all(prediction_model== 1):
            prediction_model = "scam"
            final_pred = 'The message: {} is {}'.format(pred_text, prediction_model)
            return render_template("index.html", prediction=final_pred)
        #save the new model to the text table database
        new_message = Text(message=pred_text, message_source=source)
        db.session.add(new_message)
        db.session.commit()
    flash("message must be inputed", category='error')

@views.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)