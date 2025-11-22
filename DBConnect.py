import oracledb

# --- Database connection details ---
username = "system"
password = "PassWord"
dsn = "localhost:1521/XE"  # Use XEPDB1 if that's where the table is now

try:
    # Connect to Oracle
    connection = oracledb.connect(user=username, password=password, dsn=dsn)
    print("✅ Connected to Oracle Database")

    cursor = connection.cursor()

    # Run a simple query
    cursor.execute("SELECT empno, ename, job, sal FROM emp")
    rows = cursor.fetchall()

    print("\n📋 EMP Table Data:")
    for row in rows:
        print(row)

except oracledb.DatabaseError as e:
    print("❌ Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()
        print("🔒 Connection closed.")
