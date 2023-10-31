import pandas as pd
from flask import Flask ,request,render_template,jsonify
import pickle

app=Flask(__name__)

model=pickle.load(open('Artifacts\model2.pkl','rb'))
scaler=pickle.load(open('Artifacts\scaler.pkl','rb'))

@app.route("/")
def Home():
    return render_template("home.html")

@app.route('/predict',methods=['GET','POST'])
def predict():
    brand=float(request.form.get('Brand'))
    fuel_type=float(request.form.get('Fuel_Type'))
    transmission=float(request.form.get('Transmission_Type'))
    body_type=float(request.form.get('Body_Type'))
    Mileage=float(request.form.get('Mileage'))
    Displacement=float(request.form.get('Displacement'))
    cylinder=float(request.form.get('cylinder'))
    power=float(request.form.get('Power'))
    torque=float(request.form.get('Torque'))
    seating_capacity=float(request.form.get('seating_capacity'))
    Fuel_capacity=float(request.form.get('Fuel_capacity'))
    ground=float(request.form.get('Ground'))
    Power_Steering=float(request.form.get('v1',0))
    Power_Windows=float(request.form.get('v2',0))
    Anti_lock=float(request.form.get('v3',0))
    AC=float(request.form.get('v4',0))
    dairbag=float(request.form.get('v5',0))
    pairbag=float(request.form.get('v6',0))
    climate_contol=float(request.form.get('v7',0))
    fog_light=float(request.form.get('v8',0))
    alloy_wheels=float(request.form.get('v9',0))
    brand_list=[0]*19
    if brand<19:
        brand_list[int(brand)]=1
    fuel_type_list=[0,0]
    if fuel_type<2:
        fuel_type_list[int(fuel_type)]=1
    transmission_list=[0]
    if transmission<1:
        transmission_list[int(transmission)]=1
    body_list=[0]*7
    if body_type<7:
        body_list[int(body_type)]=1
    final_list=[]

    for i in brand_list:
        final_list.append(i)
    for i  in fuel_type_list:
        final_list.append(i)
    for i in transmission_list:
        final_list.append(i)
    for i in body_list:
        final_list.append(i)

    final_list.append(Mileage)
    final_list.append(Displacement)
    final_list.append(cylinder)
    final_list.append(power)
    final_list.append(torque)
    final_list.append(seating_capacity)
    final_list.append(Fuel_capacity)
    final_list.append(Power_Steering)
    final_list.append(Power_Windows)
    final_list.append(Anti_lock)
    final_list.append(AC)
    final_list.append(dairbag)
    final_list.append(pairbag)
    final_list.append(climate_contol)
    final_list.append(fog_light)
    final_list.append(alloy_wheels)
    final_list.append(ground)
    columns_list=['Brand_Audi', 'Brand_BMW', 'Brand_Fiat', 'Brand_Ford', 'Brand_Honda',
       'Brand_Hyundai', 'Brand_Jaguar', 'Brand_Land', 'Brand_Mahindra',
       'Brand_Maruti', 'Brand_Mercedes-Benz', 'Brand_Mitsubishi',
       'Brand_Nissan', 'Brand_Renault', 'Brand_Skoda', 'Brand_Tata',
       'Brand_Toyota', 'Brand_Volkswagen', 'Brand_Volvo', 'Fuel Type_Diesel',
       'Fuel Type_Petrol', 'TransmissionType_Manual', 'Body Type_Convertible',
       'Body Type_Coupe', 'Body Type_Hatchback', 'Body Type_Minivan',
       'Body Type_Pickup Truck', 'Body Type_SUV', 'Body Type_Sedan',
       'ARAI Mileage', 'Engine Displacement (cc)', 'No. of cylinder',
       'Max Power (kW)', 'Max Torque (Nm)', 'Seating Capacity',
       'Fuel Tank Capacity', 'Power Steering', 'Power Windows Front',
       'Anti Lock Braking System', 'Air Conditioner', 'Driver Airbag',
       'Passenger Airbag', 'Automatic Climate Control', 'Fog Lights - Front',
       'Alloy Wheels', 'Ground Clearance Unladen']
    
    df=pd.DataFrame([final_list],columns=columns_list)
    df=scaler.transform(df)
    prediction=model.predict(df)
    
    return render_template('home.html',predict=prediction[0][0])

if __name__=='__main__':
    app.run(debug=True)