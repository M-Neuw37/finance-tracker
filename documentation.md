This streamlit app is run from the shell using the command `streamlit run main.py` from the relevant directory. There are two pages to the app, the main page (the dashboard) displays the total amount of the various metrics found on the paycheck.
You can view the totals for the calendar year or the current tax year and display the full CSV file (and the induvidial months) to see the standalone earnings. 

The second page hosts the cumulative graphs and are just a visual representaion on what is displayed in the columns on the main dashboard. 

The CSV for the app is in the format shown in the table below. 
| Year | Tax.Year | Month | Basic.Pay | Tax | NI | Pension Contribution | Total.Deducts | Take.Home | Invested | Kept | Saved |
|------|----------|-------|-----------|-----|----|----------------------|---------------|-----------|----------|------|-------|

` Pension Contribution` should be changed to something along the lines of `[companyname].Pension` and ensure this is changed in the script. 
