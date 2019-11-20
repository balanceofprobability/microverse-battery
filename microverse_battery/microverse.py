import subprocess
import click
import toml


class Gooblebox:
    """spin up a detached gnu screen session per worker box"""

    def __init__(self, boxfile: str = "spaceship.toml"):
        self.boxes = toml.load(boxfile)

    def run(self, box_name: str, xvfb: bool = False):
        click.echo("Initializing {}...".format(box_name))
        box = self.boxes[box_name]
        if xvfb == True:
            xvfb_cmd = (
                'export DISPLAY=:0; xvfb-run --server-args="-screen 0, 1280x768x24" -a '
            )
        elif xvfb == False:
            xvfb_cmd = ""
        cmd = "screen -dmS {0} sh -c '{1}miniverse {2} {3} {4} {5} {6}; exec bash'".format(
            box_name,
            xvfb_cmd,
            box["profile_dir"],
            box["email"],
            box["pw"],
            box["url"],
            box["cell_id"],
        )
        subprocess.Popen(cmd, shell=True)

    def runall(self, xvfb: bool = False):
        for box_name in self.boxes.keys():
            self.run(box_name, xvfb)

    @staticmethod
    def kill(box_name: str):
        click.echo("kill {}".format(box_name))
        cmd = "screen -XS {0} quit".format(box_name)
        subprocess.Popen(cmd, shell=True)

    @staticmethod
    def killall():
        click.echo("killall")
        cmd = "killall screen"
        subprocess.Popen(cmd, shell=True)


@click.group()
def cli():
    pass


@cli.command()
@click.argument("box_names", nargs=-1)
@click.option("--xvfb/--no-xvfb", default=False)
def run(box_names, xvfb):
    box = Gooblebox()
    for box_name in box_names:
        box.run(box_name, xvfb)


@cli.command()
@click.argument("box_names", nargs=-1)
def kill(box_names):
    box = Gooblebox()
    for box_name in box_names:
        box.kill(box_name)


@cli.command()
@click.option("--xvfb/--no-xvfb", default=False)
def runall(xvfb):
    box = Gooblebox()
    box.runall(xvfb)


@cli.command()
def killall():
    box = Gooblebox()
    box.killall()
