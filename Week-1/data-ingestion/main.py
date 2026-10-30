
import csv
from config import connect


# STEP 1: READ THE KAGGLE DATASET

records = []

with open("Iris.csv", "r", encoding="utf-8-sig") as file:

    reader = csv.DictReader(file)

    for row in reader:

        record = (
            int(row["Id"]),
            float(row["SepalLengthCm"]),
            float(row["SepalWidthCm"]),
            float(row["PetalLengthCm"]),
            float(row["PetalWidthCm"]),
            row["Species"]
        )

        records.append(record)

print("Dataset loaded successfully!")
print("Total records:", len(records))


# STEP 2: CONNECT TO SOURCE DATABASE

source = connect("source_db")
source_cursor = source.cursor()

# Clear old source records
source_cursor.execute("DELETE FROM iris")

query = """
INSERT INTO iris
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Insert all CSV records into source
source_cursor.executemany(query, records)

source.commit()

print("Data inserted into source database!")


# STEP 3: CONNECT TO TARGET DATABASE

target = connect("target_db")
target_cursor = target.cursor()

# Clear old target records
target_cursor.execute("DELETE FROM iris")
target.commit()

print("Connected to target database!")


# STEP 4: FETCH RECORDS IN BATCHES

source_cursor.execute(
    "SELECT * FROM iris ORDER BY Id"
)

BATCH_SIZE = 25

batch_number = 0

while True:

    batch = source_cursor.fetchmany(BATCH_SIZE)

    if not batch:
        break

    batch_number += 1

    # STEP 5: INSERT BATCH INTO TARGET

    target_cursor.executemany(query, batch)

    target.commit()

    print(
        "Batch", batch_number,
        "inserted successfully:",
        len(batch), "records"
    )


# STEP 6: VALIDATE DATA

source_cursor.execute(
    "SELECT COUNT(*) FROM iris"
)

source_count = source_cursor.fetchone()[0]

target_cursor.execute(
    "SELECT COUNT(*) FROM iris"
)

target_count = target_cursor.fetchone()[0]

print("\n----- VALIDATION -----")

print("Source records:", source_count)
print("Target records:", target_count)

if source_count == target_count:
    print("SUCCESS: Data ingestion completed!")
else:
    print("ERROR: Record counts do not match!")


# STEP 7: CLOSE CONNECTIONS

source_cursor.close()
target_cursor.close()

source.close()
target.close()

print("\nAll database connections closed.")
