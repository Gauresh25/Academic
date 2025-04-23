# Multi-Pass Macroprocessor for Assembly Language (Pass 1)
# This program processes macro definitions from assembly code and generates tables

def macro_processor_pass1(input_file):
    # Initialize data structures
    macro_name_table = {}  # Maps macro names to their definitions
    macro_definition_table = []  # Stores the actual macro code
    parameter_table = {}  # Stores parameters for each macro

    # Read the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    output_lines = []  # For source code after macro removal
    i = 0

    while i < len(lines):
        line = lines[i].strip()
        tokens = line.split()

        # Check for MACRO directive
        if len(tokens) > 1 and tokens[1] == 'MACRO':
            # Extract macro name and parameters
            macro_name = tokens[0]
            params = []

            # If there are parameters after MACRO
            if len(tokens) > 2:
                params = tokens[2].split(',')

            # Store in macro name table with index into definition table
            macro_name_table[macro_name] = len(macro_definition_table)
            parameter_table[macro_name] = params

            # Store the macro definition
            macro_body = []
            i += 1  # Move past the MACRO line

            while i < len(lines) and 'ENDM' not in lines[i].strip().split():
                macro_body.append(lines[i].strip())
                i += 1

            # Add to definition table
            macro_definition_table.append(macro_body)

            # Skip the ENDM line
            i += 1
            continue

        # If not inside a macro definition, add to output
        output_lines.append(line)
        i += 1

    # Return the tables and processed source code
    return {
        'macro_name_table': macro_name_table,
        'macro_definition_table': macro_definition_table,
        'parameter_table': parameter_table,
        'processed_source': output_lines
    }


def display_tables(tables):
    print("\n--- MACRO NAME TABLE ---")
    print("Macro Name\tIndex in Definition Table")
    for name, index in tables['macro_name_table'].items():
        print(f"{name}\t\t{index}")

    print("\n--- PARAMETER TABLE ---")
    print("Macro Name\tParameters")
    for name, params in tables['parameter_table'].items():
        print(f"{name}\t\t{', '.join(params)}")

    print("\n--- MACRO DEFINITION TABLE ---")
    for i, definition in enumerate(tables['macro_definition_table']):
        print(f"\nDefinition {i}:")
        for line in definition:
            print(f"  {line}")

    print("\n--- PROCESSED SOURCE CODE ---")
    for line in tables['processed_source']:
        print(line)


# Example usage
if __name__ == "__main__":
    # Sample input file path (create this file with sample assembly code)
    input_file = "assembly.txt"

    # Process the file
    tables = macro_processor_pass1(input_file)

    # Display the generated tables
    display_tables(tables)

# Sample input file (sample_assembly.txt) content could be:
"""
PROG1 START 0
      LDA   ALPHA
      STA   BETA
ADD   MACRO &X,&Y,&Z
      LDA   &X
      ADD   &Y
      STA   &Z
ENDM
      ADD   GAMMA,DELTA,EPSILON
MULT  MACRO &P,&Q
      LDA   &P
      MUL   &Q
ENDM
      MULT  ALPHA,BETA
      END
"""