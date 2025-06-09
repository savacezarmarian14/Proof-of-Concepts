import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt


def clean_column_names(df):
    df.columns = df.columns.str.strip()
    return df


def evaluate_results(results_csv):
    if not os.path.exists(results_csv):
        print(f"[ERROR] File not found: {results_csv}")
        return

    df = pd.read_csv(results_csv)
    df = clean_column_names(df)

    df_unique = df.drop_duplicates(subset=['epoch'])

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(df_unique['epoch'], df_unique['metrics/precision'], label='Precision')
    plt.plot(df_unique['epoch'], df_unique['metrics/recall'], label='Recall')
    plt.plot(df_unique['epoch'], df_unique['metrics/mAP_0.5'], label='mAP@0.5')
    plt.plot(df_unique['epoch'], df_unique['metrics/mAP_0.5:0.95'], label='mAP@0.5:0.95')

    plt.xlabel("Epoch")
    plt.ylabel("Score")
    plt.title("Model Evaluation Metrics")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("metrics_plot.png")
    print("[✓] Plot saved as metrics_plot.png")

    # Max values
    print("\n[SUMMARY] Maximum values:")
    print("Precision:", df_unique['metrics/precision'].max())
    print("Recall:", df_unique['metrics/recall'].max())
    print("mAP@0.5:", df_unique['metrics/mAP_0.5'].max())
    print("mAP@0.5:0.95:", df_unique['metrics/mAP_0.5:0.95'].max())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=str, required=True, help="Path to results.csv file")
    args = parser.parse_args()

    evaluate_results(args.csv)
