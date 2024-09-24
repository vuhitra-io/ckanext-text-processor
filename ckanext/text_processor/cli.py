import click


@click.group(short_help="text_processor CLI.")
def text_processor():
    """text_processor CLI.
    """
    pass


@text_processor.command()
@click.argument("name", default="text_processor")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [text_processor]
