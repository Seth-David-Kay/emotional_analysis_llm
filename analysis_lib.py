# Accessing the local model using a json request
import requests
import json
import time

# Returns a string response
def generate_full_reponse_gemma(prompt):
    r = requests.post('http://0.0.0.0:11434/api/generate',
                      json={
                          'model': "gemma:2b",
                          'prompt': prompt,
                      },
                      stream=False)
    full_response = ""    
    for line in r.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            json_line = json.loads(decoded_line)
            full_response += json_line.get("response", "")
            if json_line.get("done"):
                break

    # print(full_response)
    return full_response

# Returns average deduction and then number of responses that failed
def compute_average_of_ten (tweet, times_run, debug, print_true):
    start_time = time.time()
    prompt = f"You are given a tweet.\
    Respond only with a number -10 to 10, no words. The number represents how neutral, negative, or positive the tweet is. \
    -10 is a tweet that is very negative, 0 is a tweet that is neutral\
    , and 10 is a tweet that is very positive. Any number in between\
    is along the gradient of negative to neutral to positive, as\
    the numbers become more positive. Here is the quote:\"{tweet}\""

    total_of_responses = 0
    total_number_of_responses = times_run
    total_responses_failed = 0
    for i in range(times_run):
        response = generate_full_reponse_gemma(prompt)
        
        # Get response as an int and add it to our average
            # This MAY fail, so try and if it does just print out an error
            # subtract one from our average division.
            # We don't retry because it may always give an input that is
            # not only an int and we may be caught in an infinite loop.
        try:
            response_as_int = int(response)
            total_of_responses += response_as_int
        except:
            if print_true:
                print("Response conversion failed.")
            total_number_of_responses -= 1
            total_responses_failed += 1
            continue

        if debug:
            print(response)
            print("\n")

    if total_number_of_responses == 0:
        average_deduction = 0
    else:
        average_deduction = total_of_responses / total_number_of_responses

    if debug:
        print(total_of_responses)
        print("\n")
        print(total_number_of_responses)
        print("\n")

    if print_true:
        print(f"Tweet: {tweet}")

        print(f"Average deduction given: {average_deduction}")

        end_time = time.time()

        print(f"Time taken to execute: {(end_time - start_time)}")

    return average_deduction, total_responses_failed