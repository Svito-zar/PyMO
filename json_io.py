"""
This file contains the functions that read, crop and write the JSON transcriptions
"""

import json
import numpy as np

def check_json_transcript(json_infile, printout=False):
    """
    Check if everything is fine with the json transcript file

    Args:
        json_file: file with speech transcript
        printout:  weather we need to print for debugging

    Returns:
        nothing, can raise errors
    """
    with open(json_infile, 'r') as file:
        datastore = json.load(file)

    prev_time = 0

    for segment in datastore:

        if printout:
            print('New segment')

        words = segment['alternatives'][0]['words']

        for word in words:

            # Get the word timing
            start_time = float(word['start_time'][0:-1])  # remove s
            end_time = float(word['end_time'][0:-1])  # remove s

            print(start_time)
            assert start_time <= end_time
            assert prev_time <= start_time

            prev_time = end_time

            if printout:
                print(prev_time)

            # Check if we have "'" symbol
            if "'" in word["word"]:
                print(start_time)
                print(word["word"])

    print("Transcript file is alright\n")


def crop_transcript(json_infile, json_outfile, crop_time, goal_time, printout=False):
    """
    Check if everything is fine with the json transcript file

    Args:
        json_file: file with speech transcript
        printout:  weather we need to print for debugging

    Returns:
        nothing, can raise errors
    """
    with open(json_infile, 'r') as file:
        datastore = json.load(file)

    prev_time = 0

    croped_segm = []

    for segment in datastore:

        if printout:
            print('New segment')

        words = segment['alternatives'][0]['words']

        start_time = float(words[0]['start_time'][0:-1])

        for word in words:

            # Get the word timing
            start_time = float(word['start_time'][0:-1])  # remove s
            end_time = float(word['end_time'][0:-1])  # remove s

            #print(start_time)
            assert start_time <= end_time
            assert prev_time <= start_time

            prev_time = end_time

            if printout:
                print(prev_time)

            # Check if we have "'" symbol
            if "'" in word["word"]:
                print(start_time)
                print(word["word"])

        # take only the last part
        if end_time > crop_time:

            # shift the times accordingly

            for w_ind, word in enumerate(words):

                # Get the word timing
                start_time = float(word['start_time'][0:-1])  # remove s
                end_time = float(word['end_time'][0:-1])  # remove s

                new_st_time = start_time - goal_time
                new_end_time = end_time - goal_time

                segment['alternatives'][0]['words'][w_ind]['start_time'] = str(round(new_st_time, 2)) + "s"
                segment['alternatives'][0]['words'][w_ind]['end_time'] = str(round(new_end_time,2)) + "s"

            croped_segm.append(segment)

    with open(json_outfile, 'w') as file_out:
        json.dump(croped_segm, file_out, indent=4, sort_keys=False)


json_in = "/home/tarask/Documents/Datasets/TrinityCollege/raw/Latest_from_Simon_Jun_20/transcript_sanitized/NaturalTalking_31.json"

json_out = "/home/tarask/Documents/Datasets/TrinityCollege/raw/Test_GENEA_2020/Transcripts/TestSeq001.json"


#check_json_transcript(json_in, printout=False)


crop_transcript(json_in, json_in, 0, 0)

#check_json_transcript(json_out, printout=False)


def check():

    prefix = "/home/tarask/Documents/Datasets/TrinityCollege/raw/GENEA_2020/Transcripts/Recording_0"

    #prefix = "/home/tarask/Documents/Datasets/TrinityCollege/raw/Latest_from_Simon_Jun_20/transcript_sanitized/NaturalTalking_0"

    for i in range(30,31):
        json_file = prefix + str(i) + ".json"

        check_json_transcript(json_file, printout=False)
        print(json_file)
