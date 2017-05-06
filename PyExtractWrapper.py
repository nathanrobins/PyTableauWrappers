from tableausdk.Extract import *

def interactive_mode():
    # Intro Message

    # Get Data Type [csv, tsv, anything else?]

    # Identify input file

    # Ask if headers are present

    # Analyze data and guess types (default to string)

    # Confirm data types (Yes, No - Default to String, No - Choose a data type(show options), Exclude)


    # What to do with entries that are of the incorrect type? (Fail, Ignore Row, Set to Null and Flag Row, Set to Null)

    # Build Extract

    # Success/Failure Message



    return None

def analyze_input(data, options):
    # Identify type
    inputType = data.__class__.__name__

    if inputType is None:
        print('No Data Found')
        return None

    # if headers provided
         # Build headers list or dict (check for type mismatch here )
    # if List
        # if types provided

    # if Dict
        # if types provided

    if options['types_specified']:


     and inputType is 'list' :





    return None

