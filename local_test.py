import sys
from core.agent_brain import DataAgent

def test_modular_engine():
    print("🧪 Testing Modular Architecture...")
    try:
        agent = DataAgent()
        print("✅ Core module loaded successfully.")
        
        # Simulated failure
        res = agent.perform_rca("AZURE_SYNC", "Timeout: Snowflake cluster not responding.")
        print("\n--- AI DIAGNOSTIC OUTPUT ---")
        print(res)
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_modular_engine()
