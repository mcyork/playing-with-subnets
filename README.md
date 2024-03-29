# Exploring CSV File Manipulations

I am exploring how to manipulate odd CSV files to remove artifacts that other systems perceive as errors. The source files are flat representations of hierarchical data. Therefore, one goal is to reintroduce structure by adding redundancy to the leaf records and removing the root nodes.

## Overview

The provided Python script processes CSV files in several ways to clean up and restructure the data:

1. **Newline Removal**: Fields in the CSV file may contain newlines that should be treated as spaces. The script replaces these newlines within fields to ensure each field is properly represented as a single line of text.
2. **Parent-Child Relationship**: In our dataset, rows represent nodes in a hierarchical structure, identifiable by `parent_id` and `subnet_id` columns. The script enhances each child node's data by adding a comment from its parent node, thus enriching the child's contextual information.
3. **Filtering**: The script removes rows representing top-level nodes (root nodes), identified by having a `parent_id` of 0 or blank. This step focuses the dataset on more specific, detailed records.

## How It Works

The script reads the CSV file, performing the following operations:

- Skips initial lines if they contain file artifacts or headers not part of the actual data structure.
- Iterates through the rows to remove newlines within fields and constructs a mapping between `parent_id` and comments for use in later processing.
- Enhances child records with comments from their corresponding parent records, based on the `parent_id`.
- Filters out the records that do not represent specific subnet entries, essentially removing the root nodes from the dataset.

The output is a modified CSV file where each record is more contextually rich and free from the formatting issues that could be seen as errors in other systems.

## Usage

To use the script, you need to have Python installed on your system and a CSV file you wish to process. Run the script with the CSV file as input, and it will generate a new, modified CSV file as output.
