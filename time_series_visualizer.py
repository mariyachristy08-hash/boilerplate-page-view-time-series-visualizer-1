import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Import data
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    index_col="date",
    parse_dates=True
)

# Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(df.index, df["value"])

    ax.set_title(
        "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and modify data
    df_bar = df.copy()

    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()

    # Calculate average page views for each month of each year
    df_bar = df_bar.groupby(
        ["year", "month"]
    )["value"].mean()

    df_bar = df_bar.unstack()

    # Put months in correct order
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
        "December"
    ]

    df_bar = df_bar[months]

    # Draw bar plot
    fig = df_bar.plot.bar(figsize=(10, 8)).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    # Save image and return fig
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data
    df_box = df.copy()

    df_box["year"] = df_box.index.year
    df_box["month"] = df_box.index.month

    # Create figure with two axes
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Year-wise box plot
    sns.boxplot(
        data=df_box,
        x="year",
        y="value",
        ax=axes[0]
    )

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(
        data=df_box,
        x="month",
        y="value",
        ax=axes[1]
    )

    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Change month numbers to month names
    month_names = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"
    ]

    axes[1].set_xticklabels(month_names)

    # Save image and return fig
    fig.savefig("box_plot.png")
    return fig