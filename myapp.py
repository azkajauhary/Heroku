#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.models import CategoricalColorMapper, ColorPicker
from bokeh.palettes import Spectral6
from bokeh.layouts import widgetbox, row, gridplot
from bokeh.models import Slider, Select


# In[67]:


# import dataset
df = pd.read_csv("datacovid.csv")


# In[68]:


bandung = df.loc[df['nama_kab']=='KOTA BANDUNG'][['tanggal','nama_kab','confirmation','confirmation_selesai','confirmation_meninggal','pertumbuhan_confirmation','pertumbuhan_confirmation_selesai','pertumbuhan_confirmation_meninggal']]
bogor = df.loc[df['nama_kab']=='KOTA BOGOR'][['tanggal','nama_kab','confirmation','confirmation_selesai','confirmation_meninggal','pertumbuhan_confirmation','pertumbuhan_confirmation_selesai','pertumbuhan_confirmation_meninggal']]
depok = df.loc[df['nama_kab']=='KOTA DEPOK'][['tanggal','nama_kab','confirmation','confirmation_selesai','confirmation_meninggal','pertumbuhan_confirmation','pertumbuhan_confirmation_selesai','pertumbuhan_confirmation_meninggal']]
bandung['tanggal'] = pd.to_datetime(bandung['tanggal'])
bogor['tanggal'] = pd.to_datetime(bogor['tanggal'])
depok['tanggal'] = pd.to_datetime(depok['tanggal'])
bandung = bandung[bandung.tanggal.dt.year.eq(2020)]
bogor = bogor[bogor.tanggal.dt.year.eq(2020)]
depok = depok[depok.tanggal.dt.year.eq(2020)]


# In[69]:


source = ColumnDataSource(data={
    'x'       : bandung['tanggal'],
    'bandung'       : bandung['confirmation'],
    'bogor'       : bogor['confirmation'],
    'depok'       : depok['confirmation'],
})


# In[80]:


plot = figure(title="Simple line example", x_axis_label="x", y_axis_label="y")

line1 = plot.line(x='x', y='bandung', source=source, legend_label='Kota Bandung', color='blue', line_width=2)
line2 = plot.line(x='x', y='bogor', source=source, legend_label='Kota Bogor', color='red', line_width=2)
line3 = plot.line(x='x', y='depok', source=source, legend_label='Kota Depok', color='green', line_width=2)

plot.legend.location = 'top_left'

def update_plot(attr, old, new):
    y = y_select.value
    
    plot.yaxis.axis_label = y

    new_data = {
    'x'       : bandung['tanggal'],
    'bandung'       : bandung[y],
    'bogor'       : bogor[y],
    'depok'       : depok[y],
    }
    source.data = new_data
    
    plot.title.text = 'Title lah pokoknya'

y_select = Select(
    options=['confirmation','confirmation_selesai','confirmation_meninggal','pertumbuhan_confirmation','pertumbuhan_confirmation_selesai','pertumbuhan_confirmation_meninggal'],
    value='confirmation_selesai',
    title='y-axis data'
)

y_select.on_change('value', update_plot)

picker1 = ColorPicker(title="Line Color For Kota Bandung")
picker1.js_link('color', line1.glyph, 'line_color')

picker2 = ColorPicker(title="Line Color For Kota Bogor")
picker2.js_link('color', line2.glyph, 'line_color')

picker3 = ColorPicker(title="Line Color For Kota Depok")
picker3.js_link('color', line3.glyph, 'line_color')

layout = row(widgetbox(y_select, picker1, picker2, picker3), plot)
curdoc().add_root(layout)


# In[77]:


show(layout)


# In[65]:


depok[depok.tanggal.dt.year.eq(2020)]


# In[ ]:




