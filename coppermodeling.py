import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu


# Add a title to your Streamlit app
st.markdown('<h1 style="color:#B22222;">Industrial Copper Modelling</h1>', unsafe_allow_html=True)
st.write("**The Best Predictor!**")

#set up the sidebar with optionmenu

task = option_menu("",options=["Home","Price Prediction","Status Prediction","About"],
                        icons=["house","cash",'check',"info-circle"],
                        default_index=1,
                        orientation="horizontal",
                            styles={"container": {"width": "100%", "border": "2px ridge", "background-color": "#006400"},
                                    "icon": {"color": "#F8CD47", "font-size": "20px"}, 
                                    "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "color": "#FFFFFF"},
                                    "nav-link-selected": {"background-color": "#000000", "color": "#FFFFFF"}})


# set up the information for 'Home' menu
if task == 'Home':
    title_text = '''<h1 style='font-size: 30px;text-align: center; color:#B22222;'> COPPER : Properties & Applications </h1>'''
    st.markdown(title_text, unsafe_allow_html=True)

    st.subheader(":green[Copper :]")

    st.markdown('''Copper is one of the few metals that can occur in nature in a directly usable metallic form (native metals).
                This led to very early human use in several regions, from 8000 BC. Thousands of years later, it was the first metal to be smelted from sulfide ore in
                5000 BC; the first metal to be cast into a shape in a mold in 4000 BC; and the first metal to be purposely alloyed with another metal, tin,
                to create bronze 3500 BC.
                Copper is a versatile and widely used metal known for its excellent electrical conductivity,thermal conductivity, malleability
                and resistance to corrosion.
                Copper is a chemical element; it has symbol Cu (from Latin cuprum) and atomic number 29.
                It is a soft, malleable, and ductile metal with very high thermal and electrical conductivity.
                A freshly exposed surface of pure copper has a pinkish-orange color. Copper is used as a conductor of heat and electricity, as a building material
                and as a constituent of various metal alloys, such as sterling silver used in jewelry, cupronickel used to make marine hardware and coins
                and constantan used in strain gauges and thermocouples for temperature measurement.''')

    st.subheader(':green[Properties of Copper :]')

    st.markdown(''':orange[**Electrical Conductivity :**] Copper has the highest electrical conductivity of any non-precious metal,
                        making it ideal for electrical wiring.''')
    
    st.markdown(''':orange[**Thermal Conductivity :**] It is an excellent conductor of heat, which makes it useful in heat exchangers and cookware.''')

    st.markdown(''':orange[**Corrosion Resistance :**] Copper forms a protective oxide layer that helps resist corrosion, especially in moist environments.''')

    st.markdown(''':orange[**Malleability and Ductility :**] Copper can be easily shaped and drawn into wires without breaking.''')

    st.markdown(''':orange[**Antimicrobial Properties :**] Copper has natural antimicrobial properties, which help reduce the spread of harmful bacteria..''')

    st.subheader(":green[Applications of Copper :]")

    st.write("1. Electrical and Electronics")
    st.write("2. Construction and Architecture")
    st.write("3. Transportation")
    st.write("4. Industrial Machinery")
    st.write("5. Consumer Products")
    st.write("6. Renewable Energy")

    st.subheader(":green[Environmental and Health Considerations :]")
    st.markdown(''':orange[**Recyclability :**] Copper is 100 Percent recyclable without any loss of quality, making it an environmentally friendly material.''')
    st.markdown(''':orange[**Health Benefits :**] Copper's antimicrobial properties are utilized in healthcare settings to reduce the spread of infections.''')

# User input Values:

class option():
    
    country_values=[ 25.,  26.,  27.,  28.,  30.,  32.,  38.,  39.,  40.,  77.,  78., 79.,  80.,  84.,  89., 107., 113.]

    status_values=['Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM','Wonderful', 'Revised',
            'Offered', 'Offerable']

    status_encoded = {'Lost':0, 'Won':1, 'Draft':2, 'To be approved':3, 'Not lost for AM':4,'Wonderful':5, 'Revised':6,
                    'Offered':7, 'Offerable':8}
    
    item_type_values=['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']

    item_type_encoded = {'W':5.0, 'WI':6.0, 'S':3.0, 'Others':1.0, 'PL':2.0, 'IPL':0.0, 'SLAWR':4.0}

    application_values=[2.0, 3.0, 4.0, 5.0, 10.0, 15.0, 19.0, 20.0, 22.0, 25.0, 26.0, 27.0, 28.0, 29.0, 38.0, 39.0, 40.0,
                41.0, 42.0, 56.0, 58.0, 59.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 79.0, 99.0]
    
    product_ref_values=[611728, 611733, 611993, 628112, 628117, 628377, 640400, 640405, 640665, 164141591, 164336407,
                164337175, 929423819, 1282007633, 1332077137, 1665572032, 1665572374, 1665584320, 1665584642,
                1665584662, 1668701376, 1668701698, 1668701718, 1668701725, 1670798778, 1671863738, 1671876026,
                1690738206, 1690738219, 1693867550, 1693867563, 1721130331, 1722207579]

if task == 'Price Prediction':
    title_text = '''<h1 style='font-size: 32px;text-align: center;color:#B22222;'>Copper Selling Price Prediction</h1>'''
    st.markdown(title_text, unsafe_allow_html=True)
    

    st.markdown("<h5 style=color:#006400>Provide the following Information:",unsafe_allow_html=True)
    st.write('')

    # creted form to get the user input 
    with st.form('prediction'):
        col1,col2=st.columns(2)

        with col1:

            Item_Date=st.date_input(label='**Item Date**',format='DD/MM/YYYY')

            Country=st.selectbox(label='**Country**',options=option.country_values,index=None)

            Item_Type=st.selectbox(label='**Item Type**',options=option.item_type_values,index=None)

            Application=st.selectbox(label='**Application**',options=option.application_values,index=None)

            Product_Ref=st.selectbox(label='**Product Ref**',options=option.product_ref_values,index=None)

            Customer_Id=st.number_input('**Customer ID**',min_value=10000)

        with col2:

            Delivery_Date=st.date_input(label='**Delivery Date**',format='DD/MM/YYYY')

            Status=st.selectbox(label='**Status**',options=option.status_values,index=None)

            Quantity=st.number_input(label='**Quantity**',min_value=0.1)

            Width=st.number_input(label='**Width**',min_value=1.0)

            Thickness=st.number_input(label='**Thickness**',min_value=0.1)

            st.markdown('<br>', unsafe_allow_html=True)
            
            button=st.form_submit_button(':red[**Predict Selling Price**]',use_container_width=True)

    if button:
        #check whether user fill all required fields
        if not all([Item_Date, Delivery_Date, Country, Item_Type, Application, Product_Ref,
                    Customer_Id, Status, Quantity, Width, Thickness]):
            st.error("Data Missing, Complete all the information above.")

        else:
            
            #opened pickle model and predict the selling price with user data
            with open('Random_forest_regressor.pkl','rb') as files:
                predict_model=pickle.load(files)

            # customize the user data to fit the feature 
            Status=option.status_encoded[Status]
            Item_Type=option.item_type_encoded[Item_Type]

            Delivery_Time_Taken=abs((Item_Date - Delivery_Date).days)

            Quantity_Log=np.log(Quantity)
            Thickness_Log=np.log(Thickness)

            #predict the selling price with regressor model
            user_data=np.array([[Customer_Id, Country, Status, Item_Type ,Application, Width, Product_Ref,
                                Delivery_Time_Taken, Quantity_Log, Thickness_Log]])
            
            pred=predict_model.predict(user_data)

            selling_price_pred=np.exp(pred[0])

            #display the predicted selling price 
            st.subheader(f":green[Predicted Selling Price :] {selling_price_pred:.2f}") 
            st.snow()
    
if task == 'Status Prediction':
    title_text = '''<h1 style='font-size: 32px;text-align: center;color:#B22222;'>Copper Status Prediction</h1>'''
    st.markdown(title_text, unsafe_allow_html=True)
    st.markdown("<h5 style=color:#006400;>Provide the following information:",unsafe_allow_html=True)
    st.write('')

    #creted form to get the user input 
    with st.form('classifier'):
        col1,col2=st.columns(2)
        with col1:

            Item_Date=st.date_input(label='**Item Date**',format='DD/MM/YYYY')

            Country=st.selectbox(label='**Country**',options=option.country_values,index=None)

            Item_Type=st.selectbox(label='**Item Type**',options=option.item_type_values,index=None)

            Application=st.selectbox(label='**Application**',options=option.application_values,index=None)

            Product_Ref=st.selectbox(label='**Product Ref**',options=option.product_ref_values,index=None)

            Customer_Id=st.number_input('**Customer ID**',min_value=10000)

        with col2:

            Delivery_Date=st.date_input(label='**Delivery Date**',format='DD/MM/YYYY')

            Quantity=st.number_input(label='**Quantity**',min_value=0.1)

            Width=st.number_input(label='**Width**',min_value=1.0)

            Thickness=st.number_input(label='**Thickness**',min_value=0.1)

            Selling_Price=st.number_input(label='**Selling Price**',min_value=0.1)

            st.markdown('<br>', unsafe_allow_html=True)
            
            button=st.form_submit_button(':red[**Predict Copper Status**]',use_container_width=True)

    if button:
        #check whether user fill all required fields
        if not all([Item_Date, Delivery_Date, Country, Item_Type, Application, Product_Ref,
                    Customer_Id,Quantity, Width,Selling_Price]):
            st.error("Please fill in all required fields.")

        else:
            #opened pickle model and predict status with user data
            with open('Extra_trees_classifier.pkl','rb') as files:
                model=pickle.load(files)

            # customize the user data to fit the feature 
            Item_Type=option.item_type_encoded[Item_Type]

            Delivery_Time_Taken=abs((Item_Date - Delivery_Date).days)

            Quantity_Log=np.log(Quantity)
            Thickness_Log=np.log(Thickness)
            Selling_Price_Log=np.log(Selling_Price)

            #predict the status with classifier model
            user_data=np.array([[Customer_Id, Country,Item_Type ,Application, Width, Product_Ref,
                                Delivery_Time_Taken, Quantity_Log, Thickness_Log,Selling_Price_Log]])
            
            status=model.predict(user_data)

            #display the predicted status 
            if status==1:
                st.subheader(f":green[Status of the Copper :] Won")
                st.snow()

            else:
                st.subheader(f":red[Status of the Copper :] Lost")
                st.snow()

#set up information for 'About' menu 
if task == "About":
    st.subheader(':green[Project Title :]')
    st.markdown('<h5> Industrial Copper Modelling',unsafe_allow_html=True)

    st.subheader(':green[Processes :]')
    st.markdown(' <h5> Python scripting, Data Preprocessing, Machine learning, Exploratory Data Analysis, Streamlit',unsafe_allow_html=True)

    st.subheader(':green[Information :]')
    st.markdown('''**This Project - Industrial Copper Modelling was done by myself, :red[**NAGAPPAN M.S**]**''')
    st.markdown('''**To refer codes of this project, refer my Github page by clicking on the button below**''')
    st.link_button('**Go to Github**','https://github.com/nagappanms/DS_Industrial-Copper-Modeling.git')