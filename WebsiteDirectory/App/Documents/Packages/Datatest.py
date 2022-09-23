
from dash import dash_table


def table(data):
    df=dash_table.DataTable(data.to_dict('records'),
        
        sort_action='native',
        columns=[
                {"name": i, "id": i} for i in data.columns
            ],
        page_size=50,
        style_data_conditional=[
        {
        'if': 
            {
            'filter_query': '{Videos_with_Mill} =1',
            'column_id': 'View_count'
            },
        'color': 'green',
        'fontWeight': 'bold'
        },],
        style_cell={'textAlign': 'left'},
        style_data={ 'border': '1px solid black',
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white'
                    },
        fixed_columns={ 'headers': True, 'data': 2},
        style_table={'minWidth': '100%'},

        style_header={ 'border': '1px solid black'},
  
        ),
            
    return df




