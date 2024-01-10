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

    # Include CSS styles using st.markdown
    st.markdown("""
        <style>
            .card-wrapper {
                margin: 5% 0;
            }
            
            .custom-circle-image {
                width: 10vw; /* note I used vw not px for better responsiveness */
                height: 10vw;
            }

            .custom-circle-image img {
                object-fit: cover;
            }

            .card-title {
                letter-spacing: 1.1px;
            }

            .card-text {
                font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
                font-size: 20px;
                line-height: initial;
            }

            .dropzone {
                border-style: dashed;
            }

            .error {
                font-family: MerriweatherRegular;
                font-size: 30px;
                line-height: initial;
                color: blue;
                text-align: center;
            }

            #classTable {
                font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }

            #classTable td, #classTable th {
                border: 1px solid #ddd;
                padding: 8px;
            }

            #classTable th {
                padding-top: 12px;
                padding-bottom: 12px;
                text-align: left;
                background-color: #4CAF50;
                color: white;
            }
        </style>
    """)

    # The rest of your Streamlit app code here...

if __name__ == "__main__":
    main()
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
