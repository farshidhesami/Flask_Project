from flask import Flask,request,jsonify ## Add jsonify for jason format not html 

app=Flask(__name__)

#Routes;

@app.route('/')
def homepage():
    return "Welcome to the homepage"

@app.route("/add",methods=['POST'])
def addition():
    if request.method=="POST":
        result=int(request.json["num1"]) + int(request.json["num2"])  ## " json format in postman selected "
        return "The summation is {}".format(result) 
        


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
    
    