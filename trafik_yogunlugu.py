import pandas as pd
import streamlit as st


trafik=pd.read_csv('trafik_1224.csv') #Veri Setinin Okunması ve Bilgi Alınması

trafik.info()

trafik['DATE_TIME']=pd.to_datetime(trafik['DATE_TIME']) #Tarih Zaman Verisinin Formatlanması

ort=trafik.groupby("GEOHASH").mean() #Veri Gruplama

nokta=st.sidebar.selectbox("Konum Seç",ort.index) #Kullanıcı Arayüzü için Konum Seçimi

ort.columns=["Date-Time","lat","lon","min","max","ort","sayi"] #Kolon Adlarının Düzenlenmesi

st.dataframe(ort) #Veri Görselleştirme

df=ort.loc[[nokta]] #Veri Seçimi ve Harita Üzerinde Görselleştirme
st.map(df) # Veri Seçimi ve Harita Üzerinde Görselleştirme
#streamlit run trafik_yogunlugu.py
