print('APP FILE LOADED')
print('THIS IS THE CORRECT APP FILE')
from click import group
from flask import (
    Flask,
    render_template,
    request,
    redirect
)
from flask_login import logout_user
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    current_user
)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'login'

class Fixture(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    home_team = db.Column(
        db.String(100)
    )

    away_team = db.Column(
        db.String(100)
    )

    home_flag = db.Column(
        db.String(10)
    )

    away_flag = db.Column(
        db.String(10)
    )

    match_date = db.Column(
        db.String(50)
    )

    kickoff = db.Column(
    db.DateTime
    )   
    home_score = db.Column(
    db.Integer,
    nullable=True
)
    stage = db.Column(
    db.String(50)
)
    away_score = db.Column(
    db.Integer,
    nullable=True
)
    group_name = db.Column(
    db.String(10)
)


class User(UserMixin, db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    first_name = db.Column(
        db.String(100)
    )

    last_name = db.Column(
        db.String(100)
    )

    email = db.Column(
        db.String(100),
        unique=True
    )

    password = db.Column(
        db.String(200)
    )
    
    is_admin = db.Column(
    db.Boolean,
    default=False
)

class Prediction(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )

    fixture_id = db.Column(
        db.Integer,
        db.ForeignKey('fixture.id')
    )

    prediction = db.Column(
        db.String(20)
    )
    
    points = db.Column(
    db.Integer,
    default=0
)

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(
        int(user_id)
    )

class KnockoutPrediction(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )

    fixture_id = db.Column(
        db.Integer,
        db.ForeignKey('fixture.id')
    )

    home_score = db.Column(
        db.Integer,
        default=0
    )

    away_score = db.Column(
        db.Integer,
        default=0
    )
    
    points = db.Column(
    db.Integer,
    default=0
)
@app.route('/debug-fixtures')
def debug_fixtures():

    fixtures = Fixture.query.all()

    output = ''

    for fixture in fixtures:

        output += f'''

        {fixture.home_team}
        vs
        {fixture.away_team}

        |

        stage:
        {fixture.stage}

        |

        group:
        {fixture.group_name}

        |

        result:
        {fixture.home_score}-
        {fixture.away_score}

        <br><br>
        '''

    return output
@app.route('/')
def home():

    player_count = User.query.count()

    prize_money = player_count * 10

    return render_template(
        'menu.html',
        player_count=player_count,
        prize_money=prize_money
    )


@app.route('/predict-groups')
@login_required
def predict_groups():

    fixtures = Fixture.query.filter_by(
    stage='GROUP'
).all()

    predictions = Prediction.query.filter_by(
        user_id=current_user.id
    ).all()

    prediction_map = {}

    for prediction in predictions:

        prediction_map[
            prediction.fixture_id
        ] = prediction.prediction

    current_time = datetime.now()

    return render_template(

        'predict_groups.html',

        fixtures=fixtures,

        prediction_map=prediction_map,

        current_time=current_time
    )

@app.route('/predict-knockouts')
@login_required
def predict_knockouts():

    fixtures = Fixture.query.filter(
        Fixture.stage != 'GROUP'
    ).all()

    if len(fixtures) == 0:

        return render_template(
            'predict_knockouts.html',
            no_fixtures=True
        )

    predictions = KnockoutPrediction.query.filter_by(
        user_id=current_user.id
    ).all()

    prediction_map = {}

    for prediction in predictions:

        prediction_map[
            prediction.fixture_id
        ] = prediction

    current_time = datetime.now()

    return render_template(

        'predict_knockouts.html',

        fixtures=fixtures,

        prediction_map=prediction_map,

        current_time=current_time,

        no_fixtures=False
    )


@app.route('/leaderboard')
def leaderboard():

    users = User.query.all()

    leaderboard_data = []

    for user in users:

        group_points = 0

        knockout_points = 0

        group_predictions = Prediction.query.filter_by(
            user_id=user.id
        ).all()

        for prediction in group_predictions:

            fixture = Fixture.query.get(
                prediction.fixture_id
            )

            if (
                fixture.home_score is not None
                and
                fixture.away_score is not None
            ):

                actual_result = None

                if fixture.home_score > fixture.away_score:

                    actual_result = 'HOME'

                elif fixture.home_score < fixture.away_score:

                    actual_result = 'AWAY'

                else:

                    actual_result = 'DRAW'

                if prediction.prediction == actual_result:

                    group_points += 1

        knockout_predictions = (
            KnockoutPrediction.query.filter_by(
                user_id=user.id
            ).all()
        )

        for prediction in knockout_predictions:

            fixture = Fixture.query.get(
                prediction.fixture_id
            )

            if (
                fixture.home_score is not None
                and
                fixture.away_score is not None
            ):

                if (
                    prediction.home_score ==
                    fixture.home_score
                    and
                    prediction.away_score ==
                    fixture.away_score
                ):

                    knockout_points += 3

                else:

                    predicted_result = None

                    actual_result = None

                    if (
                        prediction.home_score >
                        prediction.away_score
                    ):

                        predicted_result = 'HOME'

                    elif (
                        prediction.home_score <
                        prediction.away_score
                    ):

                        predicted_result = 'AWAY'

                    else:

                        predicted_result = 'DRAW'

                    if (
                        fixture.home_score >
                        fixture.away_score
                    ):

                        actual_result = 'HOME'

                    elif (
                        fixture.home_score <
                        fixture.away_score
                    ):

                        actual_result = 'AWAY'

                    else:

                        actual_result = 'DRAW'

                    if predicted_result == actual_result:

                        knockout_points += 1

        total_points = (
            group_points +
            knockout_points
        )

        leaderboard_data.append({

            'name':
                user.first_name +
                ' ' +
                user.last_name,

            'group_points':
                group_points,

            'knockout_points':
                knockout_points,

            'total_points':
                total_points
        })

    leaderboard_data = sorted(

        leaderboard_data,

        key=lambda x:
            x['total_points'],

        reverse=True
    )

    return render_template(

        'leaderboard.html',

        leaderboard_data=
            leaderboard_data
    )

@app.route('/standings')
def standings():

    groups = [
    'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L'
]

    standings_data = {}

    for group in groups:

        fixtures = Fixture.query.filter_by(
            group_name=group
        ).all()

        table = {}

        for fixture in fixtures:

            teams = [
                fixture.home_team,
                fixture.away_team
            ]

            for team in teams:

                if team not in table:

                    table[team] = {

                        'team': team,

                        'played': 0,

                        'wins': 0,

                        'draws': 0,

                        'losses': 0,

                        'gf': 0,

                        'ga': 0,

                        'gd': 0,

                        'points': 0
                    }

            if (
                fixture.home_score is not None
                and
                fixture.away_score is not None
            ):

                home = table[
                    fixture.home_team
                ]

                away = table[
                    fixture.away_team
                ]

                home['played'] += 1
                away['played'] += 1

                home['gf'] += fixture.home_score
                home['ga'] += fixture.away_score

                away['gf'] += fixture.away_score
                away['ga'] += fixture.home_score

                home['gd'] = (
                    home['gf'] -
                    home['ga']
                )

                away['gd'] = (
                    away['gf'] -
                    away['ga']
                )

                if fixture.home_score > fixture.away_score:

                    home['wins'] += 1
                    home['points'] += 3

                    away['losses'] += 1

                elif fixture.home_score < fixture.away_score:

                    away['wins'] += 1
                    away['points'] += 3

                    home['losses'] += 1

                else:

                    home['draws'] += 1
                    away['draws'] += 1

                    home['points'] += 1
                    away['points'] += 1

        sorted_table = sorted(

            table.values(),

            key=lambda x: (
                x['points'],
                x['gd'],
                x['gf']
            ),

            reverse=True
        )

        standings_data[group] = sorted_table

    return render_template(

        'standings.html',

        standings_data=standings_data
    )

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        first_name = request.form.get(
            'first_name'
        )

        last_name = request.form.get(
            'last_name'
        )

        email = request.form.get(
            'email'
        )

        password = request.form.get(
            'password'
        )

        new_user = User(

    first_name=first_name,

    last_name=last_name,

    email=email,

    password=password,

    is_admin=False
)

        db.session.add(new_user)

        db.session.commit()

        return redirect('/')

    return render_template(
        'register.html'
    )
    
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get(
            'email'
        )

        password = request.form.get(
            'password'
        )

        user = User.query.filter_by(
            email=email
        ).first()

        if user and user.password == password:

            login_user(user)

            return redirect('/')

    return render_template(
        'login.html'
    )
    
@login_manager.user_loader
def load_user(user_id):

    return User.query.get(
        int(user_id)
    )
    

@app.route('/admin-results')
def admin_results():

    fixtures = Fixture.query.all()

    return render_template(
        'admin_results.html',
        fixtures=fixtures
    )


@app.route('/update-result', methods=['POST'])
def update_result():

    print('UPDATE RESULT ROUTE HIT')

    print(request.form)

    fixture_id = request.form.get(
        'fixture_id'
    )

    home_score = request.form.get(
        'home_score'
    )

    away_score = request.form.get(
        'away_score'
    )

    print(fixture_id)
    print(home_score)
    print(away_score)

    fixture = Fixture.query.get(
        fixture_id
    )

    print(fixture)

    fixture.home_score = int(
        home_score
    )

    fixture.away_score = int(
        away_score
    )

    db.session.commit()

    print('DATABASE COMMITTED')

    return redirect(
        '/admin-results'
    )
    
@app.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect('/login')

print('REACHED KNOCKOUT ROUTE')

@app.route('/save-knockout-prediction', methods=['POST'])
@login_required
def save_knockout_prediction():

    data = request.get_json()

    fixture_id = data.get(
        'fixture_id'
    )

    home_score = int(
        data.get('home_score')
    )

    away_score = int(
        data.get('away_score')
    )

    fixture = Fixture.query.get(
        fixture_id
    )

    if datetime.now() >= fixture.kickoff:

        return {
            'success': False
        }

    prediction = KnockoutPrediction.query.filter_by(

        user_id=current_user.id,

        fixture_id=fixture_id

    ).first()

    if prediction:

        prediction.home_score = home_score

        prediction.away_score = away_score

    else:

        prediction = KnockoutPrediction(

            user_id=current_user.id,

            fixture_id=fixture_id,

            home_score=home_score,

            away_score=away_score
        )

        db.session.add(
            prediction
        )

    db.session.commit()

    return {
        'success': True
    }

@app.route('/save-prediction', methods=['POST'])
@login_required
def save_prediction():
    print('SAVE ROUTE HIT')

    data = request.get_json()

    print(data)

    fixture_id = data.get(
        'fixture_id'
    )

    prediction_value = data.get(
        'prediction'
    )

    print(fixture_id)
    print(prediction_value)
    data = request.get_json()

    fixture_id = data.get(
        'fixture_id'
    )

    prediction_value = data.get(
        'prediction'
    )

    fixture = Fixture.query.get(
        fixture_id
    )

    if datetime.now() >= fixture.kickoff:

        return {
            'success': False
        }

    existing_prediction = Prediction.query.filter_by(

        user_id=current_user.id,

        fixture_id=fixture_id

    ).first()

    if existing_prediction:

        existing_prediction.prediction = (
            prediction_value
        )

    else:

        new_prediction = Prediction(

            user_id=current_user.id,

            fixture_id=fixture_id,

            prediction=prediction_value
        )

        db.session.add(
            new_prediction
        )

    db.session.commit()

    return {
        'success': True
    }

print('SAVE PREDICTION ROUTE REGISTERED')

@app.route('/admin/knockouts', methods=['GET', 'POST'])
def admin_knockouts():

    fixtures = Fixture.query.filter(
        Fixture.stage != 'GROUP'
    ).order_by(Fixture.kickoff).all()

    if request.method == 'POST':

        fixture_id = request.form.get('fixture_id')

        fixture = Fixture.query.get(fixture_id)

        home_selection = request.form.get('home_selection').split('|')
        away_selection = request.form.get('away_selection').split('|')

        fixture.home_team = home_selection[0]
        fixture.home_flag = home_selection[1]

        fixture.away_team = away_selection[0]
        fixture.away_flag = away_selection[1]

        db.session.commit()

        return redirect('/admin/knockouts')
    flags = [
    ('', '-'),
    ('🇩🇿', 'Algeria'),
    ('🇦🇷', 'Argentina'),
    ('🇦🇺', 'Australia'),
    ('🇦🇹', 'Austria'),
    ('🇧🇪', 'Belgium'),
    ('🇧🇦', 'Bosnia and Herzegovina'),
    ('🇧🇷', 'Brazil'),
    ('🇨🇦', 'Canada'),
    ('🇨🇻', 'Cabo Verde'),
    ('🇨🇴', 'Colombia'),
    ('🇭🇷', 'Croatia'),
    ('🇨🇼', 'Curaçao'),
    ('🇨🇿', 'Czechia'),
    ('🇨🇩', 'DR Congo'),    
    ('🇪🇨', 'Ecuador'),
    ('🇪🇬', 'Egypt'),
    ('🏴󠁧󠁢󠁥󠁮󠁧󠁿', 'England'),
    ('🇫🇷', 'France'),
    ('🇩🇪', 'Germany'),
    ('🇬🇭', 'Ghana'),
    ('🇭🇹', 'Haiti'),
    ('🇮🇷', 'Iran'),
    ('🇮🇶', 'Iraq'),
    ('🇨🇮', "Ivory Coast"),
    ('🇯🇵', 'Japan'),
    ('🇯🇴', 'Jordan'),
    ('🇰🇷', 'Korea Republic'),
    ('🇲🇽', 'Mexico'),
    ('🇲🇦', 'Morocco'),
    ('🇳🇱', 'Netherlands'),
    ('🇳🇿', 'New Zealand'),
    ('🇳🇴', 'Norway'),
    ('🇵🇦', 'Panama'),
    ('🇵🇾', 'Paraguay'),
    ('🇵🇹', 'Portugal'),
    ('🇶🇦', 'Qatar'),
    ('🏴󠁧󠁢󠁳󠁣󠁴󠁿', 'Scotland'),
    ('🇸🇳', 'Senegal'),
    ('🇸🇦', 'Saudi Arabia'),
    ('🇿🇦', 'South Africa'),
    ('🇪🇸', 'Spain'),
    ('🇸🇪', 'Sweden'),
    ('🇨🇭', 'Switzerland'),
    ('🇹🇳', 'Tunisia'),
    ('🇹🇷', 'Turkey'),
    ('🇺🇾', 'Uruguay'),
    ('🇺🇸', 'USA'),
    ('🇺🇿', 'Uzbekistan')
]
    return render_template(
        'admin_knockouts.html',
        fixtures=fixtures,
        flags=flags
    )

print(app.url_map)

if __name__ == '__main__':

    app.run(
    host='0.0.0.0',
    port=8000,
    debug=True,
    use_reloader=False
)