import streamlit as st

def main():
    st.set_page_config(
        page_title="Sports Person Classifier",
        page_icon=":athletic_shoe:",
        layout="wide"
    )

    st.title("Harry Potter Characters Classifier")

    st.markdown(
        """
        Welcome to the Harry Potter Characters Classifier! Upload an image, and the classifier will predict the character.
        """
    )

    # Your Dropzone code
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Classifying...")

        # Add your classification logic here

        st.success("Classification successful!")
        display_results()  # Define this function to display the classification results

    st.sidebar.header("Probability Scores")
    display_probability_scores()  # Define this function to display the probability scores in the sidebar

if __name__ == "__main__":
    main()
