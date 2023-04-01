import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('Heart_model.sav','rb'))
def heart_predicton(input_data):
   
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if(prediction[0]==0):
       return 'The Person does not have a Heart Disease'
    else:
       return 'The person has heart Disease'
       
def main():
      
      st.title('Heart Prediction Model')
      
      Age=st.text_input("Age of the Person")
      Sex=st.text_input("Sex of the Person")
      Cp=st.text_input("CP Value")
      Trestbps=st.text_input("trestbps Value")
      Chol=st.text_input("Chol Value")
      Fbs=st.text_input("Fbs value")
      Restecg=st.text_input("Restecg value")
      Thalach=st.text_input("Thalach value")
      Exang=st.text_input("Exang value")
      Oldpeak=st.text_input("OldPeak value")
      Slope=st.text_input("Slope  value")
      Ca=st.text_input("CA value")
      Thal=st.text_input("Thal value")
      
      diagnosis=''
      
      if st.button('Heart Test Result'):
          diagnosis=heart_predicton([Age,Sex,Cp,Trestbps,Chol,Fbs,Restecg,Thalach,Exang,Oldpeak,Slope,Ca,Thal])
          
          
      st.success(diagnosis)
      
if __name__=='__main__':
    main()