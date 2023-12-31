#!/usr/bin/env python
import os
import sys  # Required for command-line arguments
from return_sam_records import sam_records


def find_sam_entry(entry):
    directory_path = "hvsams"
    sams = sam_records()

    try:
        if entry.startswith("M"):
            file_id = entry.split("_")[1].split(".")[0]
        else:
            file_id = entry.split(".")[0]

        full_filename = file_id + ".sam"

        file_path = os.path.join(directory_path, full_filename)

        with open(file_path, "r") as file:
            results = []
            for line in file:
                sam_entry = str(line.split("\t")[0].strip())

                if sam_entry == entry:
                    # print(line)
                    filtered_df = sams[sams["read_id"] == entry][
                        [
                            "read_id",
                            "sequence",
                            "alignment_score",
                            "sqrt_length_adj_score",
                            "log_length_adj_score",
                            "read_type",
                            "read_length",
                        ]
                    ]
                    for idx, row in filtered_df.iterrows():
                        for column in filtered_df.columns:
                            print(f"{column}: {row[column]}")
                        print("\n")
                    break

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python return_full_sam_record.py <entry>")
        sys.exit(1)

    entry = sys.argv[1]
    find_sam_entry(entry)


if __name__ == "__main__":
    main()
