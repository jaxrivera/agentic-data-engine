import os
from snowflake_utils import SnowflakeManager
from agent_brain import DataAgent

def run_agentic_pipeline():
    print("🚀 Starting Agentic Data Engine...")
    
    db = SnowflakeManager()
    agent = DataAgent()
    target_table = "DEMO_TABLE" 
    
    print(f"🔍 Inspecting table: {target_table}...")
    try:
        # 1. Get the row count
        count_result = db.execute_query(f"SELECT COUNT(*) FROM {target_table}")
        
        # Check if the result is an error string instead of a list
        if isinstance(count_result, str) and count_result.startswith("Error"):
            print(f"❌ Snowflake Query Failed: {count_result}")
            return

        row_count = int(count_result[0][0])
        
        # 2. Logic to trigger the Agent
        if row_count == 0:
            print(f"⚠️ Alert: {target_table} is EMPTY.")
            print("🧠 Consultation with AI Agent for Root Cause...")
            
            # Simulated failure context
            status = f"CRITICAL: Table {target_table} has 0 rows."
            logs = "Snowflake Error: Integration 'S3_INT' failed. Reason: S3 Access Denied."
            
            rca_report = agent.perform_rca(status, logs)
            
            print("\n--- AI AGENT RCA REPORT ---")
            print(rca_report)
            print("---------------------------\n")
        else:
            print(f"✅ Table {target_table} looks healthy with {row_count} rows.")
            print("💡 To test the AI Agent, try emptying the table with 'TRUNCATE TABLE'.")
            
    except Exception as e:
        print(f"❌ Pipeline Crash: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    run_agentic_pipeline()
