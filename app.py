import streamlit as st
import os,sys
import IPython
import soundfile
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pickle
import joblib



def wave_plot(data,sampling_rate):
    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(30.5, 18.5)
    ax.set_facecolor("black")
    fig.set_facecolor("black")
    plt.ylabel('Amplitude')
    plt.title("WAVEFORM",fontweight="bold")
    librosa.display.waveshow(data, sampling_rate,x_axis='s')
    st.pyplot(fig,use_container_width=True)
    return data



def prediction_mlp(data,sampling_rate):
    dict_values = {0:"neutral",1:"calm",2:"happy",3:"sad",4:"angry",5:"fear",6:"disgust",7:"pleasant surprise"}
    path = "MLP_model.pkl"
    
    MLP_model = joblib.load(open(path,"rb"))
    arr=[] 
    mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T,axis=0) 
    arr.append(mfccs)
    predict = MLP_model.predict(arr)
    detected_emotion = [dict_values[val] for val in predict]
    original_title = '<p style="font-family:Courier; color:DarkSeaGreen; font-size: 18px;"><b>EMOTION DETECTED</b></p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.subheader(detected_emotion[0].upper())    
    

def main():
    st.title(" Speech Emotion Classifier App")    
    menu = ["MLP Model","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    col1, col2 = st.columns(2)
    
                    
    if choice == "MLP Model":
        with col1:
            original_title = '<p style="font-family:Courier; color:DarkSeaGreen; font-size: 20px;"><b>CHOOSE AUDIO FILE</b></p>'
            st.markdown(original_title, unsafe_allow_html=True)
            audio_file = st.file_uploader("", type=['wav', 'mp3', 'ogg'])
            if audio_file is not None:
                with col1:
                    data, sampling_rate = librosa.load(audio_file)
                    original_title = '<p style="font-family:Courier; color:DarkSeaGreen; font-size: 18px;"><b>WAVE FORM</b> </p>'
                    st.markdown(original_title, unsafe_allow_html=True)
                    data = wave_plot(data,sampling_rate)
                with col2 :
                    original_title = '<p style="font-family:Courier; color:DarkSeaGreen; font-size: 18px;"><b>PLAY AUDIO</b> </p>'
                    st.markdown(original_title, unsafe_allow_html=True)
                    st.write('\n')
                    st.write("\n")
                    st.write("\n")
                    st.audio(audio_file, format='audio/wav', start_time=0)
                    st.write("\n")
                    st.write("\n")
                    st.write("\n")
                    st.write("\n")
                    st.write("\n")
                    prediction_mlp(data,sampling_rate) 
    else:
        
        original_title = '<p style="font-family:Courier; color:Teal; font-size: 18px;"><b>Speech emotion recognition (SER) is a research field that based on speech recognition but deals with the recognizing the emotional state of the speaker. Speech emotion recognition can have applications between a natural man and machine interaction.</b></p>'
        st.markdown(original_title, unsafe_allow_html=True) 
        original_title = '<p style="font-family:Courier; color:white;font-size: 18px;"></br><b>trained MLP model to predict the output<b><p>'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<br></br>'
        st.markdown(original_title, unsafe_allow_html=True) 
        original_title = '<p style="font-family:Courier; color:Teal; font-size: 25px;"><b>CREATED BY</b></p>'
        st.markdown(original_title, unsafe_allow_html=True)  
        st.write("\n")
        original_title = '<p style="font-family:Courier; color:Teal; font-size: 20px;"><b>APOORVA KR -apoorvargowda1@gmail.com</b></p>'
        st.markdown(original_title, unsafe_allow_html=True)       


if __name__ == '__main__':
    main()
