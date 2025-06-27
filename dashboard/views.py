from django.shortcuts import render
import pandas as pd
import os
from django.conf import settings


def index(request):
    # Load Excel file
    file_path = os.path.join(settings.MEDIA_ROOT, 'employee_data.xlsx')
    df = pd.read_excel(file_path)

    # Preprocess
    df['Age'] = pd.to_datetime('today').year - pd.to_datetime(df['Date_of_Birth']).dt.year
    df['Experience_Years'] = pd.to_datetime('today').year - pd.to_datetime(df['Date_of_Joining']).dt.year
    df['Years_Left'] = df['Retirement_Age'] - df['Age']

    # Dropdown options
    columns = ['Department', 'Job_Title', 'Employment_Type']
    departments = df['Department'].dropna().unique().tolist()

    # GET params
    selected_option = request.GET.get('chart_column', 'Department')
    selected_dept = request.GET.get('department', '')

    # Filter by department
    if selected_dept:
        df = df[df['Department'] == selected_dept]

    # Chart data
    chart_data = df[selected_option].value_counts().to_dict()

    # KPIs
    avg_years_left = round(df['Years_Left'].mean(), 1) if not df.empty else 0
    avg_experience = round(df['Experience_Years'].mean(), 1) if not df.empty else 0
    total_employees = df.shape[0]

    # Line chart data: average experience by age
    line_df = df.groupby('Age')['Experience_Years'].mean().reset_index()
    line_data = {
        "labels": line_df['Age'].tolist(),
        "values": line_df['Experience_Years'].tolist()
    }

    context = {
        'df': df,
        'columns': columns,
        'departments': departments,
        'selected_option': selected_option,
        'selected_dept': selected_dept,
        'chart_data': chart_data,
        'avg_years_left': avg_years_left,
        'avg_experience': avg_experience,
        'line_data': line_data,
        'total_employees': total_employees
    }

    return render(request, 'dashboard\index.html', context)
