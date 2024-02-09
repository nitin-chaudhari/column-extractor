import sqlglot
import sqlglot.expressions as exp
import streamlit as st

st.title("Column Extractor")

with st.form("Column extractor form"):

    # column extracts from select query
    query = st.text_area("Insert select query here",height=50)

    column_names = []

    if query:
        for expression in sqlglot.parse_one(query).find(exp.Select).args["expressions"]:
            if isinstance(expression, exp.Alias):
                column_names.append(expression.text("alias"))
            elif isinstance(expression, exp.Column):
                column_names.append(expression.text("this"))
            elif isinstance(expression,exp.AggFunc):
                column_names.append(expression.text('this'))
    
    submitted = st.form_submit_button("Get Columns")
    if submitted and len(column_names) > 0:
        st.write("Extracted Columns Names",column_names)
    else:
        st.write("Insert select first")