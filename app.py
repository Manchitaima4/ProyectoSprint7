import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
st.header('Proyecto Sprint 7')
hist_button = st.button('Construir histograma')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

#Agrega otro botón que, al hacer clic en él, construya un gráfico de dispersión 
# plotly-express. 
# Nuevamente, considera utilizar las funciones st.write() y st.plotly_chart().
disp_button = st.button("Construir gráfico de dispersión")

if disp_button:
    # escribimos el mensaje
    st.write("Creación de un diagrama de dispersión")

    #Crear el diagrama de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price")

    #Mostramos el grafico
    st.plotly_chart(fig2, use_container_width=True)

