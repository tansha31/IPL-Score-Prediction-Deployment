# Import necessary libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# load the Rigde Regression Model
filename = 'ipl-score-prediction-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()

    if request.method == 'POST':

        # venue
        venue = request.form['venue']

        if venue == 'Feroz Shah Kotla':
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0]
        elif venue == 'Himachal Pradesh Cricket Association Stadium':
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0]
        elif venue == 'M Chinnaswamy Stadium':
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0]
        elif venue == 'MA Chidambaram Stadium, Chepauk':
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0]
        elif venue == 'Punjab Cricket Association IS Bindra Stadium, Mohali':
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0]
        elif venue == 'Punjab Cricket Association Stadium, Mohali':
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0]
        elif venue == 'Rajiv Gandhi International Stadium, Uppal':
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0]
        elif venue == 'Sardar Patel Stadium, Motera':
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0]
        elif venue == 'Sawai Mansingh Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0]
        elif venue == 'Wankhede Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0]
        elif venue == 'Others':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1]
        elif venue == 'Eden Gardens':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0]

        # batting_team
        batting_team = request.form['batting-team']

        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,1]

        # bowling_team
        bowling_team = request.form['bowling-team']

        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,1]

        # Overs, Runs, Wickets, Runs_last5, Wickets_last5
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_last5 = int(request.form['runs_last_5'])
        wickets_last5 = int(request.form['wickets_last_5'])

        temp_array = temp_array + [overs,runs,wickets,runs_last5,wickets_last5]

        # Converting into numpy array
        data = np.array([temp_array])

        my_prediction = int(regressor.predict(data)[0].round())

        return render_template('result.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5)

@app.route('/home', methods=['POST'])
def homes():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
