"""Environment Variable & Secret Drift Config Validator.
100% Python Standard Library.
"""

class EnvConfigDriftValidator:
    """Validates runtime environment configuration keys against `.env.example` templates and flags missing or placeholder values."""

    @staticmethod
    def validate_env_config(template_keys: list, runtime_env: dict) -> dict:
        missing_keys = []
        placeholder_keys = []
        placeholder_patterns = {"changeme", "your_api_key", "todo", "xxx", "replace_me"}

        for key in template_keys:
            if key not in runtime_env or str(runtime_env[key]).strip() == "":
                missing_keys.append(key)
            else:
                val = str(runtime_env[key]).strip().lower()
                if any(p in val for p in placeholder_patterns):
                    placeholder_keys.append(key)

        ready = (len(missing_keys) == 0 and len(placeholder_keys) == 0)
        return {
            "deployment_ready": ready,
            "missing_keys": missing_keys,
            "placeholder_keys": placeholder_keys,
            "validated_keys_count": len(template_keys)
        }
