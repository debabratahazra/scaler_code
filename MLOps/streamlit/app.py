import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time
# import matplotlib.pyplot as plt

# Create a tab
tab1, tab2, tab3 = st.tabs(["Home", "Dataframe", "Stocks"])

# Create a button on the first tab
with tab1:
    st.title("Streamlit Demo App")
    st.header("_Streamlit_ is :blue[cool] :sunglasses:")

    st.subheader("One", divider=True)
    st.write("This is a example of Badge:")
    st.badge("New")
    st.badge("Success", icon=":material/check:", color="green")
    st.markdown(
        ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
    )


    st.subheader("Two", divider=True)
    st.write("Code Bock example:")
    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, language="python")


    st.subheader("Three", divider=True)
    st.write("Hello, *World!* :Debabrata here!")
    st.write(
        pd.DataFrame(
            {
                "first column": [1, 2, 3, 4],
                "second column": [10, 20, 30, 40],
            }
        )
    )

    st.subheader("Four", divider=True)
    df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
    c = (
        alt.Chart(df)
        .mark_circle()
        .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
    )
    st.write(c)

    ###########################
    st.subheader("Five", divider=True)
    _LOREM_IPSUM = """
    Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    """


    def stream_data():
        for word in _LOREM_IPSUM.split(" "):
            yield word + " "
            time.sleep(0.02)

        yield pd.DataFrame(
            np.random.randn(5, 10),
            columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
        )

        for word in _LOREM_IPSUM.split(" "):
            yield word + " "
            time.sleep(0.02)


    if st.button("Stream data"):
        st.write_stream(stream_data)
        
        
    ###############################
    st.subheader("Six")
    st.write("This is a Divider:")
    st.divider()
    st.write("This is a slider:")
    sliver_val = st.slider("This is a slider", 0, 100, (25, 75))
    st.write("Slider value:", sliver_val)


    st.subheader("Seven", divider=True)
    st.write("This is a Echo function:")

    def get_user_name():
        return 'John'

    with st.echo():
        # Everything inside this block will be both printed to the screen
        # and executed.

        def get_punctuation():
            return '!!!'

        greeting = "Hi there, "
        value = get_user_name()
        punctuation = get_punctuation()

        st.write(greeting, value, punctuation)

    # And now we're back to _not_ printing to the screen
    st.write('Done!')


    st.subheader("Eight", divider=True)
    st.write("This is a Latex example:")
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')

    st.text("This is text area.\n[and more text](that's not a Markdown link).")

    st.subheader("Nine", divider=True)
    st.write("This is a HTML example:")
    st.html(
        "<p><span style='text-decoration: line-through double red;'>Debarata here</span>!</p>"
    )

    st.subheader("Help", divider=True)
    st.write("This is a help document:")
    st.help(pd.DataFrame)


# Create content on the second tab
with tab2:
    from dataframe import open_dataframe
    open_dataframe()


with tab3:
    from stock_market import open_stockmarket
    open_stockmarket()