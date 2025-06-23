import json
from models import *
from flask import request
from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required,get_jwt_identity





#http://localhost:5000/employee/api  --> POST -- {"EMPLOYEE_ID" : 101,"EMPLOYEE_NAME": "abc","EMPLOYEE_SALARY" : 283.34,"EMPLOYEE_ROLE" : "sse"}

USERNAME = "Tina"
PASSWORD = "Tina123"

@app.route('/employee/api/get_token',methods = ['POST'])
def generate_api_token():
    jsonbody = request.get_json()
    username = jsonbody.get('username')
    password = jsonbody.get('password')
    if username and password and username == USERNAME and password == PASSWORD:
        access_token = create_access_token((username,password))
        refresh_token = create_refresh_token((username, password))
        return json.dumps({"ACCESS_TOKEN" : access_token, "REFRESH_TOKEN" : refresh_token})
    else:
        return json.dumps({"ERROR" : "Invalid Creadentails"})


@app.route("/employee/api",methods = ['POST'])
@jwt_required()
def create_an_employee_record():
    jsonBody = request.get_json()
    if jsonBody:
        emp = Employee(id=jsonBody.get('EMPLOYEE_ID'),
                 name=jsonBody.get('EMPLOYEE_NAME'),
                 salary=jsonBody.get('EMPLOYEE_SALARY'),
                 role=jsonBody.get('EMPLOYEE_ROLE'),)
        db.session.add(emp)
        db.session.commit()
        return json.dumps({"SUCCESS" : "Emp Created Successfully..!"})
    else:
        return json.dumps({"ERROR": "Problem in Employee Add..!"})
                
@app.route("/employee/api",methods = ['GET'])
@jwt_required()
def list_of_employees():
    emplist = Employee.query.all()
    empJsonList = []

    for emp in emplist:
        employee_json = {"EMP ID " : emp.id,"EMPLOYEE NAME " : emp.name,
                         "EMPLOYEE SALARY" : emp.salary, "EMPLOYEE ROLE" : emp.role}
        empJsonList.append(employee_json)
    if empJsonList:
        return json.dumps(empJsonList)
    else:
        return json.dumps({"ERROR" : "NO Employees"})

@app.route('/employee/api/get_a_token',methods = ['GET'])
@jwt_required(refresh=True)
def get_access_token_using_refresht():
    identity = get_jwt_identity()
    access_token = create_access_token(identity)
    return json.dumps({"ACCESS_TOKEN": access_token})



if __name__ == '__main__':
    app.run(debug=True)

    """  {
    "EMPLOYEE_ID" : 4,
    "EMPLOYEE_NAME" : "John",
    "EMPLOYEE_SALARY" : 20000000,
    "EMPLOYEE_ROLE" : "Manager"

} """