# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 00:10:30 2020

@author: AKSHATA G. NAYAK
"""

import pandas as pd
import dash
import dash_html_components as html
import webbrowser
import sys
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
from dash.exceptions import PreventUpdate
import datetime


app=dash.Dash()  #creating an aobject

def open_browser():
    print('open browser')          
    webbrowser.open_new('http://127.0.0.1:8050/')     #for connecting to browser
    

def load_data():
    dataset_name = 'global_terror.csv'    #dataset
    global df
    df = pd.read_csv(dataset_name)        #convert database into csv file
    print(df['iyear'].unique().tolist())  #only unique values of year
    print(df.sample(5))
    
    global temp_list
    temp_list = sorted(df['country_txt'].unique().tolist())
    
    global country_list
    country_list = [{'label':str(i),'value':str(i)}for i in temp_list]
    
    
    
    global year_list 
    year_list =sorted(df['iyear'].unique().tolist())
    
    global year_dict
    year_dict = {str(year):str(year) for year in year_list} #for slider we need dict
    
    global chart_dropdown_values
    chart_dropdown_values ={"Terrorist Organisation":'gname',
                            "Target Nationality" : 'natlty1_txt',
                            "Target Type" : 'targtype1_txt',
                            "Type of Attack" : 'attacktype1_txt',
                            "Weapon Type" : 'weaptype1_txt',
                            "Region":'region_txt',
                            "Country Attacked" : 'country_txt'}
    
    chart_dropdown_values = [{"label" : keys, "value" : value} for keys, value in chart_dropdown_values.items() ]
    
    
    global chart_dropdown_values1
    chart_dropdown_values1 ={"Terrorist Organisation":'gname',
                            "Target Nationality" : 'natlty1_txt',
                            "Target Type" : 'targtype1_txt',
                            "Type of Attack" : 'attacktype1_txt',
                            "Weapon Type" : 'weaptype1_txt',
                            "Region": 'region_txt',
                            "Country Attacked" : 'country_txt'}
    
    chart_dropdown_values1 = [{"label" : keys, "value" : value} for keys, value in chart_dropdown_values1.items() ]

    month = {
        'January' : 1,
        'February' : 2,
        'March' : 3,
        'April' : 4,
        'May' : 5,
        'June' : 6,
        'July' : 7,
        'August' : 8,
        'September' : 9,
        'October' : 10,
        'November' : 11,
        'December' :12}

    global month_list
    month_list = [{'label':key,'value':values}for key,values in month.items()]
    
    global day_list
    day_list = [{'label':str(i),'value':str(i)}for i in range(1,32)]
    
    global region_list
    region_list = [{'label':str(i),'value':str(i)}for i in sorted(df['region_txt'].unique().tolist())]
    
    global state_list
    state_list = [{'label':str(i),'value':str(i)}for i in sorted(df['provstate'].astype(str).unique().tolist())]
    
    global city_list
    city_list = [{'label':str(i),'value':str(i)}for i in sorted(df['city'].astype(str).unique().tolist())]
    
    global attack_list
    attack_list = [{'label':str(i),'value':str(i)}for i in sorted(df['attacktype1_txt'].astype(str).unique().tolist())]
   
    
def create_app_ui():
    main_layout = main_layout = html.Div([
    
    html.H3(datetime.datetime.now().strftime('%d-%m-%Y'),style={'text-align':'right', 'color':'white'}) ,
    html.Div([html.Img(src='/assets/logo.png', style={'height':'80px', 'width' :'80px'})],style={'textAlign':'center'}),
    html.H1('Terrorism Analysis with Insights', id='Main_title', style={'text-align':'center', 'color':'white'}),
  
  
  dcc.Tabs(id="Tabs", value="tab-1",children=[
      dcc.Tab(label="Map Tool" ,id="Map tool",value="tab-1", children=[
      dcc.Tabs(id = "subtabs", value = "tab-1",children = [
              dcc.Tab(label="World Map Tool", id="World", value="tab-1", children = [ html.Div([
   
    
    
  
    
    html.H3('World Map Showing Attacks from 1970-2018', id='side_title', style={'text-align':'center', 'color':'white'}),
    dcc.Dropdown(id='month-dd', options = month_list,placeholder='Select Month',multi=True,style={'backgroundColor':'#5efb6e','borderColor' : 'black','color':'black','borderRadius':'30px'},className='custom-dropdown'),
    dcc.Dropdown(id='day-dd', options = day_list,placeholder='Select Day',multi=True,style={'backgroundColor':'#6afb92','borderColor' : 'black','color':'black','borderRadius':'30px'}),
    dcc.Dropdown(id='region-dd', options = region_list,placeholder='Select Region',multi=True,style={'backgroundColor':'#5efb6e','borderColor' : 'black','color':'black','borderRadius':'30px'}),
    dcc.Dropdown(id='country-dd', options = country_list,placeholder='Select Country',multi=True,style={'backgroundColor':'#6afb92','borderColor' : 'black','color':'black','borderRadius':'30px'}),
    dcc.Dropdown(id='state-dd', options = state_list,placeholder='Select Stae or Proviance',multi=True,style={'backgroundColor':'#5efb6e','borderColor' : 'black','color':'black','borderRadius':'30px'}),
    dcc.Dropdown(id='city-dd', options = city_list,placeholder='Select City',multi=True,style={'backgroundColor':'#6afb92','color':'black','borderColor' : 'black','borderRadius':'30px'}),
    dcc.Dropdown(id='attack-dd', options = attack_list,placeholder='Select Attack Type',multi=True,style={'backgroundColor':'#5efb6e','color':'black','borderColor' : 'black','borderRadius':'30px'}),
    html.Button('Reset',id='close_button',n_clicks = 0,
                                                        style={'marginLeft': 600,
                                                             'marginRight': 610,
                                                             'marginTop': 30,
                                                             'padding':'5px 15px',
                                                             'background-color':'white',
                                                             'color':'black',
                                                             'font-size':'20px',
                                                             'border':'3px solid #4caf50',
    
                                                             'width':'150px'},),
    dcc.Loading(
            id="loading-1",
            type="default",
            children=html.Div(id="loading-output-1")
        ),
    dcc.Graph(id='graph-obj'),
   
    html.H1(id='stat',children='Loading...',style={'text-align':'center', 'color':'#32ff0c'}),
    dcc.RangeSlider(
        id ='year-sld',
        min = min(year_list),
        max = max(year_list),
        value = [min(year_list), max(year_list)],
        marks = year_dict
        ),
     
                                                                             
       ])]),
              
              
              
    dcc.Tab(label="India Map Tool", id="India", value="tab-2", children =[html.Div([
   
   
    html.H3('India Map Showing Attacks from 1970-2018', id='side_title2', style={'text-align':'center', 'color':'white'}),
    dcc.Dropdown(id='month-dd1', options = month_list,placeholder='Select Month',multi=True,style={'backgroundColor':'#5efb6e','borderColor' : 'black','color':'black','borderRadius':'30px'},),
    dcc.Dropdown(id='day-dd1', options = day_list,placeholder='Select Day',multi=True,style={'backgroundColor':'#6afb92','borderColor' : 'black','borderRadius':'30px'},),
    dcc.Dropdown(id='region-dd1', options = region_list,placeholder='Select Region',value='South Asia', disabled=True,style={'backgroundColor':'#5efb6e','borderColor' : 'black','color':'black','borderRadius':'30px'},),
    dcc.Dropdown(id='country-dd1', options =country_list,placeholder='Select Country',value="India",disabled = True,style={'backgroundColor':'#6afb92','borderColor' : 'black','borderRadius':'30px'},),
    dcc.Dropdown(id='state-dd1', options = state_list,placeholder='Select Stae or Proviance',multi=True,style={'backgroundColor':'#5efb6e','borderColor' : 'black','color':'black','borderRadius':'30px'},),
    dcc.Dropdown(id='city-dd1', options =city_list,placeholder='Select City',multi=True,style={'backgroundColor':'#6afb92','borderColor' : 'black','borderRadius':'30px'},),
    dcc.Dropdown(id='attack-dd1', options = attack_list,placeholder='Select Attack Type',multi=True,style={'backgroundColor':'#5efb6e','borderColor' : 'black','color':'black','borderRadius':'30px'},),
    
     html.Button('Reset',id='close_button1',n_clicks = 0, style={'marginLeft': 600, 'marginRight': 610,'marginTop': 30,
                                                             'padding':'5px 15px',
                                                             'background-color':'white',
                                                             'color':'black',
                                                             'font-size':'20px',
                                                             'border':'3px solid #4caf50',
                                                             'width':'150px'},),
    html.Div(children=[
     
     dcc.Graph(id='graph-obj1'),
     dcc.Loading(
            id="loading-2",
            type="default",
            children=html.Div(id="loading-output-2")
        ),
    
    dcc.RangeSlider(
        id ='year-sld1',
        min = min(year_list),
        max = max(year_list),
        value = [min(year_list), max(year_list)],
        marks = year_dict
        ),
    html.H1(id='stat1',children='Loading...',style={'text-align':'center', 'color':'#32ff0c'}) ])
                                                                             
       ])])
              ],colors={'border':'white','primary':'gold','background':'cornsilk'}
              )]),
      
      dcc.Tab(label = "Chart Tool", id="chart tool", value="Chart", children=[
      dcc.Tabs(id = "subtabs2", value = "WorldChart",children = [
              dcc.Tab(label="World Chart Tool", id="WorldC", value="WorldChart", children=[
                  html.H3('World Chart Tool Showing Attacks from 1970-2018', id='side_title3', style={'text-align':'center', 'color':'white'}),
                  dcc.Dropdown(id='chart_dd', options = chart_dropdown_values, value='region_txt'),
                
                  dcc.Input(id = 'search', placeholder = 'Search Here..',style={'backgroundColor':'white', 'align':'center', 'width':1320}),
                 
                  dcc.Graph(id='areagraph'),
                  
                  dcc.RangeSlider(
                      id ='year-sld2',
                      min = min(year_list),
                      max = max(year_list),
                      value = [min(year_list), max(year_list)],
                      marks = year_dict
                      ),
                  html.H1(id='stat2',children='Results',style={'text-align':'center', 'color':'#32ff0c'})
                  
                  ]),
                  
              dcc.Tab(label="India Chart Tool", id="IndiaC", value="IndiaChart", children=[
                  html.H3('India Chart Tool Showing Attacks from 1970-2018', id='side_title4', style={'text-align':'center', 'color':'white'}),

                  dcc.Dropdown(id='chart_dd1', options = chart_dropdown_values, placeholder='Select Option', 
                               value='region_txt',style={'backgroundColor':'white'}),
                 
                  dcc.Input(id = 'search1', placeholder = 'Search Here..', style={'backgroundColor':'white', 'align':'center', 'width':1320}),
                 
                  dcc.Graph(id='areagraph1'),
                  
                  dcc.RangeSlider(
                      id ='year-sld3',
                      min = min(year_list),
                      max = max(year_list),
                      value = [min(year_list), max(year_list)],
                      marks = year_dict
                      ),
                  html.H1(id='stat3',children='Results',style={'text-align':'center', 'color':'#32ff0c'})
                  ]),
              
              ],colors={'border':'white','primary':'gold','background':'cornsilk'}),
      ])
      ],colors={'border':'white','primary':'gold','background':'cornsilk'}),
     
  ],style={'background-image':'url(/assets/c4.jpg)', })
    return main_layout


   
'''#f3042e''' 

    
#to show the loading image when updating is in process  
@app.callback(Output("loading-output-2", "children"), [Input("graph-obj1", "figure")])
def input_triggers_spinner(value):

    return value

@app.callback(Output("loading-output-1", "children"), [Input("graph-obj", "figure")])
def input_triggers_spinner1(value):

    return value
     

#to filter the graph in world chart tool
@app.callback(
    dash.dependencies.Output('areagraph','figure'),
    [ 
    dash.dependencies.Input('chart_dd','value'),
    dash.dependencies.Input('search','value'),
    dash.dependencies.Input('year-sld2', 'value'),])

#For world chart tool    
def update_app_ui3(chart_dp_value, search, year_selector):
    
            
            chart_df = pd.DataFrame()         #same as the above
            year_range = [x for x in range(year_selector[0],year_selector[1]+1)]
            
            for i in year_range:
                tmpdf = pd.DataFrame(df[df['iyear'] == i])
                chart_df = chart_df.append(tmpdf)
            
   
            if chart_dp_value is not None:
                if search is not None:
                    chart_df = chart_df.groupby('iyear')[chart_dp_value].value_counts().reset_index(name='count')    #to merge the data using count of the region occured
                    chart_df = chart_df[chart_df[chart_dp_value].str.contains(search, case=False)]      #to filter the data using search bar
                else:
                    chart_df = chart_df.groupby('iyear')[chart_dp_value].value_counts().reset_index(name='count')
                    
                    print('chart_df is',chart_df)
                    
            else:
                raise PreventUpdate
            
            
            
            chartFigure = px.area(chart_df, x='iyear', y='count', color = chart_dp_value, height = 500)
            fig = chartFigure
       
            return fig
        
        
#to filter the graph in india chart tool     
@app.callback(
    dash.dependencies.Output('areagraph1','figure'),
    [
     
     dash.dependencies.Input('chart_dd1','value'),
     dash.dependencies.Input('search1','value'),
     dash.dependencies.Input('year-sld3', 'value')
    ])

     
def update_app_ui4(chart_dp_value, search, year_selector):
    
            chart_df = pd.DataFrame()         #same as the above
            year_range = [x for x in range(year_selector[0],year_selector[1]+1)]
            
            for i in year_range:
                tmpdf = pd.DataFrame(df[df['iyear'] == i])
                chart_df = chart_df.append(tmpdf)
            
            
            chart_df = chart_df[(chart_df['region_txt']=='South Asia') &(chart_df['country_txt']=='India')]
   
            if chart_dp_value is not None:
                if search is not None:
                    chart_df = df.groupby('iyear')[chart_dp_value].value_counts().reset_index(name='count')    #to merge the data using count of the region occured
                    chart_df = chart_df[chart_df[chart_dp_value].str.contains(search, case=False)]
                else:
                    chart_df = chart_df.groupby('iyear')[chart_dp_value].value_counts().reset_index(name='count')
                    
                    if chart_dp_value == 'natlty1_txt':      
                        chart_df = chart_df[chart_df['natlty1_txt']=='India']     #to show the data based on india
                    if chart_dp_value == 'weaptype1_txt':
                         print('chart df is', chart_df)
                    if chart_dp_value == 'region_txt':
                        chart_df = chart_df[chart_df['region_txt']=='South Asia']
                    if chart_dp_value == "country_txt":
                        chart_df = chart_df[chart_df['country_txt']=='India']
                   
                    
            else:
                raise PreventUpdate
            
            chartFigure = px.area(chart_df, x='iyear', y='count', color = chart_dp_value,height = 500)
            fig = chartFigure
       
            return fig
      
    
      
    
    
   
    
    

@app.callback(
    [Output('graph-obj', 'figure'),
    Output('stat', 'children')],
    [Input('month-dd', 'value'),
      Input('day-dd', 'value'),
     Input('region-dd', 'value'),
     Input('country-dd', 'value'),
     Input('state-dd', 'value'),
     
     Input('city-dd', 'value'),
     Input('attack-dd', 'value'),
     Input('year-sld', 'value'),
     ]
    
    )

#to filter the graph in world map tool
def update_app_ui( month_value, day_value,  region_value, country_value, 
                  state_value,city_value,attack_value,year_value):
    
   
    global dfnew
    dfnew = df      # dfnew so that if we unselect option, it must show the previous result

    if(year_value != None):
        global df1
        n = [x for x in range(year_value[0],year_value[1]+1)]
        df1 = pd.DataFrame()
        print(n)
        for i in n:
            df2 = pd.DataFrame(df[df['iyear'] == i])
            df1 = df1.append(df2)
        dfnew = df1       
            
    if (month_value != None):
        dfnew = df1              #before changing df1 value, i need to store the values in dfnew so if we unselect we get the previous values
        df1 = pd.DataFrame(df[df['imonth'].isin(month_value)])
             
             
        if (day_value != None):
            dfnew = df1 
            dfd = pd.DataFrame(df[df['iday'].isin(day_value)])
            df1 = df1.merge(dfd)
            print('df1 is',df1)
    
    if(region_value != None):
        dfnew = df1 
        df3 = pd.DataFrame(df[df['region_txt'].isin(region_value)])
        df1 = df1.merge(df3)
        print(df1)
        
     
            
        if (country_value != None):
             dfnew = df1 
             dfc = pd.DataFrame(df[df['country_txt'].isin(country_value)])
             df1 = df1.merge(dfc)
             
        if (state_value != None):
             dfnew = df1 
             dfs = pd.DataFrame(df[df['provstate'].isin(state_value)])
             df1 = df1.merge(dfs)
                 
        if (city_value != None):
            dfnew = df1 
            dfy = pd.DataFrame(df[df['city'].isin(city_value)])
            df1 = df1.merge(dfy)
                     
        if(attack_value != None):
            dfnew = df1 
            dfa = pd.DataFrame(df[df['attacktype1_txt'].isin(attack_value)])
            df1 = df1.merge(dfa)
                         
       
    
            
            
    if (attack_value != None):
        dfnew = df1 
        dfa = pd.DataFrame(df[df['attacktype1_txt'].isin(attack_value)])
        df1 = df1.merge(dfa)   
    
        
    if df1.empty:
            value = 'Results Found'
            fig = px.scatter_mapbox(dfnew, lat=dfnew["latitude"], lon=dfnew["longitude"], hover_name=dfnew["city"], hover_data=['region_txt','country_txt','provstate','city','attacktype1_txt','nkill','imonth','iday'], 
                color='attacktype1_txt', zoom=2, height=500)
            fig.update_layout(mapbox_style="open-street-map")
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    else:
        value = 'Results Found'
        print(df1)
        fig = px.scatter_mapbox(df1, lat=df1["latitude"], lon=df1["longitude"], hover_name=df1["city"],hover_data=['region_txt','country_txt','provstate','city','attacktype1_txt','nkill','imonth','iday'], 
                color='attacktype1_txt', zoom=2, height=500)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
 
    return fig, value



#to filter the country options based on region in world map tool  
@app.callback(
    Output('country-dd', 'options'),
    [Input('region-dd', 'value')
     
     ]
    )
    
def update_country(region):
    print('region type is',type(region))
    
    if region is None:
        return None
    else:
        return [{'label':str(i),'value':str(i)}for i in df[df['region_txt'].isin(region)]['country_txt'].unique().tolist()]

#to filter the state options based on  in world map tool    
@app.callback(
    Output('state-dd', 'options'),
    [Input('country-dd', 'value')
     
     ]
    )
    
def update_state(country):
    if country is None:
        return None
    else:
        return [{'label':str(i),'value':str(i)}for i in df[df['country_txt'].isin(country)]['provstate'].unique().tolist()]
   

#to filter the city options based on state in world map tool    
@app.callback(
    Output('city-dd', 'options'),
    [Input('state-dd', 'value')
     
     ]
    )

def update_city(state):
    if state is None:
        return None
    else:
        return [{'label':str(i),'value':str(i)}for i in df[df['provstate'].isin(state)]['city'].unique().tolist()]
        


#to filter the graph in india map tool
@app.callback(
    [Output('graph-obj1', 'figure'),
    Output('stat1', 'children')],
    [Input('month-dd1', 'value'),
      Input('day-dd1', 'value'),
     Input('region-dd1', 'value'),
     Input('country-dd1', 'value'),
     Input('state-dd1', 'value'),
     
     Input('city-dd1', 'value'),
     Input('attack-dd1', 'value'),
     Input('year-sld1', 'value'),
     ]
    
    )
def update_app_ui2( month_value, day_value,  region_value, country_value, 
                  state_value,city_value,attack_value,year_value):
    
   
    if(region_value != None):
            df1 = pd.DataFrame()
            dfnew = pd.DataFrame()
            n = [x for x in range(year_value[0],year_value[1]+1)]
            for i in n:
                df2 = pd.DataFrame(df[df['iyear'] == i])
                df1 = df1.append(df2)
           
            
            df3 = pd.DataFrame(df[df['region_txt']==(region_value)])
            df1 = df1.merge(df3)
            dfnew = df1
            print(df1)
        
            if (country_value != None):
                dfnew = df1
                dfc = pd.DataFrame(df[df['country_txt']==(country_value)])
                df1 = df1.merge(dfc)
    
             
            
        
                if (month_value != None):
                    dfnew = df1
                    dfm = pd.DataFrame(df[df['imonth'].isin(month_value)])
                    df1 = df1.merge(dfm)
                    
             
             
                if (day_value != None):
                    dfnew = df1
                    dfd = pd.DataFrame(df[df['iday'].isin(day_value)])
                    df1 = df1.merge(dfd)
     
            
        
             
                if (state_value != None):
                    dfnew = df1
                    dfs = pd.DataFrame(df[df['provstate'].isin(state_value)])
                    df1 = df1.merge(dfs)
                 
                if (city_value != None):
                    dfnew = df1
                    dfy = pd.DataFrame(df[df['city'].isin(city_value)])
                    df1 = df1.merge(dfy)
                     
                if(attack_value != None):
                    dfnew = df1
                    dfa = pd.DataFrame(df[df['attacktype1_txt'].isin(attack_value)])
                    df1 = df1.merge(dfa)
            
        
        
                         
    
            
    if df1.empty:
        value = 'No Results Found'
        fig = px.scatter_mapbox(dfnew, lat=dfnew["latitude"], lon=dfnew["longitude"], hover_name=dfnew["city"], hover_data=['region_txt','country_txt','provstate','city','attacktype1_txt','nkill','imonth','iday'],
                color='attacktype1_txt', zoom=2, height=500)
        fig.update_layout(mapbox_style="open-street-map")
            
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    else:
        value = 'Results Found'
        print('the df1 in month is',df1) 
        fig = px.scatter_mapbox(df1, lat=df1["latitude"], lon=df1["longitude"], hover_name=df1["city"],hover_data=['region_txt','country_txt','provstate','city','attacktype1_txt','nkill','imonth','iday'], 
                color='attacktype1_txt', zoom=2, height=500)
        fig.update_layout(mapbox_style="open-street-map")
            
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

        

 
    return fig, value

#to filter the state value based on country selected in india map tool
@app.callback(
    Output('state-dd1', 'options'),
    [Input('country-dd1', 'value')
     
     ]
    )
    
def update_state1(country):
    return [{'label':str(i),'value':str(i)}for i in df[df['country_txt']==country]['provstate'].unique().tolist()]
   

#to filter the city value based on state selected in india map tool    
@app.callback(
    Output('city-dd1', 'options'),
    [Input('state-dd1', 'value')
     
     ]
    )

def update_city1(state):
    if state==None:
        return [{'label':str(i),'value':str(i)}for i in df[df['provstate']==(state)]['city'].unique().tolist()]
    else:
        return [{'label':str(i),'value':str(i)}for i in df[df['provstate'].isin(state)]['city'].unique().tolist()]
        
    
#to reset the values selected in world map tool
@app.callback(
    [dash.dependencies.Output('month-dd', 'value'),
     dash.dependencies.Output('day-dd', 'value'),
     dash.dependencies.Output('region-dd', 'value'),
     dash.dependencies.Output('country-dd', 'value'),
     dash.dependencies.Output('state-dd', 'value'),
     dash.dependencies.Output('city-dd', 'value'),
     dash.dependencies.Output('attack-dd', 'value'),
     dash.dependencies.Output('close_button', 'value')],
     
    
    [dash.dependencies.Input('close_button', 'n_clicks')]
    
    )


def update_reset(n_clicks):
    print('Value Passed =', str(n_clicks))
    
    if n_clicks > 0:
        n_clicks = 0
        return None,None,None,None,None,None,None,0 


#to reset the values selected in india map tool
@app.callback(
    [dash.dependencies.Output('month-dd1', 'value'),
     dash.dependencies.Output('day-dd1', 'value'),
     dash.dependencies.Output('state-dd1', 'value'),
     dash.dependencies.Output('city-dd1', 'value'),
     dash.dependencies.Output('attack-dd1', 'value'),
     dash.dependencies.Output('close_button1', 'value')],
     
    
    [dash.dependencies.Input('close_button1', 'n_clicks')]
    
    )

def update_reset1(n_clicks):
    print('Value Passed =', str(n_clicks))
    
    if n_clicks > 0:
        n_clicks = 0
        return None,None,None,None,None,0 

def main():
    sys.stdout.write("Hello Akii")
    load_data()
    open_browser()
    
    global app             #to use the global variable inside the function
    app.title = 'terrorism'
    app.layout = create_app_ui() #to create a look and view (blank page or blank card)
    app.run_server()        #to run the server
    
    app=None 
    
    print("thankyou akii")

if __name__=='__main__':
    print("Hi")
    main()
