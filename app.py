import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="DataInsight AI",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("📊 DataInsight AI")

st.subheader("AI-Powered Data Analytics Platform")

st.write(
    "Upload a CSV dataset and automatically clean, "
    "profile and analyze your data."
)


# =========================================================
# CSV UPLOAD
# =========================================================

uploaded_file = st.file_uploader(
    "📁 Upload your CSV file",
    type=["csv"]
)


# =========================================================
# MAIN APPLICATION
# =========================================================

if uploaded_file is not None:

    # -----------------------------------------------------
    # READ CSV
    # -----------------------------------------------------

    df = pd.read_csv(uploaded_file)

    st.success("✅ CSV uploaded successfully!")


    # =====================================================
    # DATASET OVERVIEW
    # =====================================================

    st.header("📋 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Rows",
            df.shape[0]
        )

    with col2:
        st.metric(
            "Columns",
            df.shape[1]
        )

    with col3:
        st.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

    with col4:
        st.metric(
            "Duplicate Rows",
            int(df.duplicated().sum())
        )


    # =====================================================
    # DATASET PREVIEW
    # =====================================================

    st.header("🔍 Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )


    # =====================================================
    # DATA QUALITY ASSESSMENT
    # =====================================================

    st.header("🔎 Data Quality Assessment")


    # Missing values

    missing_values = df.isnull().sum()

    missing_values = missing_values[
        missing_values > 0
    ]


    if len(missing_values) > 0:

        st.warning("⚠️ Missing values detected")

        missing_table = pd.DataFrame({
            "Column": missing_values.index,
            "Missing Values": missing_values.values
        })

        st.dataframe(
            missing_table,
            use_container_width=True
        )

    else:

        st.success("✅ No missing values detected")


    # Duplicate rows

    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:

        st.warning(
            f"⚠️ {duplicate_count} duplicate rows detected"
        )

    else:

        st.success(
            "✅ No duplicate rows detected"
        )


    # =====================================================
    # AUTOMATED DATA CLEANING
    # =====================================================

    st.header("🧹 Automated Data Cleaning")

    cleaned_df = df.copy()


    # -----------------------------------------------------
    # NUMERICAL COLUMNS
    # -----------------------------------------------------

    numerical_columns = cleaned_df.select_dtypes(
        include=["number"]
    ).columns


    # Fill missing numerical values with median

    for column in numerical_columns:

        if cleaned_df[column].isnull().sum() > 0:

            median_value = cleaned_df[column].median()

            cleaned_df[column] = cleaned_df[column].fillna(
                median_value
            )


    # -----------------------------------------------------
    # CATEGORICAL COLUMNS
    # -----------------------------------------------------

    categorical_columns = cleaned_df.select_dtypes(
        include=["object"]
    ).columns


    # Fill missing categorical values with mode

    for column in categorical_columns:

        if cleaned_df[column].isnull().sum() > 0:

            mode_value = cleaned_df[column].mode()

            if len(mode_value) > 0:

                cleaned_df[column] = cleaned_df[column].fillna(
                    mode_value[0]
                )


    # -----------------------------------------------------
    # REMOVE DUPLICATES
    # -----------------------------------------------------

    cleaned_df = cleaned_df.drop_duplicates()


    st.success("✅ Automated cleaning completed!")


    # =====================================================
    # CLEANING SUMMARY
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Original Rows",
            len(df)
        )

    with col2:

        st.metric(
            "Cleaned Rows",
            len(cleaned_df)
        )

    with col3:

        st.metric(
            "Rows Removed",
            len(df) - len(cleaned_df)
        )


    # =====================================================
    # CLEANED DATASET
    # =====================================================

    st.header("✨ Cleaned Dataset")

    st.dataframe(
        cleaned_df,
        use_container_width=True
    )


    # =====================================================
    # DOWNLOAD CLEANED DATASET
    # =====================================================

    csv_data = cleaned_df.to_csv(
        index=False
    ).encode("utf-8")


    st.download_button(
        label="⬇️ Download Cleaned CSV",
        data=csv_data,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )


    # =====================================================
    # DATASET PROFILING
    # =====================================================

    st.header("📊 Dataset Profiling")


    # Detect column types

    numerical_columns = cleaned_df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    categorical_columns = cleaned_df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()


    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🔢 Numerical Columns")

        if numerical_columns:

            for column in numerical_columns:

                st.write(f"• {column}")

        else:

            st.write("No numerical columns found.")


    with col2:

        st.subheader("🔤 Categorical Columns")

        if categorical_columns:

            for column in categorical_columns:

                st.write(f"• {column}")

        else:

            st.write("No categorical columns found.")


    # =====================================================
    # STATISTICAL SUMMARY
    # =====================================================

    st.header("📈 Statistical Analysis")


    if numerical_columns:

        st.subheader("Numerical Statistics")

        statistics = cleaned_df[numerical_columns].describe().T

        statistics = statistics.rename(
            columns={
                "count": "Count",
                "mean": "Mean",
                "std": "Std Dev",
                "min": "Minimum",
                "25%": "25th Percentile",
                "50%": "Median",
                "75%": "75th Percentile",
                "max": "Maximum"
            }
        )

        st.dataframe(
            statistics.round(2),
            use_container_width=True
        )

    else:

        st.info("No numerical columns available for statistical analysis.")


    # =====================================================
    # COLUMN PROFILING
    # =====================================================

    st.header("🔬 Column Profiling")


    profile_data = []

    for column in cleaned_df.columns:

        profile_data.append({
            "Column": column,
            "Data Type": str(cleaned_df[column].dtype),
            "Unique Values": cleaned_df[column].nunique(),
            "Missing Values": cleaned_df[column].isnull().sum(),
            "Missing %": round(
                cleaned_df[column].isnull().mean() * 100,
                2
            )
        })


    profile_df = pd.DataFrame(profile_data)


    st.dataframe(
        profile_df,
        use_container_width=True
    )


    # =====================================================
    # VISUAL ANALYTICS
    # =====================================================

    st.header("📊 Interactive Visual Analytics")


    # -----------------------------------------------------
    # HISTOGRAM
    # -----------------------------------------------------

    if numerical_columns:

        st.subheader("📊 Distribution Analysis")

        selected_column = st.selectbox(
            "Select a numerical column",
            numerical_columns
        )


        fig = px.histogram(
            cleaned_df,
            x=selected_column,
            title=f"Distribution of {selected_column}",
            marginal="box"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # -----------------------------------------------------
    # BOX PLOT
    # -----------------------------------------------------

    if numerical_columns:

        st.subheader("📦 Outlier Analysis")

        box_column = st.selectbox(
            "Select a column for box plot",
            numerical_columns,
            key="box_column"
        )


        fig_box = px.box(
            cleaned_df,
            y=box_column,
            title=f"Box Plot of {box_column}"
        )


        st.plotly_chart(
            fig_box,
            use_container_width=True
        )


    # -----------------------------------------------------
    # CATEGORICAL BAR CHART
    # -----------------------------------------------------

    if categorical_columns:

        st.subheader("📊 Category Analysis")

        category_column = st.selectbox(
            "Select a categorical column",
            categorical_columns
        )


        category_counts = (
            cleaned_df[category_column]
            .value_counts()
            .reset_index()
        )


        category_counts.columns = [
            category_column,
            "Count"
        ]


        fig_category = px.bar(
            category_counts,
            x=category_column,
            y="Count",
            title=f"Distribution of {category_column}"
        )


        st.plotly_chart(
            fig_category,
            use_container_width=True
        )


    # =====================================================
    # CORRELATION HEATMAP
    # =====================================================

    if len(numerical_columns) >= 2:

        st.subheader("🔥 Correlation Analysis")


        correlation_matrix = cleaned_df[
            numerical_columns
        ].corr()


        fig_corr = px.imshow(
            correlation_matrix,
            text_auto=True,
            title="Correlation Heatmap",
            aspect="auto"
        )


        st.plotly_chart(
            fig_corr,
            use_container_width=True
        )


    # =====================================================
    # SCATTER PLOT
    # =====================================================

    if len(numerical_columns) >= 2:

        st.subheader("🔵 Relationship Between Variables")


        col1, col2 = st.columns(2)


        with col1:

            x_axis = st.selectbox(
                "X-axis",
                numerical_columns,
                key="x_axis"
            )


        with col2:

            y_axis = st.selectbox(
                "Y-axis",
                numerical_columns,
                key="y_axis"
            )


        fig_scatter = px.scatter(
            cleaned_df,
            x=x_axis,
            y=y_axis,
            title=f"{x_axis} vs {y_axis}"
        )


        st.plotly_chart(
            fig_scatter,
            use_container_width=True
        ) 
        # =====================================================
# AI-POWERED INSIGHTS
# =====================================================

st.header("🤖 AI-Powered Insights")

if api_key:

    if st.button("✨ Generate AI Insights"):

        with st.spinner("🤖 AI is analyzing your dataset..."):

            client = OpenAI(api_key=api_key)

            # Create a compact summary for the AI
            dataset_summary = f"""
Dataset shape:
Rows: {cleaned_df.shape[0]}
Columns: {cleaned_df.shape[1]}

Columns:
{list(cleaned_df.columns)}

Data types:
{cleaned_df.dtypes.to_string()}

Statistical summary:
{cleaned_df.describe(include="all").to_string()}

Missing values:
{cleaned_df.isnull().sum().to_string()}

First rows:
{cleaned_df.head(10).to_string()}
"""

            prompt = f"""
You are an expert data analyst.

Analyze the following dataset summary.

{dataset_summary}

Provide a clear business-friendly analysis.

Include:

1. Overall dataset summary
2. Important patterns
3. Important numerical observations
4. Categorical observations
5. Possible outliers or unusual values
6. Interesting relationships between variables
7. Three actionable insights

Do not invent information that is not supported by the dataset.

Explain the findings in simple language suitable for a beginner.
"""

            response = client.responses.create(
                model="gpt-5.6-luna",
                input=prompt
            )

            st.markdown(response.output_text)

else:

    st.warning(
        "⚠️ OpenAI API key not found. "
        "Add OPENAI_API_KEY to your .env file."
    )