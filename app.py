import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -------------------------------
# 1. ESTILOS PERSONALIZADOS
# -------------------------------
st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #000000;
            color: #FFD700;
            font-family: 'Trebuchet MS', sans-serif;
        }

        table {
            background-color: #000000;
            color: #FFD700;
            border: 1px solid #FFD700;
        }

        th {
            background-color: #222222;
            color: #FFD700;
        }

        td {
            background-color: #111111;
            color: #FFD700;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# 2. DATASET
# -------------------------------
data = {
    "Nombre": ["Ana", "Juan", "Lucía", "Carlos"],
    "Edad": [30, 29, 31, 28],
    "Salario": [45000, 50000, 47500, 44000],
    "Antigüedad": [3, 2, 4, 1]
}
df = pd.DataFrame(data)

# -------------------------------
# 3. SIDEBAR CON FILTROS
# -------------------------------
st.sidebar.title("🔧 Filtros")

nombre_filtrado = st.sidebar.selectbox("Seleccionar empleado", ["Todos"] + list(df["Nombre"].unique()))
antiguedad_min = st.sidebar.slider("Antigüedad mínima (años)", min_value=0, max_value=5, value=0)
color = st.sidebar.color_picker("Color del gráfico", "#FFD700")

# -------------------------------
# 4. FILTRADO DE DATOS
# -------------------------------
df_filtrado = df[df["Antigüedad"] >= antiguedad_min]

if nombre_filtrado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Nombre"] == nombre_filtrado]

# -------------------------------
# 5. CONTENIDO PRINCIPAL
# -------------------------------
st.title("Dashboard de Empleados")

st.write("👀 Vista previa del dataset filtrado:")
st.markdown(df_filtrado.to_html(index=False), unsafe_allow_html=True)

# -------------------------------
# 6. GRÁFICO CON PLOTLY
# -------------------------------
if not df_filtrado.empty:
    fig = go.Figure(
        data=[go.Bar(
            x=df_filtrado["Nombre"],
            y=df_filtrado["Salario"],
            marker=dict(color=color, line=dict(width=1, color="black")),
            width=0.5,
        )]
    )

    fig.update_layout(
        plot_bgcolor="#000000",
        paper_bgcolor="#000000",
        font=dict(color="#FFD700"),
        title="📊 Salario por empleado"
    )

    st.plotly_chart(fig)
else:
    st.warning("No hay empleados que cumplan con los filtros seleccionados.")

# -------------------------------
# 7. ESTADÍSTICAS
# -------------------------------
st.subheader("📈 Estadísticas básicas")
st.write(df_filtrado.describe())
