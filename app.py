import pickle
import streamlit as st

# Load the trained model
with open("classifier.pkl", "rb") as f:
    classifier = pickle.load(f)


def predict_note_authentication(WEBSITE, YEAR, PAGE_VIEWS, UNIQUE_VIEWS, AVERAGE_TIME_ON_PAGE_SECONDS, ENTRANCES, EXIT_RATE):
    """
    Predict function to use the classifier.
    """
    prediction = classifier.predict([[WEBSITE, YEAR, PAGE_VIEWS, UNIQUE_VIEWS, AVERAGE_TIME_ON_PAGE_SECONDS, ENTRANCES, EXIT_RATE]])
    return prediction[0]


def main():
    st.title("WEB TRAFIC PRIDICTION")

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Web Trafic Prediction ML App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Input fields as text_input
    WEBSITE = st.text_input("WEBSITE (integer)")
    YEAR = st.text_input("YEAR (integer)")
    PAGE_VIEWS = st.text_input("PAGE_VIEWS (integer)")
    UNIQUE_VIEWS = st.text_input("UNIQUE_VIEWS (integer)")
    AVERAGE_TIME_ON_PAGE_SECONDS = st.text_input("AVERAGE_TIME_ON_PAGE_SECONDS (float)")
    ENTRANCES = st.text_input("ENTRANCES (integer)")
    EXIT_RATE = st.text_input("EXIT_RATE (float)")

    if st.button("Predict"):
        try:
            # Convert inputs to proper types
            WEBSITE_num = int(WEBSITE)
            YEAR_num = int(YEAR)
            PAGE_VIEWS_num = int(PAGE_VIEWS)
            UNIQUE_VIEWS_num = int(UNIQUE_VIEWS)
            AVERAGE_TIME_ON_PAGE_SECONDS_num = float(AVERAGE_TIME_ON_PAGE_SECONDS)
            ENTRANCES_num = int(ENTRANCES)
            EXIT_RATE_num = float(EXIT_RATE)

            # Call prediction function
            result = predict_note_authentication(
                WEBSITE_num, YEAR_num, PAGE_VIEWS_num, UNIQUE_VIEWS_num,
                AVERAGE_TIME_ON_PAGE_SECONDS_num, ENTRANCES_num, EXIT_RATE_num
            )
            st.success(f"The prediction result is: {result}")

        except ValueError:
            st.error("Please enter valid numeric values in all fields.")

    if st.button("About"):
        st.text("Created by You")
        st.text("Built with Streamlit and XGBoost")


if __name__ == "__main__":
    main()
