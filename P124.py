from flask import Flask , jsonify ,  request

app = Flask(__name__)

contacts = [
    {
        'id' : 1,
        'name' : "Krishna",
        'contact' : 1111111111
    },
    {
        'id' : 2,
        'name' : "Rahul",
        'contact' : 2222222222
    }
]

@app.route( '/add-data', methods = ['POST'])

def addData():
    if not request.json:
        return jsonify(
            {
                "status" : "error",
                "message" : "Please Provide the data !"
            }
        )
    contact = {
        'id' : contacts[-1]['id'] + 1,
        'name' : request.json('name'),
        'contact' : request.json.get('contact' , "")
    }

    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "Contact added succssfully"
    })

@app.route("/get-data")
def getData():
    return jsonify({
        "data": contacts
    })

if __name__ == "__main__":
    app.run()