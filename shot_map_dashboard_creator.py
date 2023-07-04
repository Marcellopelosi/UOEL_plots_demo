import pandas as pd
import panel as pn
import plotly.express as px
from PIL import Image

def shot_dashboard(player, squad, df, background_image_path = "./football pitch.png"):

  #Load background image path
  pitch = Image.open(background_image_path)
  
  # Create scatterplot
  scatterplot = px.scatter(df, x='x_loc', y='y_loc', color='shot outcome',
  color_discrete_map={'Saved': 'yellow',
 'Off T': 'purple',
 'Post': 'white',
 'Blocked': 'red',
 'Wayward': 'black',
 'Goal': 'green'})
  
  
  scatterplot.update_xaxes(showticklabels=False)
  scatterplot.update_yaxes(showticklabels=False)
  
  # Set x and y labels
  scatterplot.update_xaxes(title='')
  scatterplot.update_yaxes(title='')
  
  scatterplot.update_layout(
      xaxis_range=[0, 120],
      yaxis_range=[0, 80],
      width=120*8,
      height=80*8,
      xaxis=dict(showgrid=False),
      yaxis=dict(showgrid=False),
      plot_bgcolor="rgba(0, 0, 0, 0)"
  )
  
  # Add background
  scatterplot.add_layout_image(
          dict(
              source=pitch,
              xref="x",
              yref="y",
              x=0,
              y=68,
              sizex=120,
              sizey=80,
              sizing="stretch",
              opacity=0.5,
              layer="below")
  )
  
  # Create table
  df = df[['period', 'minute', 'second', 'shot outcome','body part', 'type of shot',  'squad against']].reset_index(drop = True)
  table = pn.widgets.DataFrame(df[['period', 'minute', 'second', 'shot outcome','body part', 'type of shot',  'squad against']])
  
  # Create a title panel
  title_panel = pn.pane.Markdown(f'{player} shot map with {squad} in 2022 WC', style={'font-size': '20px', 'font-weight': 'bold'})
  
  # Align center
  spacer = pn.Spacer()  # Create a spacer to center-align
  title_panel = pn.Row(spacer, title_panel, spacer, align='center')
  table = pn.Row(spacer, table, spacer, align='center')
  scatterplot = pn.Row(spacer, scatterplot, spacer, align='center')
  
  # Create a column layout with all the elements previously created
  dashboard = pn.Column(title_panel, scatterplot, table)

  return dashboard
