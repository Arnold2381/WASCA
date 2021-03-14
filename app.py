import streamlit as st


from PIL import Image
import os
import pickle as pkle
import cv2 as cv
from collections import OrderedDict


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
        r=uploaded_file.__dict__
        if('clean' in r['name']):
            tagline='Sit and just appreciate the beauty around you!'
            label=9
        else:
            tagline='You need a Marie Kondo to clear it up!'
            label=4
    
        image = Image.open(uploaded_file)
        img_show='''<img width= "800px" height="300px" src={image} text-align='center'></img>
        '''
        st.image(image, caption='Uploaded Image.', width=300 )

        st.write("")

    
     
       
        st.write("Waste Category: "+ str(label))
        
      
if __name__=="__main__":
    main()


