import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


sns.set(style="dark")


def create_season_counts_df(df):
    season_counts_df = df.groupby(by="season").total_count.sum().reset_index()

    return season_counts_df


def create_monthly_2011_df(df):
    options = [2011]
    monthly_2011_df = df[df["year"].isin(options)]

    monthly_2011_df = (
        monthly_2011_df.groupby(by="month").total_count.sum().reset_index()
    )

    return monthly_2011_df


def create_monthly_2012_df(df):
    options = [2012]
    monthly_2012_df = df[df["year"].isin(options)]

    monthly_2012_df = (
        monthly_2012_df.groupby(by="month").total_count.sum().reset_index()
    )

    return monthly_2012_df


# import dataset
all_df = pd.read_csv("all_data.csv")


season_counts_df = create_season_counts_df(all_df)
monthly_2011_df = create_monthly_2011_df(all_df)
monthly_2012_df = create_monthly_2012_df(all_df)

# mengurutkan nama bulan
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
monthly_2011_df["month"] = pd.Categorical(
    monthly_2011_df["month"], categories=months, ordered=True
)
monthly_2012_df["month"] = pd.Categorical(
    monthly_2012_df["month"], categories=months, ordered=True
)


# Dashboard title
st.title("Bike Sharing Data Analysis :bike:")


# Visualisasi jumlah rental setiap musim
st.header("Bike Rentals per Season :maple_leaf:")

fig, ax = plt.subplots(figsize=(10, 5))

ax = sns.barplot(
    y="total_count",
    x="season",
    data=season_counts_df.sort_values(by="total_count", ascending=False),
    palette="Greens_r",
)
plt.title("Number of Bike Rentals by Season", loc="center", fontsize=15)
plt.ylabel("Bike Rentals", fontsize=14)
plt.xlabel("Season", fontsize=16)
plt.tick_params(axis="x", labelsize=12)
plt.ticklabel_format(style="plain", axis="y")
ax.bar_label(ax.containers[0], fmt="%.f")

st.pyplot(fig)


# Visualisasi jumlah rental perbulan
st.header("Bike Rentals per Month :crescent_moon:")

year = st.selectbox(label="Select year", options=("2011", "2012"))

# Visualisasi jumlah rental tahun 2011
if "2011" in year:
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))

    sns.lineplot(x="month", y="total_count", data=monthly_2011_df, marker="o")
    plt.title("Total Bike Rentals per Month (2011)", loc="center", fontsize=20)
    plt.ylabel("Bike Rentals", fontsize=14)
    plt.xlabel("Month", fontsize=16)
    plt.xticks(fontsize=10)
    plt.xticks(rotation=45)
    plt.yticks(fontsize=10)

    st.pyplot(fig)


# Visualisasi jumlah rental tahun 2012
if "2012" in year:
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))

    sns.lineplot(x="month", y="total_count", data=monthly_2012_df, marker="o")
    plt.title("Total Bike Rentals per Month (2012)", loc="center", fontsize=20)
    plt.ylabel("Bike Rentals", fontsize=14)
    plt.xlabel("Month", fontsize=16)
    plt.xticks(fontsize=10)
    plt.xticks(rotation=45)
    plt.yticks(fontsize=10)

    st.pyplot(fig)
