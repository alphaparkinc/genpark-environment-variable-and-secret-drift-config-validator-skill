"""Example usage for Environment Variable & Secret Drift Config Validator."""
from client import EnvConfigDriftValidator

if __name__ == "__main__":
    res = EnvConfigDriftValidator.validate_env_config(
        ["DATABASE_URL", "OPENAI_API_KEY", "PORT"],
        {"DATABASE_URL": "postgres://localhost/db", "OPENAI_API_KEY": "your_api_key_here"}
    )
    print("Deployment Ready:", res["deployment_ready"])
    print("Missing:", res["missing_keys"], "Placeholders:", res["placeholder_keys"])
