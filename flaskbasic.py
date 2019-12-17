from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", message="Hello Flask!");



@app.route("/users")
def user_page():
	filter = request.args.get('filter')


	user_list = [{"id": 1, "name": "Aadesh Khatri", "active": True, "imageUrl": ""},
				 {"id": 2, "name": "Riddhi Patel", "active": False, "imageUrl": ""},
                    {"id": 3, "name": "Chuck Pratt", "active": False, "imageUrl": ""}]

	if filter == 'active':
		user_list = [user_list[0]]
	elif filter == 'inactive':
		user_list = [user_list[1]]

	if filter:
		if user_list:
			return render_template("users.html", user_list=user_list, filter=filter)
		else:
			return render_template("no-user.html", filter=filter)
	else:
		return render_template("users.html", filter=filter)




@app.route("/no-user")
def no_user():
	return render_template("no-user.html")





if __name__ == '__main__':
	app.run(debug=True)