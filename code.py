count_actividad = pd.DataFrame()
for medio in medios:
    count_actividad[medio] = data_CF[medio].apply(lambda x: 1 if x > 0 else 0)
count_actividad = pd.melt(count_actividad,
                         value_vars=medios,
                         var_name='medios',
                         value_name='Semanas')
count_actividad = count_actividad.groupby(['medios'])['Semanas'].sum().reset_index()
px.bar(count_actividad,
      x='medios',
      y='Semanas',
      color='medios' ,
      text='Semanas',
      title='Numero de semanas que mantuvieron activa la inversion')


#----



data_CF_year_share = pd.DataFrame()
for medio in medios:
    data_CF_year_share[medio] =data_CF.groupby(['year'])[medios].sum().apply(lambda x: round((x[medio]*100) / x.sum(axis=0),3), axis=1)
data_CF_year_share = data_CF_year_share.reset_index()
data_CF_year_share = pd.melt(data_CF_year_share,
                            id_vars='year',
                            value_vars=medios,
                            var_name='medios',
                            value_name='% Participacion')
data_CF_year_share['year'] = data_CF_year_share['year'].astype(str)
plot_share = px.bar(data_CF_year_share,
              x = 'medios',
              y = '% Participacion',
              color='year',
              barmode='group',
              text='% Participacion')
#plot_share.update_traces(texttemplate='%{text:.0%}')
plot_share.show()


#---

px.bar(best_params.query('Parametro == "length"'),
      x = 'Medio',
      y = 'values',
      color = 'Medio')

#---

px.bar(best_params.query('Parametro == "strength"'),
      x = 'Medio',
      y = 'values',
      color = 'Medio')

#-----

px.bar(best_params.query('Parametro == "a"'),
      x = 'Medio',
      y = 'values',
      color = 'Medio')


#----

fig = go.Figure()
for i, medio in enumerate(medios):
    medio_sat = medio +'_Adbug'
    data_adstock = data_model
    fig.add_trace(go.Scatter(x=data_adstock[medio], 
                             y=data_adstock[medio_sat],
                            mode='markers',
                            name=medio))
fig.show()