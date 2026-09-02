import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import pandas as pd

df = sns.load_dataset('iris')

# 1. matplotlib
fig, ax = plt.subplots() 
ax.scatter(df['sepal_length'], df['sepal_width'])
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_title('Iris Sepal Dimensions')
ax.legend(['Sepal'])
st.pyplot(fig)

# 2. seaborn
fig, ax = plt.subplots()
sns.histplot(data=df, x='petal_length', bins=20, ax=ax, kde=True)
ax.set_title('Petal Length Distribution')
st.pyplot(fig)

fig, ax = plt.subplots()
sns.boxplot(data=df, x='species', y='petal_length', ax=ax)
ax.set_title('Petal Length by Species')
st.pyplot(fig)

# 3. plotly
fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species')
fig.update_layout(title='Interactive Iris Sepal Scatter Plot',
                  updatemenus=[dict(
                      type="dropdown",
                      direction='down',
                      showactive=True,
                      x=0.1,
                      y=1.1,
                      buttons=list([
                          dict(
                              label="All",
                              method="update",
                              args=[{"visible": [True, True, True]}]
                          ),
                          dict(
                              label="Setosa Only",
                              method="update",
                              args=[{"visible": [True, False, False]}]
                          ),
                          dict(
                              label="Versicolor Only",
                              method="update",
                              args=[{"visible": [False, True, False]}]
                          ),
                          dict(
                              label="Virginica Only",
                              method="update",
                              args=[{"visible": [False, False, True]}]
                          )
                      ])
                  )])
st.plotly_chart(fig)

fig = px.line(df, x='sepal_length', y='sepal_width', color='species')
fig.update_layout(title='Interactive Iris Sepal Line Chart',
                  updatemenus=[dict(
                      type="dropdown",
                      direction='down',
                      showactive=True,
                      x=0.1,
                      y=1.1,
                      buttons=list([
                          dict(
                              label="All",
                              method="update",
                              args=[{"visible": [True, True, True]}]
                          ),
                          dict(
                              label="Setosa Only",
                              method="update",
                              args=[{"visible": [True, False, False]}]
                          ),
                          dict(
                              label="Versicolor Only",
                              method="update",
                              args=[{"visible": [False, True, False]}]
                          ),
                          dict(
                              label="Virginica Only",
                              method="update",
                              args=[{"visible": [False, False, True]}]
                          )
                      ])
                  )])
st.plotly_chart(fig)
