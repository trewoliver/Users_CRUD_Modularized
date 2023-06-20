from flask import render_template, request, redirect


from flask_app import app


# from flask_app.config.mysqlconnection import connectToMySQL

# user_model represents the file
# which we pull the class from
from flask_app.models.user_model import User

#you need to create two different routes in order to process the html file
#  then running the action for the file itself
@app.route('/user_form')
def show_form():

    return render_template('user_form.html')



@app.route('/submit_user_form',methods=["POST"])
def submit_user_form():
    
    User.add_user(request.form)
    
    return redirect('/')



@app.route('/')
def Home():
    
    all_users = User.get_all()
    print(all_users)

    return render_template('index.html',all_users=all_users)



@app.route('/edit_user_form',methods=["POST"])
def update():

    User.update_user(request.form)

    return redirect('/')



@app.route('/edit/<int:user_id>')
def show_edit_form(user_id):

    one_user = User.get_one( {'user_id' :  user_id} )

    return render_template('edits_form.html',one_user=one_user)



@app.route('/delete/<int:user_id>')
def delete_user(user_id):

    User.delete_one( {'user_id' : user_id} )

    return redirect('/')



@app.route('/show_user/<int:user_id>')
def display_user(user_id):

    show_one = User.display_one( {'user_id' : user_id} )


    return render_template('show_form.html', show_one=show_one)



# @app.route('/show_form',methods=['POST'])
# def display_user_form():

#     User.show_user(request.form)

#     return redirect('/')