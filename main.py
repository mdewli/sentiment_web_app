import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import time
from PIL import Image
import matplotlib.pyplot as plt



def main():
    
    
    ger_gov_img = Image.open('data/ger_cities.PNG')
    ger_gov = Image.open('data/ger_gov.PNG')
    
    ger_econ_img = Image.open('data/econ.jpg')   
    ger_econ = Image.open('data/ger_econ.PNG')
    
    ger_head_img = Image.open('data/angela.jpg')
    ger_head = Image.open('data/ger_head.PNG')
    
    vaccn_img = Image.open('data/vaccn.jpg')
    ger_vaccn = Image.open('data/ger_vaccn.PNG')
    
    
    
    
      
    ind_gov_img = Image.open('data/ind_map.PNG')
    ind_gov = Image.open('data/ind_govt.PNG')
    
    ind_econ_img = Image.open('data/ind-econ_img.jpg')   
    ind_econ = Image.open('data/economy.PNG')
    
    ind_head_img = Image.open('data/modi.jpg')
    ind_head = Image.open('data/ind_head.PNG')
    
    vaccn_Img = Image.open('data/vaccn.jpg')
    ind_vaccn = Image.open('data/ind_vacc.PNG')
    
    
    
      
    tur_gov_img = Image.open('data/turky_map.PNG')
    tur_gov = Image.open('data/turk_gov.PNG')
    
    tur_econ_img = Image.open('data/tur_econ_img.jpg')   
    tur_econ = Image.open('data/turk_econ.PNG')
    
    tur_head_img = Image.open('data/erdogan_img.png')
    tur_head = Image.open('data/turk_erdo.PNG')
    
    vaccn_img = Image.open('data/vaccn.jpg')
    tur_vaccn = Image.open('data/turk_vacc.PNG')
    
    
    
    
    
    
    
    
    
    df=load_data()
    
    ger_cities=['Berlin','Munich','Hamburg','Cologne']
    ind_cities=['Delhi','Mumbai','Chennai','Bangalore']
    tur_cities=['Istanbul','Ankara','Izmir','Antalya']
    
    countries=df.groupby('Country').count().reset_index()['Country'].tolist()
    cities= df.groupby('Location').count().reset_index()['Location'].tolist()
    categories=['Government','Head of State','Economy','Vaccine']
    slot1 = st.empty()
    slot1 = st.empty()
    slot2 = st.empty()
    slot3 = st.empty()
    slot4 = st.empty()
    slot5 = st.empty()
    slot6 = st.empty()
    
    slota = st.sidebar.empty()
    slott= st.sidebar.empty()
    slotb = st.sidebar.empty()
    slotc = st.sidebar.empty()
    slotd = st.sidebar.empty()
    slote = st.sidebar.empty()
    slotf = st.sidebar.empty()
    slotg = st.sidebar.empty()
        
    slota.title('Select the parameters to analyze Sentiment')
    slott.write("")
    check1 = slotb.checkbox("Show Analysis by Country", False, key=1)
    
    
    col1, col2 = st.beta_columns(2)
    
    if check1==False:
        st.title("Twitter Sentiment Analysis")
        st.subheader("Compare and Analyse Public Sentiment on various Topics in 4 major Cities of Turkey, India and Germany!")
        st.subheader("Select a topic or a country from the dropdown list to the left of the screen!")
        st.text("")
        st.write("The goal of the project was to analyse the public sentiment towards the head's of the states, the economy, the vaccines and the handling of the corona crisis by the ruling parties. In order to analyse the sentiment towards government's handling of the pandemic we considered tweets which had words 'Government'/Ruling parties name/Head of state's name and corona in the same tweet. Similarly, various other 'keywords' were used to extract tweets on other issues ")
        image = Image.open('data/homepage.PNG')
        st.write("This analysis is based on over 30 thousand tweets collected in the months of november and december using twitter's official API 'Tweepy'. We have considered tweets from from 4 major cities of India, Turkey and Germany for this analysis.The tweets extracted, contained text data in 3 languages: English, German and Turkish. The sentiment scores were calculated using pretrained BERT based models which are available in English, Turkish and German language. The sentiment is divided in three categories: Positive, Negative and Neutral. The score may range from 0 to 1 and is a measure of accuracy of prediction.The visualizations were produced using Tableau. The web app has been created using the open source Python library called Sreamlit.")
        st.image(image,use_column_width=True)
        
    if check1==True:
        select1=slotc.selectbox('Select a Country',countries)
        
        check2=slotd.checkbox("Want to Analyse by Category?")
        
        
        
        if check2==True:
            select2=slote.selectbox("Select a Category: ",categories)
            
            
            #gernmany all cities
        if select1==countries[0]:
            slot1.subheader("Public perception on various issues across 4 major German cities:")
            slot2.subheader("")
            ger_map = Image.open('data/ger_cities.PNG')
            slot3.image(ger_map,use_column_width=True)
            ger_gov = Image.open('data/ger_all.PNG')
            slot4.subheader('Sentiment across 4 major cities of Germany:')
            slot5.subheader("")
            slot6.image(ger_gov,use_column_width=True)
            
            #India general for all cities
        if select1==countries[1]:
            slot1.subheader("Public perception on various issues across 4 major Indian cities:")
            slot2.subheader("")
            ind_map = Image.open('data/ind_map.PNG')
            slot3.image(ind_map,use_column_width=True)
            ind_gov = Image.open('data/india_all.PNG')
            slot4.subheader('Sentiment across 4 major cities of India:')
            slot5.subheader("")
            slot6.image(ind_gov,use_column_width=True)
            
            #Turkey general for all cities
        if select1==countries[2]:
            slot1.subheader("Public perception on various issues across 4 major Turkish cities:")
            slot2.subheader("")
            tur_map = Image.open('data/turky_map.PNG')
            slot3.image(tur_map,use_column_width=True)
            tur_gov = Image.open('data/turk_all.PNG')
            slot4.subheader('Sentiment across 4 major cities of Turkey:')
            slot5.subheader("")
            slot6.image(tur_gov,use_column_width=True)
            
            
            
            
        if check1==True and check2==True:
            
            #german_govt all cities
            if select1==countries[0] and select2==categories[0]:
                slot1.subheader("Public perception of Government across 4 major German cities:")
                slot2.subheader("") 
                slot3.image(ger_gov_img,use_column_width=True)
                slot4.subheader('Sentiment across 4 major cities of Germany:')
                slot5.subheader("")
                slot6.image(ger_gov,use_column_width=True)
                
                #german head of state all cities
            if select1==countries[0] and select2==categories[1]:
                slot1.subheader("Public perception of Angela Merkel across 4 major German cities:")
                slot2.subheader("")
               
                slot3.image(ger_head_img,use_column_width=True)
        
                slot4.subheader('Sentiment across 4 major cities of Germany:')
                slot5.subheader("")
                slot6.image(ger_head,use_column_width=True)
                
                #german economy all cities
            if select1==countries[0] and select2==categories[2]:
                slot1.subheader("Public perception of German Economy across 4 major German cities:")
                slot2.subheader("")
              
                slot3.image(ger_econ_img,use_column_width=True)
                
                slot4.subheader('Sentiment across 4 major cities of Germany:')
                slot5.subheader("")
                slot6.image(ger_econ,use_column_width=True)
                
                #german vaccine all cities
            if select1==countries[0] and select2==categories[3]:
                slot1.subheader("Public sentiment n on Vaccination across 4 major German cities:")
                slot2.subheader("")
             
                slot3.image(vaccn_img,use_column_width=True)
           
                slot4.subheader('Sentiment across 4 major cities of Germany:')
                slot5.subheader("")
                slot6.image(ger_vaccn,use_column_width=True)
                
                
                
                
                #Indian givt all cities
            if select1==countries[1] and select2==categories[0]:
                slot1.subheader("Public perception of governance across 4 major Indian cities:")
                slot2.subheader("")
                slot3.image(ind_gov_img,use_column_width=True)
                slot4.subheader('Sentiment across 4 major cities of India:')
                slot5.subheader("")
                slot6.image(ind_gov,use_column_width=True)
                
                #Indian head of state all cities
            if select1==countries[1] and select2==categories[1]:
                slot1.subheader("Public perception of Indian Prime Minister across 4 major Indian cities:")
                slot2.subheader("")
             
                slot3.image(ind_head_img,use_column_width=True)
              
                slot4.subheader('Sentiment across 4 major cities of India:')
                slot5.subheader("")
                slot6.image(ind_head,use_column_width=True)
                
                #Indian economy all cities
            if select1==countries[1] and select2==categories[2]:
                slot1.subheader("Public perception of Indian economy across 4 major Indian cities:")
                slot2.subheader("")
                
                slot3.image(ind_econ_img,use_column_width=True)
              
                slot4.subheader('Sentiment across 4 major cities of India:')
                slot5.subheader("")
                slot6.image(ind_econ,use_column_width=True)
                
                #Indian vaccine all cities
            if select1==countries[1] and select2==categories[3]:
                slot1.subheader("Public perception on vaccination across 4 major Indian cities:")
                slot2.subheader("")

                slot3.image(vaccn_img,use_column_width=True)
               
                slot4.subheader('Sentiment across 4 major cities of India:')
                slot5.subheader("")
                slot6.image(ind_vaccn,use_column_width=True)
                
                
                
                
                
                
                #turish govt all categ all cities
            if select1==countries[2] and select2==categories[0]:
                slot1.subheader("Public perception on goveranance across 4 major Turkish cities:")
                slot2.subheader("")
               
                slot3.image(tur_giv_img,use_column_width=True)
                
                slot4.subheader('Sentiment across 4 major cities of Turkey:')
                slot5.subheader("")
                slot6.image(tur_gov,use_column_width=True)
                
                #Turkish head of state all cities
            if select1==countries[2] and select2==categories[1]:
                slot1.subheader("Public perception of Turkish President across 4 major Turkish cities:")
                slot2.subheader("")
               
                slot3.image(tur_head_img,use_column_width=True)
               
                slot4.subheader('Sentiment across 4 major cities of Turkey:')
                slot5.subheader("")
                slot6.image(tur_head,use_column_width=True)
                
                #Turkish economy all cities
            if select1==countries[2] and select2==categories[2]:
                slot1.subheader("Public perception of Turkish economy across 4 major Turkish cities:")
                slot2.subheader("")
                
                slot3.image(tur_econ_img,use_column_width=True)
             
                slot4.subheader('Sentiment across 4 major cities of Turkey:')
                slot5.subheader("")
                slot6.image(tur_econ,use_column_width=True)
                
                #Turkish vaccine all cities
            if select1==countries[2] and select2==categories[3]:
                slot1.subheader("Public sentiment about Vaccination across 4 major Turkish cities:")
                slot2.subheader("")
              
                slot3.image(vaccn_img,use_column_width=True)
               
                slot4.subheader('Sentiment across 4 major cities of Turkey:')
                slot5.subheader("")
                slot6.image(tur_vaccn,use_column_width=True)
                
                
     
                

                
                
                
            
            
                
            
            
            
                
   
                    
        
        
                    
                    


    
    
    
    
    

    
#     stocks = ["India", "Turkey", "Germany"]

#     check_boxes = st.sidebar.checkbox('Select a Country',stocks)

#     page = st.sidebar.selectbox("Select a Country", ['',"India", "Turkey","Germany"])
#     page2 = st.sidebar.selectbox("Select a Topic", ["","Government", "Economy","Vaccine"])
    

#     if page=='' and page2=="":
#         st.button('Hey bro')
#         st.subheader("Compare and Analyse Public Sentiment on various Topics in 4 major Cities of Turkey, India and Germany!")
#         st.subheader("Select a topic or a country from the dropdown list to the left of the screen!")
#         st.text("")
#         image = Image.open('data/homepage.PNG')
#         st.image(image,use_column_width=True)

        
        
#     elif page == "India" and page2=='Government':
     
#         st.write(df_govt_in)
#         distribution_pickup =df_govt_in.groupby(["Location"])["Positive"].count().sort_values()
#         st.bar_chart(distribution_pickup)
#             #st.subheader("Select a city from the dropdown list")
#             #select=st.selectbox("",["Delhi","Mumbai","Chennai","Kolkata"])

                
        
#     elif page == "Turkey" and page2=='Government':

#         st.write(df_govt_tr)
#         distribution_pickup =df_govt_tr.groupby(["Location"])["Positive"].count().sort_values()
#         st.bar_chart(distribution_pickup)
#         #st.subheader("Select a city from the dropdown list")
#         #st.selectbox("",["Istanbul","Ankara","Izmir","Antalya"])
#         #st.write(df)
        
#         #visualize_data(df, x_axis, y_axis)

#     elif page == 'Germany' and page2=='Government':
     
#         st.write(df_govt_de)
#         distribution_pickup =df_govt_de.groupby(["Location"])["Positive"].count().sort_values()
#         st.bar_chart(distribution_pickup)
        
@st.cache
def load_data():
    df = pd.read_csv('./data/Final.csv',encoding='utf-8')
    df=df.iloc[:,1:]
    return df

@st.cache
def get_df(country,category=''):
    df = pd.read_csv('data/Final.csv',encoding='utf-8')
    if country==country and category=='':
        new_df=df[(df['Country']==country)|(df['Category']=='')]
    elif country=='India'and category=='Head of State':
        new_df=df[(df['Country']==country)&(df['Category']=='Narendra Modi')]
    elif country=='Germany'and category=='Head of State':
        new_df=df[(df['Country']==country)&(df['Category']=='Angela Merkel')]
    elif country=='Turkey'and category=='Head of State':
        new_df=df[(df['Country']==country)&(df['Category']=='Recep Tayyip Erdo?an')]
    else:
        new_df=df[(df['Country']==country)&(df['Category']==category)]
    return new_df.iloc[:,1:]


def generate_page(country,img1,img2):
    
    st.subheader("Public perception on various issues across 4 major cities of ",country)
    col1, col2 = st.beta_columns(2)
    slot1 = st.empty()
    slot1 = st.empty()
    slot2 = st.empty()
    slot3 = st.empty()
    slot4 = st.empty()
    slot5 = st.empty()
    slot6 = st.empty()
    
    
    col1.slot2.subheader("")
    image1 = Image.open(img1)
    col1.slot3.image(img_map,use_column_width=True)
    image2 = Image.open(img2)
    col2.slot4.subheader('Sentiment across 4 major cities of ', country)
    col2.slot5.subheader("")
    col2.slot6.image(image2,use_column_width=True)
   
    
    
    







def visualize_data(df, x_axis, y_axis):
    graph = alt.Chart(df).mark_circle(size=60).encode(
        x=x_axis,
        y=y_axis,
        color='Origin',
        tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
    ).interactive()

    st.write(graph)

if __name__ == "__main__":
    main()