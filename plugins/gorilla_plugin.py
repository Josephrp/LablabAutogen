import asyncio
import asyncio.subprocess as subprocess
from typing import List, Dict

class GorillaPlugin:
    _cli_path: str
    _env_info: Dict[str, str]

    """A plugin that uses the Gorilla CLI to perform a series of executions based on a natural language query or high level overview of the user's problem."""


    async def collect_environment_info(self) -> None:
        """
        Collects information about the environment where the commands are executed.
        """
        uname_command = "uname -a"  # This is for Unix-like systems, for Windows use 'systeminfo'
        try:
            process = await subprocess.create_subprocess_shell(
                uname_command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = await process.communicate()

            if process.returncode == 0:
                self._env_info['uname'] = stdout.decode().strip()
            else:
                self._env_info['uname'] = f"Error collecting environment info: {stderr.decode().strip()}"
        except Exception as e:
            self._env_info['uname'] = f"Exception collecting environment info: {str(e)}"

    def compare_environment_info(self, initial_env_info: Dict[str, str], updated_env_info: Dict[str, str]) -> Dict[str, str]:
        """
        Compares the initial and updated environment information and returns the differences.
        """
        changes = {}
        for key in initial_env_info:
            if initial_env_info[key] != updated_env_info.get(key, None):
                changes[key] = {
                    'initial': initial_env_info[key],
                    'updated': updated_env_info.get(key, None)
                }
        return changes

    async def execute_commands(self, natural_language_commands: List[str]):
        # Collect initial environment info
        await self.collect_environment_info()
        initial_env_info = self._env_info.copy()

        for nl_command in natural_language_commands:
            # Pass the natural language command to the Gorilla CLI and get the CLI command
            try:
                process = await subprocess.create_subprocess_shell(
                    f"{self._cli_path} \"{nl_command}\"",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                stdout, stderr = await process.communicate()

                if process.returncode != 0:
                    print(f"Failed to get CLI command for: {nl_command}")
                    print(f"Error: {stderr.decode().strip()}")
                    continue
            except Exception as e:
                print(f"Exception while processing command '{nl_command}': {str(e)}")
                continue

            cli_command = stdout.decode().strip()
            print(f"CLI command to execute: {cli_command}")

            # Execute the CLI command using subprocess without immediate user confirmation
            # User feedback will be collected after all commands have been processed
            process = await subprocess.create_subprocess_shell(
                cli_command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = await process.communicate()

            if process.returncode == 0:
                print(f"Command executed successfully: {cli_command}")
                print(f"Output: {stdout.decode().strip()}")
            else:
                print(f"Command failed: {cli_command}")
                print(f"Error: {stderr.decode().strip()}")

            # Collect updated environment info
            await self.collect_environment_info()
            updated_env_info = self._env_info.copy()

            # Compare initial and updated environment info
            env_changes = self.compare_environment_info(initial_env_info, updated_env_info)
            if env_changes:
                print("Environment changes detected:")
                for key, change in env_changes.items():
                    print(f"{key}: from '{change['initial']}' to '{change['updated']}'")

async def main():
    # Example user input
    user_input = "Generate a report from yesterday's logs and email it to the team"

    # Initialize GorillaPlugin with the path to the Gorilla CLI
    import os
    gorilla_plugin = GorillaPlugin(cli_path=os.getenv('GORILLA_CLI_PATH'))

    # Placeholder for processing the input and generating CLI commands
    # TODO: Implement the logic to process input and generate CLI commands
    cli_commands = ["echo 'Placeholder command'"]

    # Execute commands and handle feedback
    await gorilla_plugin.execute_commands(cli_commands)

if __name__ == "__main__":
    asyncio.run(main())
