import click

from .transcriber import transcribe_subcommand
# from .util import model_download

@click.group()
def s2tutil():
    pass

s2tutil.add_command(transcribe_subcommand.transcribe)

def main():
    s2tutil()

if __name__ == "__main__":
    main()