import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Bedingungen fuer Pierce Kompatibilitaet festlegen 
st.title('outlier detection')
st.write('Please upload your data without units as one column and a categorie name of your choice.')
st.write('The maximum number of values must be 60 or less.')

#Datei importieren und einlesen:
df3 = st.file_uploader('Choose your data', type=["xlsx", 'csv'])

if df3 is None:
   st.write('no file chosen')

if df3 is not None:
    if df3.name.endswith('xlsx'):
      df2 = pd.read_excel(df3)
      data = df2.to_numpy()
    if df3.name.endswith('csv'):
       df2 = pd.read_csv(df3)
       data = df2.to_numpy()

#allgemeine Outlier Detection:
def OutlierDetection(measure):

  Rvalues =[
    [1.196,None,None,None,None,None,None,None, ],
    [1.383, 1.078,None,None,None,None,None,None, ],
    [1.509, 1.2,None,None,None,None,None,None, ],
    [1.61, 1.299, 1.099,None,None,None,None,None, ],
    [1.693, 1.382, 1.187, 1.022,None,None,None,None, ],
    [1.763, 1.453, 1.261, 1.109,None,None,None,None, ],
    [1.824, 1.515, 1.324, 1.178, 1.045,None,None,None, ],
    [1.878, 1.57, 1.38, 1.237, 1.114,None,None,None, ],
    [1.925, 1.619, 1.43, 1.289, 1.172, 1.059,None,None, ],
    [1.969, 1.663, 1.475, 1.336, 1.221, 1.118, 1.009,None, ],
    [2.007, 1.704, 1.516, 1.379, 1.266, 1.167, 1.07,None, ],
    [2.043, 1.741, 1.554, 1.417, 1.307, 1.21, 1.12, 1.026, ],
    [2.076, 1.775, 1.589, 1.453, 1.344, 1.249, 1.164, 1.078, ],
    [2.106, 1.807, 1.622, 1.486, 1.378, 1.285, 1.202, 1.122, 1.039],
    [2.134, 1.836, 1.652, 1.517, 1.409, 1.318, 1.237, 1.161, 1.084],
    [2.161, 1.864, 1.68, 1.546, 1.438, 1.348, 1.268, 1.195, 1.123],
    [2.185, 1.89, 1.707, 1.573, 1.466, 1.377, 1.298, 1.226, 1.158],
    [2.209, 1.914, 1.732, 1.599, 1.492, 1.404, 1.326, 1.255, 1.19],
    [2.23, 1.938, 1.756, 1.623, 1.517, 1.429, 1.352, 1.282, 1.218],
    [2.251, 1.96, 1.779, 1.646, 1.54, 1.452, 1.376, 1.308, 1.245],
    [2.271, 1.981, 1.8, 1.668, 1.563, 1.475, 1.399, 1.332, 1.27],
    [2.29, 2, 1.821, 1.689, 1.584, 1.497, 1.421, 1.354, 1.293],
    [2.307, 2.019, 1.84, 1.709, 1.604, 1.517, 1.442, 1.375, 1.315],
    [2.324, 2.037, 1.859, 1.728, 1.624, 1.537, 1.462, 1.396, 1.336],
    [2.341, 2.055, 1.877, 1.746, 1.642, 1.556, 1.481, 1.415, 1.356],
    [2.356, 2.071, 1.894, 1.764, 1.66, 1.574, 1.5, 1.434, 1.375],
    [2.371, 2.088, 1.911, 1.781, 1.677, 1.591, 1.517, 1.452, 1.393],
    [2.385, 2.103, 1.927, 1.797, 1.694, 1.608, 1.534, 1.469, 1.411],
    [2.399, 2.118, 1.942, 1.812, 1.71, 1.624, 1.55, 1.486, 1.428],
    [2.412, 2.132, 1.957, 1.828, 1.725, 1.64, 1.567, 1.502, 1.444],
    [2.425, 2.146, 1.971, 1.842, 1.74, 1.655, 1.582, 1.517, 1.459],
    [2.438, 2.159, 1.985, 1.856, 1.754, 1.669, 1.597, 1.532, 1.475],
    [2.45, 2.172, 1.998, 1.87, 1.768, 1.683, 1.611, 1.547, 1.489],
    [2.461, 2.184, 2.011, 1.883, 1.782, 1.697, 1.624, 1.561, 1.504],
    [2.472, 2.196, 2.024, 1.896, 1.795, 1.711, 1.638, 1.574, 1.517],
    [2.483, 2.208, 2.036, 1.909, 1.807, 1.723, 1.651, 1.587, 1.531],
    [2.494, 2.219, 2.047, 1.921, 1.82, 1.736, 1.664, 1.6, 1.544],
    [2.504, 2.23, 2.059, 1.932, 1.832, 1.748, 1.676, 1.613, 1.556],
    [2.514, 2.241, 2.07, 1.944, 1.843, 1.76, 1.688, 1.625, 1.568],
    [2.524, 2.251, 2.081, 1.955, 1.855, 1.771, 1.699, 1.636, 1.58],
    [2.533, 2.261, 2.092, 1.966, 1.866, 1.783, 1.711, 1.648, 1.592],
    [2.542, 2.271, 2.102, 1.976, 1.876, 1.794, 1.722, 1.659, 1.603],
    [2.551, 2.281, 2.112, 1.987, 1.887, 1.804, 1.733, 1.67, 1.614],
    [2.56, 2.29, 2.122, 1.997, 1.897, 1.815, 1.743, 1.681, 1.625],
    [2.568, 2.299, 2.131, 2.006, 1.907, 1.825, 1.754, 1.691, 1.636],
    [2.577, 2.308, 2.14, 2.016, 1.917, 1.835, 1.764, 1.701, 1.646],
    [2.585, 2.317, 2.149, 2.026, 1.927, 1.844, 1.773, 1.711, 1.656],
    [2.592, 2.326, 2.158, 2.035, 1.936, 1.854, 1.783, 1.721, 1.666],
    [2.6, 2.334, 2.167, 2.044, 1.945, 1.863, 1.792, 1.73, 1.675],
    [2.608, 2.342, 2.175, 2.052, 1.954, 1.872, 1.802, 1.74, 1.685],
    [2.615, 2.35, 2.184, 2.061, 1.963, 1.881, 1.811, 1.749, 1.694],
    [2.622, 2.358, 2.192, 2.069, 1.972, 1.89, 1.82, 1.758, 1.703],
    [2.629, 2.365, 2.2, 2.077, 1.98, 1.898, 1.828, 1.767, 1.711],
    [2.636, 2.373, 2.207, 2.085, 1.988, 1.907, 1.837, 1.775, 1.72],
    [2.643, 2.38, 2.215, 2.093, 1.996, 1.915, 1.845, 1.784, 1.729],
    [2.65, 2.387, 2.223, 2.101, 2.004, 1.923, 1.853, 1.792, 1.737],
    [2.656, 2.394, 2.23, 2.109, 2.012, 1.931, 1.861, 1.8, 1.745],
    [2.663, 2.401, 2.237, 2.116, 2.019, 1.939, 1.869, 1.808, 1.753]
]
  # Berechnugnen 
  mean = abs(measure.mean())
  stand_dev = np.std(measure)
  sus_val = abs(measure - mean) / stand_dev   #jeder Wert der Rohdaten wird als suspecious behandelt, um später zu testen, ob einer der Werte tatsächlich ein Outlier ist 

  #Startwert in Rvalues nested list (geht bis 8 Elemente, bzw. 9 suspicious Messwerte):
  n_sus_val = 0

  while True:

    #Fuer mehr als 60 or weniger als 3 Messwerte:
    if len(measure) > 61 or len(measure) < 3:
      st.write('Pierce Method only allows a number of measurements greater 2 and less 61. Please adjust your data input!')
      break

    #Fuer die passende Anzhal an Messwerten:
    if len(measure) <= 60 or len(measure) >= 3:

      #Laenge des Arrays -3, weil Rvalues erst mit 3 Messwerten startet
      #Festlegen, was ein tatsächlicher Outlier ist 
      outliers = sus_val > Rvalues[len(measure)-3][n_sus_val]             # => True oder False output

       #falls keine Outlier:
      if any(outliers) == False:
        st.write('No Outliers in your data detected.')
        break

      #wenn mehr als 9 Outlier oder kein Rvalues, dann kein R Wert anbietet:
      if n_sus_val>8 or Rvalues[len(measure)-3][n_sus_val] == None:
        st.write('No robust statistic for Pierce Criteria')
        break

      #sobald sich in der Schleife die Anzahl an Outliern nicht mehr ändert, wird Rechnung abgebrochen und Outlier ausgegeben:
      if sum(outliers) == n_sus_val:
        df = pd.DataFrame({
        'outlier': outliers.tolist(),        #Tabelle aus 2 Spalten: ja/nein (true/ falls) und alle Rohdaten 
        'values' : measure.tolist(),
        })

        #Output:
        st.write('Analyzed data with Outlier(s) marked as True:')
        st.write(df)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[12, 4])

        ##Scatter Plot:
        #Outlier:
        fil = df['outlier'].apply(lambda x: True in x)
        y1 = df.loc[fil]['values'].tolist()
        x1 = df[fil].index                                 # index = y1.index funktioniert nicht, da x und y gleichgroß sein müssen
        ax1.scatter(x1, y1, c='red', label='Outlier')

        #Cleaned Data:
        fil_clean = df.loc[~fil]['values']
        y2 = fil_clean.tolist()
        x2 = df[~fil].index

        ax1.scatter(x2, y2, c='black', label='cleaned data')

        #Standard Deviation ohne Outlier:
        clean_val = []
        for i in fil_clean:
          res = i[0]
          clean_val.append(res)
          clean_data = np.array(clean_val)
        ax1.fill_between(fil_clean.index, clean_data.std(), -clean_data.std(), color='black', alpha=0.2, label='standard deviation cleaned data')

        #Standard Deviation mit Outliern:
        ax1.fill_between(df2.index, measure.std(), -measure.std(), color='grey', alpha=0.2, label='standard deviation raw data')

        #Histogramm
        hist_data = df['values'][~fil]
        val = hist_data.values

        hist_val = []
        for i in val:
          res = i[0]
          hist_val.append(res)

        ax2.hist(x=hist_val, bins=len(hist_val), linewidth=0.2, edgecolor='k')

        #Plot Formatierung:
        ax1.set_ylabel('measurments')
        ax1.legend(loc = 'upper left', ncols= 2, bbox_to_anchor=(0,0.2,1,1))

        ax2.set_xlabel('Value')
        ax2.set_ylabel('Probability density')
        ax2.set_title('Histogram of normal distribution: cleaned data')

        st.pyplot(fig)

        break

      #für eine feste Anzahl an Messwerten werden mit zunehmender Anzahl die angenommenen Outliern (Anzahl an suspicious Messwerten) immer gegen einen neues R Wert gecheckt
      else:
        n_sus_val +=1

if df3 is not None:
  OutlierDetection(data)

