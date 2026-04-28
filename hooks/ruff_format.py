import json
import logging
import subprocess
import sys
from pathlib import Path

LOGS_DIR = Path(__file__).parent
LOG_FILE = LOGS_DIR / "ruff_format.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.FileHandler(LOG_FILE, mode="a")],
)
logger = logging.getLogger(__name__)


def main(cwd: str, timeout: int):
    logger.info("=" * 50)
    logger.info("RUFF FIX POSTTOOLUSE HOOK TRIGGERED")
    logger.info(f"cwd: {cwd}")

    # Read hook input from stdin (Claude Code passes JSON)
    try:
        stdin_data = sys.stdin.read()
        if stdin_data.strip():
            hook_input = json.loads(stdin_data)
            logger.info(f"hook_input keys: {list(hook_input.keys())}")
        else:
            hook_input = {}
    except json.JSONDecodeError:
        hook_input = {}

    # Extract file_path from PostToolUse input
    file_path = hook_input.get("tool_input", {}).get("file_path", "")
    logger.info(f"file_path: {file_path}")

    # Only run for Python files
    if not file_path.endswith(".py"):
        logger.info("Skipping non-Python file")
        print(json.dumps({}))
        return

    # Run uv ruff format on the single file
    logger.info(f"Running: uv ruff format {file_path}")
    try:
        result = subprocess.run(
            ["uv", "run", "ruff", "format", file_path],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if stdout:
            for line in stdout.split("\n")[:20]:  # Limit log lines
                logger.info(f"  {line}")

        if result.returncode == 0:
            logger.info("RESULT: PASS - Format successful")
            print(json.dumps({}))
        else:
            logger.info(f"RESULT: BLOCK (exit code {result.returncode})")
            if stderr:
                for line in stderr.split("\n")[:10]:
                    logger.info(f"  stderr: {line}")
            error_output = stdout or stderr or "Format failed"
            print(
                json.dumps(
                    {
                        "decision": "block",
                        "reason": f"Format failed:\n{error_output[:500]}",
                    }
                )
            )

    except subprocess.TimeoutExpired:
        logger.info("RESULT: BLOCK (timeout)")
        print(
            json.dumps(
                {
                    "decision": "block",
                    "reason": "Format timed out after 120 seconds",
                }
            )
        )
    except FileNotFoundError:
        logger.info("RESULT: PASS (uv ruff format not found, skipping)")
        print(json.dumps({}))


if __name__ == "__main__":
    main(cwd=sys.argv[1], timeout=120)
