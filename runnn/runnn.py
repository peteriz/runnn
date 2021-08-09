import argparse
from typing import Dict, List

from runnn.utils import read_yaml, run_command

APP_KEY = "app"
APP_CMD_PREFIX = "cmd_prefix"
APP_POSITIONAL = "positional"
HP_PARAMS_KEY = "hyperparameters"


class CmdAndArgs:
    def __init__(self, program: str, args: Dict, cmd_prefix: str=None, positional_args: str=None):
        self.program = program
        self._args = args
        self._cmd_prefix = cmd_prefix
        self._positional = positional_args
        self.cmd = self._generate_cmd()

    @property
    def cmd_prefix(self) -> str:
        return self._cmd_prefix

    @property
    def args(self) -> Dict:
        return self._args

    @property
    def positional_args(self):
        return self._positional

    def parse(self, k, v):
        if len(k) > 1:
            arg_str = f"--{k}"
        else:
            arg_str = f"-{k}"
        # TODO: decide whether this is acceptable
        # if type(v) != bool:
        #     arg_str = f"{arg_str}={v}"

        if type(v) == str and len(v.split(" ")) > 1:
            v = '"' + v + '"'
        valid_type = [str, int, float, bool]
        if not any([type(v) == t for t in valid_type]):
            v = str(v).replace(" ", "")

        arg_str = f"{arg_str}={v}"
        return arg_str

    def _generate_cmd(self) -> None:
        # program
        cmd = [f"{self.program}"]

        # add prefix
        if self.cmd_prefix:
            cmd = [f"{self.cmd_prefix}"] + cmd

        # add positional params first
        if self.positional_args:
            cmd = cmd + [f"{self.positional_args}"]

        # add arguments
        arguments = [self.parse(k, v) for k, v in self.args.items()]
        cmd = cmd + arguments
        return cmd

    def get_cmd(self) -> List[str]:
        return self.cmd

    def get_cmd_string(self) -> str:
        return " ".join(self.cmd)

    def run_cmd(self) -> None:
        run_command(self.cmd)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("program", type=str, help="Python program to run")
    parser.add_argument(
        "arguments_file", type=str, help="Arguments yaml file to use to generate the command"
    )
    parser.add_argument("--run", action="store_true", help="Run the command instead of printing")
    return parser.parse_args()


def create_command(program: str, param_dict: Dict) -> CmdAndArgs:
    cmd_prefix = None
    if APP_KEY in param_dict:
        app_dict = param_dict.get(APP_KEY)
        cmd_prefix = app_dict.get(APP_CMD_PREFIX) if APP_CMD_PREFIX in app_dict else None
        positional_args = app_dict.get(APP_POSITIONAL) if APP_POSITIONAL in app_dict else None
    prog_arg_keys = list(param_dict.keys())
    prog_arg_keys.remove(APP_KEY)
    prog_args = {}
    for key in prog_arg_keys:
        key_dict = param_dict.get(key)
        prog_args.update({kd: kv for kd, kv in key_dict.items()})
    new_command = CmdAndArgs(program, prog_args, cmd_prefix, positional_args)
    return new_command


def main() -> None:
    args = parse_args()
    args_dict = read_yaml(args.arguments_file)
    cmd = create_command(args.program, args_dict)

    if args.run:
        cmd.run_cmd()
    else:
        print(cmd.get_cmd_string())


if __name__ == "__main__":
    main()
