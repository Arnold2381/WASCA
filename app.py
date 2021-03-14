import streamlit as st

import tensorflow as tf
from PIL import Image
import os
import pickle as pkle
import cv2 as cv
from collections import OrderedDict

def predict(image):
    loaded_model = model_from_json(loaded_model_json)
# load weights into new model
    loaded_model.load_weights("/content/drive/MyDrive/IDAO/idao_dataset/model_inception.h5")
    print("Loaded model from disk")
    img=cv.imread(filepath)
    img=cv.resize(img,(250,250))
    img.shape
    img=np.array([img])
    resultant_prediction=loaded_model.predict(img)
    return(resultant_prediction)
def main():
    page_bg_img = '''
    <style>
    html {
    background-image: url('https://firebasestorage.googleapis.com/v0/b/offisca-2d74b.appspot.com/o/deskkk.svg?alt=media&token=22b07abb-dc56-4eff-beb3-a122dc53f190');
    background-size: cover;


    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
   

    
    text_by_img=''' <a>Hello</a>
    <style>
    a{
        font-weight:bold;
    }
    '''
    st.write('')
    st.write('')
    st.write('')
    st.title("Upload")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        img_show='''<img width= "800px" height="300px" src={image} text-align='center'></img>
        '''
        st.image(image, caption='Uploaded Image.', width=350 )

        st.write("")
        label=predict(image)
    
     
       
        st.write("Waste Category: "+ str(label))
        
      
if __name__=="__main__":
    main()


