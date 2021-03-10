"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neo_list = []
    with open(neo_csv_path, "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            neo_list.append(NearEarthObject(line["pdes"], line["name"], line["diameter"], line["pha"]))
    return neo_list


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches_list = []
    with open(cad_json_path, "r") as f:
        file = json.load(f)
        approaches = file["data"]
        for line in approaches:
            approaches_list.append(CloseApproach(line[0], line[3], line[4], line[7]))
    return approaches_list

