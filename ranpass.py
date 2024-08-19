from app import application
import click
import pyperclip

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command()
@click.option('-l', '--length', type=int, help='Length of password to be generated')
def generate(length):
    logo = """
    +-----------------------------+
    | Thank you for using Ranpass |
    +-----------------------------+
    """
    password = application.generate(int(length))
    try:
        pyperclip.copy(password)
        click.echo('Password has been copied to clipboard\n')
    except Exception:
        click.echo('Could not copy password to clipboad\n')

    click.echo(password)
    click.echo(logo)

if __name__ == '__main__':
    generate()