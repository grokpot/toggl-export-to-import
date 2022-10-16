import click
import pandas

# Use click to take the following arguments: input file, output file, boolean to indicate switching projects and tags
@click.command()
@click.option("--input", default="input.csv", help="CSV export from Toggl")
@click.option("--output", default="output.csv", help="CSV import file to Toggl")
@click.option("--switch", default=False, help="Switch project and tag values")
def main(input, output, switch):
    # Read the input file
    df = pandas.read_csv(input)
    # If switch is true, switch the project and tag columns
    if switch:
        df = df.rename(columns={"Project": "Tags", "Tags": "Project"})
    # Write the output file
    df.to_csv(output, index=False)


if __name__ == "__main__":
    main()
