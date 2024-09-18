import openai

# Your OpenAI API Key
API_KEY = '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'
openai.api_key = API_KEY

# Mock crop database for demonstration

# Query the LLM via OpenAI API for crop rotation table
def get_crop_rotation(crops):
    prompt = "what is the best crop rotation method that should be used with {}, {}, {}, and {} in each year? " \
             "make it into a table format with one of the columns as the seasons, make rows and columns with - and | so that it is properly formatted. Just give the table followed by a small explanation of why it works " \
             "Prioritize first crop in the list since it will earn more money".format(crops[3], crops[2], crops[1], crops[0])
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=300)
    return response.choices[0].text.strip()

def main_rotation(CROP_ROTATION_LIST):
    print("Crops for rotation are:")
    for crop in CROP_ROTATION_LIST:
        print("- {}".format(crop))

    rotation_table = get_crop_rotation(CROP_ROTATION_LIST)
    print("\nCrop Rotation Table:")
    return rotation_table

if __name__ == "__main__":
    main_rotation()